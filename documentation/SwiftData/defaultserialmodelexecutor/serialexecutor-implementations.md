# SerialExecutor Implementations

**Framework**: SwiftData

## Topics

### Instance Methods
- [func asUnownedSerialExecutor() -> UnownedSerialExecutor](defaultserialmodelexecutor/asunownedserialexecutor.md)
  Convert this executor value to the optimized form of borrowed executor references.
- [func assertIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](defaultserialmodelexecutor/assertisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this serial executor.
- [func checkIsolated()](defaultserialmodelexecutor/checkisolated.md)
  Last resort “fallback” isolation check, called when the concurrency runtime is comparing executors e.g. during `assumeIsolated()` and is unable to prove serial equivalence between the expected (this object), and the current executor.
- [func enqueue(ExecutorJob)](defaultserialmodelexecutor/enqueue(_:).md)
- [func isSameExclusiveExecutionContext(other: Self) -> Bool](defaultserialmodelexecutor/issameexclusiveexecutioncontext(other:).md)
  If this executor has complex equality semantics, and the runtime needs to compare two executors, it will first attempt the usual pointer-based equality / check, / and if it fails it will compare the types of both executors, if they are the same, / it will finally invoke this method, in an attempt to let the executor itself decide / if this and the `other` executor represent the same serial, exclusive, isolation context.
- [func preconditionIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](defaultserialmodelexecutor/preconditionisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this serial executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultserialmodelexecutor/serialexecutor-implementations)*