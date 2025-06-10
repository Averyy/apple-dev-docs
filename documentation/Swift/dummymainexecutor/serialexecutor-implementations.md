# SerialExecutor Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func asUnownedSerialExecutor() -> UnownedSerialExecutor](dummymainexecutor/asunownedserialexecutor.md)
  Convert this executor value to the optimized form of borrowed executor references.
- [func assertIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](dummymainexecutor/assertisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this serial executor.
- [func isIsolatingCurrentContext() -> Bool](dummymainexecutor/isisolatingcurrentcontext.md)
- [func isSameExclusiveExecutionContext(other: Self) -> Bool](dummymainexecutor/issameexclusiveexecutioncontext(other:).md)
  If this executor has complex equality semantics, and the runtime needs to compare two executors, it will first attempt the usual pointer-based equality / check, / and if it fails it will compare the types of both executors, if they are the same, / it will finally invoke this method, in an attempt to let the executor itself decide / if this and the `other` executor represent the same serial, exclusive, isolation context.
- [func preconditionIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](dummymainexecutor/preconditionisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this serial executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dummymainexecutor/serialexecutor-implementations)*