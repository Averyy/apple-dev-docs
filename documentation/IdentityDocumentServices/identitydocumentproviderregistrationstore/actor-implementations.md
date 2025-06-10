# Actor Implementations

**Framework**: IdentityDocumentServices

## Topics

### Instance Methods
- [func assertIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](identitydocumentproviderregistrationstore/assertisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this actor’s serial executor.
- [func assumeIsolated<T>((isolated Self) throws -> T, file: StaticString, line: UInt) rethrows -> T](identitydocumentproviderregistrationstore/assumeisolated(_:file:line:).md)
  Assume that the current task is executing on this actor’s serial executor, or stop program execution otherwise.
- [func preconditionIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](identitydocumentproviderregistrationstore/preconditionisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this actor’s serial executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/identitydocumentproviderregistrationstore/actor-implementations)*