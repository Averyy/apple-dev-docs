# Applying launch environment and library constraints

**Framework**: Security

Limit the libraries your process loads, and the situations where it runs.

#### Overview

Separating a complex app into multiple components with distinct privileges to access a person’s data and resources on their computer is a good security practice. Use launch environment constraints and library constraints to further protect people’s security by limiting how other processes can use your app’s privileged components.

##### Identify the Type of Constraint to Use

Library constraints represent tests of attributes of library files that your process loads, and the kernel blocks your process from loading a library with attributes that don’t match.

Launch environment constraints represent tests of attributes of an executable file involved in launching your process. You can define three types of launch environment constraint:

- **Self constraint**: The constraint applies to the executable that embeds the constraint in its code signature.
- **Parent constraint**: The constraint applies to the executable file for the process that launches the constrained executable, for example by calling `posix_spawn(_:_:_:_:_:_:)`.
- **Responsible constraint**: The constraint applies to the executable file for the process that’s responsible for launching the constrained executable. The app that initiates an [`XPC`](https://developer.apple.com/documentation/xpc) connection is responsible for launching the XPC service. An app that launches a helper process directly is both the parent process and the responsible process for the helper.

The kernel doesn’t launch a process if its executable file contains any embedded launch environment constraints that aren’t satisfied.

*Spawn constraints* are launch constraints that a running process asserts when it’s launching another process. The operating system’s initialization process, `launchd`, uses spawn constraints you define in `launchd` property list files to choose whether to launch your daemon or agent. If the executable file specified in the property list file doesn’t satisfy the spawn constraint, `launchd` doesn’t start it as a launch daemon or agent.

##### Define the Constraints

Create a property list file that describes the constraints appropriate to your component. For launch daemons and launch agents, write the spawn constraint into dictionary that’s the value of the `SpawnConstraint` key in the component’s `launchd` property list file. For library constraints and launch constraints, create a separate property list file with the `.coderequirement` file extension.

For information about the keys and values to add to a constraint property list, see [`Defining launch environment and library constraints`](defining-launch-environment-and-library-constraints.md).

##### Embed the Constraint Into Your Executables Code Signature

To embed a launch constraint or library constraint into the code signature for an executable file, follow these steps:

1. Open your project in Xcode.
2. Select your project in the File navigator.
3. Select the target that builds the executable file in the Project editor.
4. Switch to the Build Settings tab.
5. Set the appropriate build setting in the Signing group to the path to the property list file that contains the constraint definition. For a self constraint, use Launch Constraint Process Plist. For a parent constraint, use Launch Constraint Parent Process Plist. For a responsible process constraint, use Launch Constraint Responsible Process List. For a library constraint, use Library Load Constraint Plist.

![A screenshot of Xcode. The Signing build settings are visible, and the setting for the Launch Constraint Parent Process Plist is being edited.](/images/com.apple.security/media-4257729@2x.png)

For information about the options to use with `codesign` in Terminal, see the UNIX manual page for `codesign`.

> **Note**:  You don’t embed spawn constraints for `launchd` daemons and agents into their executable file’s code signature. Instead, add the constraint to the `SpawnConstraint` key in the daemon or agent’s `launchd` property list file.

##### Diagnose Launch Constraint Failures

When the operating system blocks a process from launching because of an unsatisfied launch constraint, the crash log for the process reports that a launch constraint violation occurred. Additionally, when the operating system detects an unsatisfied launch constraint, it logs a message that you can search for in Console. The log message has this form:

```console
AMFI: Launch Constraint Violation (<enforcement status>), error info: c[<constraint identifier>]p[<process identifier>]m[<match result>]e[<error code>], (<message>) launching proc[vc: <launching process validation category> pid: <launching process pid>]: <launching process path>, launch type <launch type>, failure proc [vc: <failing process validation category> pid: <failing process pid>]: <failing process path>
```

The fields in the log message have the following meanings.

- **`<enforcement status>`**: A string that’s `enforcing` if the operating system blocks process launch; otherwise, it’s `not enforcing`, which indicates that the operating system logs the violation and launches the process.
- **`<constraint identifier>`**: An integer that indicates the type of constraint that’s unsatisfied. The constraint identifier is `4` for failing launch constraints, and `5` for failing spawn constraints. Other values are reserved by the operating system.
- **`<process identifier>`**: An integer that indicates whether the violation refers to (`1`) the process that’s launching; (`2`) the parent of the process that’s launching; or (`3`) the responsible process of the process that’s launching.
- **`<match result>`**: An integer that identifies the reason for the violation. The possible values for the match result are listed in Interpret the match result and error code, below.
- **`<error code>`**: An integer that identifies the error that the operating system detected. The possible values for the error code depend on the match result: see Interpret the match result and error code, below.
- **`<message>`**: A readable string that describes the error.
- **`<launching process validation category>`, `<failing process validation category>`**: An integer that’s the validation category of the process that’s launching, and of the process failing validation, respectively. For a list of values of the validation category, see [`Defining launch environment and library constraints`](defining-launch-environment-and-library-constraints.md).
- **`<launching process pid>`, `<failing process pid>`**: An integer that’s the process identifier of the process that’s launching, and of the process failing validation, respectively.
- **`<launching process path>`, `<failing process path>`**: A string that’s the path to the executable for the process that’s launching, and to the process failing validation, respectively.
- **`<launch type>`**: An integer that identifies the type of process launch. For a list of values of the launch type, see [`Defining launch environment and library constraints`](defining-launch-environment-and-library-constraints.md).

##### Interpret the Match Result and Error Code

The match result integer in a constraint violation log message has one of the following values:

- **`1`**: The process launch doesn’t match a launch constraint that’s present. The error code is `0`.
- **`2`**: The operating system couldn’t parse a launch constraint dictionary. The error code is a value in the list below.
- **`3`**: The process launch violates an operating system policy that isn’t related to the launch constraint. The error code is `255`, and the message contains more information.
- **`4`**: The operating system couldn’t parse a spawn constraint, or the spawn constraint is missing required data. The error code is `1` if the spawn constraint contains unexpected data, or `2` if the spawn constraint isn’t correctly formed.
- **`5`**: The operating system couldn’t match the executable file with the constraint, because the constraint contains a non-optional fact that isn’t defined for the executable file. The error code is a value in the list below.

When the match result is `2` or `5`, the error code has one of these values:

- **`1`**: The launch constraint contains an operator that the operating system doesn’t recognize.
- **`2`**: The launch constraint is empty.
- **`3`**: The launch constraint contains an element that isn’t supported for the operator it applies to.
- **`4`**: The launch constraint contains an operator with no facts or operators to act on.
- **`5`**: The launch constraint contains a fact that the operating system doesn’t recognize.
- **`6`**: The launch constraint has an unknown version, or doesn’t conform to the grammar rules that the operating system expects.
- **`7`**: The operating system can’t parse the launch constraint.

For information on the operators and facts you can use in launch constraints and how to construct valid constraints, see [`Defining launch environment and library constraints`](defining-launch-environment-and-library-constraints.md).

##### Diagnose Library Constraint Failures

If your app, helper, or command-line tool tries to load a dynamic library that doesn’t satisfy the process’s library constraint, the library fails to load. For example, if you use `dlopen(_:_:)` to load the library, the returned handle is `NULL` and the system sets `errno` to `EPERM` (operation not permitted). Additionally, the operating system logs a message that you can search for in Console. The message has this form:

```console
Library Load Constraint Rejection: Rejecting '<library path>' (Team ID: <library team identifier>, platform: <is platform library>) for process '<process name>(<process id>)' (Team ID: <process team identifier>, platform: is <platform process>), reason: Constraint not matched
```

The fields in the log message have the following meanings:

- **`<library path>`**: The path to the library that the process is trying to load.
- **`<library team identifier>`, `<process team identifier>`**: The Apple Developer team ID of the library and the loading process, respectively.
- **`<is platform library>`, `<is platform process>`**: Whether the library and the loading process respectively are part of the operating system.
- **`<process name>`**: The name of the process that’s trying to load the library.
- **`<process id>`**: The process identifier of the process that’s trying to load the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/applying-launch-environment-and-library-constraints)*