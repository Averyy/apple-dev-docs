# Applying launch environment and library constraints

**Framework**: Security

Limit the libraries your process loads, and the situations where it runs.

#### Overview

Separating a complex app into multiple components with distinct privileges to access a person’s data and resources on their computer is a good security practice. Use launch environment constraints and library constraints to further protect people’s security by limiting how other processes can use your app’s privileged components.

##### Identify the Type of Constraint to Use

Library constraints represent tests of attributes of library files that your process loads, and the kernel blocks your process from loading a library with attributes that don’t match.

Launch environment constraints represent tests of attributes of an executable file involved in launching your process. You can define three types of launch environment constraint:

The kernel doesn’t launch a process if its executable file contains any embedded launch environment constraints that aren’t satisfied.

 are launch constraints that a running process asserts when it’s launching another process. The operating system’s initialization process, `launchd`, uses spawn constraints you define in `launchd` property list files to choose whether to launch your daemon or agent. If the executable file specified in the property list file doesn’t satisfy the spawn constraint, `launchd` doesn’t start it as a launch daemon or agent.

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

![A screenshot of Xcode. The Signing build settings are visible, and the setting for the Launch Constraint Parent Process Plist is being edited.](https://docs-assets.developer.apple.com/published/857f404743f04d56847bc38a27f91f5f/media-4257729%402x.png)

For information about the options to use with `codesign` in Terminal, see the UNIX manual page for `codesign`.

> **Note**:  You don’t embed spawn constraints for `launchd` daemons and agents into their executable file’s code signature. Instead, add the constraint to the `SpawnConstraint` key in the daemon or agent’s `launchd` property list file.

 You don’t embed spawn constraints for `launchd` daemons and agents into their executable file’s code signature. Instead, add the constraint to the `SpawnConstraint` key in the daemon or agent’s `launchd` property list file.

##### Diagnose Launch Constraint Failures

When the operating system blocks a process from launching because of an unsatisfied launch constraint, the crash log for the process reports that a launch constraint violation occurred. Additionally, when the operating system detects an unsatisfied launch constraint, it logs a message that you can search for in Console. The log message has this form:

```console
AMFI: Launch Constraint Violation (<enforcement status>), error info: c[<constraint identifier>]p[<process identifier>]m[<match result>]e[<error code>], (<message>) launching proc[vc: <launching process validation category> pid: <launching process pid>]: <launching process path>, launch type <launch type>, failure proc [vc: <failing process validation category> pid: <failing process pid>]: <failing process path>
```

The fields in the log message have the following meanings.

##### Interpret the Match Result and Error Code

The match result integer in a constraint violation log message has one of the following values:

When the match result is `2` or `5`, the error code has one of these values:

For information on the operators and facts you can use in launch constraints and how to construct valid constraints, see [`Defining launch environment and library constraints`](defining-launch-environment-and-library-constraints.md).

##### Diagnose Library Constraint Failures

If your app, helper, or command-line tool tries to load a dynamic library that doesn’t satisfy the process’s library constraint, the library fails to load. For example, if you use `dlopen(_:_:)` to load the library, the returned handle is `NULL` and the system sets `errno` to `EPERM` (operation not permitted). Additionally, the operating system logs a message that you can search for in Console. The message has this form:

```console
Library Load Constraint Rejection: Rejecting '<library path>' (Team ID: <library team identifier>, platform: <is platform library>) for process '<process name>(<process id>)' (Team ID: <process team identifier>, platform: is <platform process>), reason: Constraint not matched
```

The fields in the log message have the following meanings:


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/applying-launch-environment-and-library-constraints)*