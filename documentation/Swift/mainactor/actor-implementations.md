# Actor Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func assertIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](./assertisolated%28_,file,line%29.md)
  Stops program execution if the current task is not executing on this actor’s serial executor.
- [func assumeIsolated<T>((isolated Self) throws -> T, file: StaticString, line: UInt) rethrows -> T](./assumeisolated%28_,file,line%29-swift.method.md)
  Assume that the current task is executing on this actor’s serial executor, or stop program execution otherwise.
- [func preconditionIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](./preconditionisolated%28_,file,line%29.md)
  Stops program execution if the current task is not executing on this actor’s serial executor.
- [func withSerialExecutor<T, E>((any SerialExecutor) throws(E) -> T) throws(E) -> T](./withserialexecutor%28_%29-79jll.md)
  Perform an operation with the actor’s [`SerialExecutor`](../serialexecutor.md).
- [func withSerialExecutor<T, E>(nonisolated(nonsending) (any SerialExecutor) async throws(E) -> T) async throws(E) -> T](./withserialexecutor%28_%29-epjy.md)
  Perform an operation with the actor’s [`SerialExecutor`](../serialexecutor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mainactor/actor-implementations)*