# Processes and Threads

**Framework**: Foundation

Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.

## Topics

### Run Loop Scheduling
- [class RunLoop](runloop.md)
  The programmatic interface to objects that manage input sources.
- [class Timer](timer.md)
  A timer that fires after a certain time interval has elapsed, sending a specified message to a target object.
### Process Info
- [class ProcessInfo](processinfo.md)
  A collection of information about the current process.
### Threads and Locking
- [class Thread](thread.md)
  A thread of execution.
- [protocol NSLocking](nslocking.md)
  The elementary methods adopted by classes that define lock objects.
- [class NSLock](nslock.md)
  An object that coordinates the operation of multiple threads of execution within the same application.
- [class NSRecursiveLock](nsrecursivelock.md)
  A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [class NSDistributedLock](nsdistributedlock.md)
  A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [class NSConditionLock](nsconditionlock.md)
  A lock that can be associated with specific, user-defined conditions.
- [class NSCondition](nscondition.md)
  A condition variable whose semantics follow those used for POSIX-style conditions.
### Operations
- [class OperationQueue](operationqueue.md)
  A queue that regulates the execution of operations.
- [class Operation](operation.md)
  An abstract class that represents the code and data associated with a single task.
- [class BlockOperation](blockoperation.md)
  An operation that manages the concurrent execution of one or more blocks.
### Scripts and External Tasks
- [class Process](process.md)
  An object that represents a subprocess of the current process.
- [class NSUserScriptTask](nsuserscripttask.md)
  An object that executes scripts.
- [class NSUserAppleScriptTask](nsuserapplescripttask.md)
  An object that executes AppleScript scripts.
- [class NSUserAutomatorTask](nsuserautomatortask.md)
  An object that executes Automator workflows.
- [class NSUserUnixTask](nsuserunixtask.md)
  An object that executes unix applications.

## See Also

- [XPC](xpc.md)
  Manage secure interprocess communication.
- [Object Runtime](object-runtime.md)
  Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md)
  Use low-level Unix features to manage input and output among files, processes, and the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processes-and-threads)*