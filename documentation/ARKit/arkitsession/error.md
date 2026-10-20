# ARKitSession.Error

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

An error that might occur when running data providers on an ARKit session.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Error
```

## Topics

### Inspecting ARKit errors
- [let dataProvider: (any DataProvider)?](./error/dataprovider.md)
  The data provider that causes an error in a session, if any.
- [let code: ARKitSession.Error.Code](./error/code-swift.property.md)
  The error code for an ARKit session error.
- [ARKitSession.Error.Code](./error/code-swift.enum.md)
  The error codes for ARKit sessions.
- [let errorDescription: String?](./error/errordescription.md)
  A localized message that describes the error that occurred.
### Providing recovery suggestions
- [let recoverySuggestion: String?](./error/recoverysuggestion.md)
  A localized message that describes how someone might recover from the error.
- [let failureReason: String?](./error/failurereason.md)
  A localized message that describes why the error occurred.
### Instance Properties
- [var description: String](./error/description.md)
  A textual representation of this error.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Starting and stopping a session
- [convenience init()](./init%28%29.md)
  Creates a new session.
- [func run([any DataProvider]) async throws](./run%28_%29.md)
  Runs a session with the data providers you supply.
- [func stop()](./stop%28%29.md)
  Stops all data providers running in this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/error)*