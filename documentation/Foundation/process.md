# Process

**Framework**: Foundation  
**Kind**: class

An object that represents a subprocess of the current process.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class Process
```

#### Overview

Using this class, your program can run another program as a subprocess and monitor that program’s execution. Unlike [`Thread`](thread.md), it doesn’t share memory space with the process that creates it.

A process operates within an environment defined by the current values for several items: the current directory, standard input, standard output, standard error, and the values of any environment variables, inheriting its environment from the process that launches it. If there are any environment variables that should be different for the subprocess (for example, if the current directory needs to change), change it in the instance after initialization, before your app launches it. Your app can’t change a process’s environment while it’s running.

You can only run the subprocess once per instance. Subsequent attempts raise an error.

> ❗ **Important**:  In a sandboxed app, child processes you create with this class inherit the sandbox of the parent app. Instead, write helper apps as XPC Services because it allows you to specify different sandbox entitlements for helper apps. For more information, see [`Daemons and Services Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i) and [`XPC`](https://developer.apple.com/documentation/XPC).

## Topics

### Creating and Initializing
- [class func run(URL, arguments: [String], terminationHandler: ((Process) -> Void)?) throws -> Process](process/run(_:arguments:terminationhandler:).md)
  Creates and runs a task with a specified executable and arguments.
- [init()](process/init.md)
  Returns an initialized process object with the environment of the current process.
### Returning Information
- [var processIdentifier: Int32](process/processidentifier.md)
  The receiver’s process identifier.
### Running and Stopping
- [func run() throws](process/run.md)
  Runs the process with the current environment.
- [func interrupt()](process/interrupt.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](process/resume.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](process/suspend.md)
  Suspends execution of the receiver task.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.
### Querying the State
- [var isRunning: Bool](process/isrunning.md)
  A status that indicates whether the receiver is still running.
- [var terminationStatus: Int32](process/terminationstatus.md)
  The exit status the receiver’s executable returns.
- [var terminationReason: Process.TerminationReason](process/terminationreason-swift.property.md)
  The reason the system terminated the task.
### Configuring
- [var arguments: [String]?](process/arguments.md)
  The command arguments that the system uses to launch the executable.
- [var currentDirectoryURL: URL?](process/currentdirectoryurl.md)
  The current directory for the receiver.
- [var environment: [String : String]?](process/environment.md)
  The environment for the receiver.
- [var executableURL: URL?](process/executableurl.md)
  The receiver’s executable.
- [var qualityOfService: QualityOfService](process/qualityofservice.md)
  The default quality of service level the system applies to operations the task executes.
- [var standardError: Any?](process/standarderror.md)
  The standard error for the receiver.
- [var standardInput: Any?](process/standardinput.md)
  The standard input for the receiver.
- [var standardOutput: Any?](process/standardoutput.md)
  The standard output for the receiver.
### Termination Handler
- [var terminationHandler: ((Process) -> Void)?](process/terminationhandler.md)
  A completion block the system invokes when the task completes.
### Constants
- [Process.TerminationReason](process/terminationreason-swift.enum.md)
  Constants that specify the termination reason values that the system returns.
- [enum QualityOfService](qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.
### Notifications
- [class let didTerminateNotification: NSNotification.Name](process/didterminatenotification.md)
  Posted when the task has stopped execution.
### Deprecated
- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](process/launchedprocess(launchpath:arguments:).md)
  Creates and launches a task with a specified executable and arguments.
- [var currentDirectoryPath: String](process/currentdirectorypath.md)
  Sets the current directory for the receiver.
- [var launchPath: String?](process/launchpath.md)
  Sets the receiver’s executable.
- [func launch()](process/launch.md)
  Launches the task represented by the receiver.
### Structures
- [Process.DidTerminateMessage](process/didterminatemessage.md)
### Instance Properties
- [var launchRequirement: LaunchCodeRequirement?](process/launchrequirement.md)
- [var launchRequirementData: Data?](process/launchrequirementdata.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSUserScriptTask](nsuserscripttask.md)
  An object that executes scripts.
- [class NSUserAppleScriptTask](nsuserapplescripttask.md)
  An object that executes AppleScript scripts.
- [class NSUserAutomatorTask](nsuserautomatortask.md)
  An object that executes Automator workflows.
- [class NSUserUnixTask](nsuserunixtask.md)
  An object that executes unix applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process)*