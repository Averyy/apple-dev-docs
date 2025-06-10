# Actor Implementations

**Framework**: Immersive Media Support

## Topics

### Instance Methods
- [func assertIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](venuedescriptor/assertisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this actor’s serial executor.
- [func assumeIsolated<T>((isolated Self) throws -> T, file: StaticString, line: UInt) rethrows -> T](venuedescriptor/assumeisolated(_:file:line:).md)
  Assume that the current task is executing on this actor’s serial executor, or stop program execution otherwise.
- [func preconditionIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](venuedescriptor/preconditionisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this actor’s serial executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor/actor-implementations)*