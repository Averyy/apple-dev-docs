# ARKitSession.Error

**Framework**: ARKit  
**Kind**: struct

An error that might occur when running data providers on an ARKit session.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct Error
```

## Topics

### Inspecting ARKit errors
- [let dataProvider: (any DataProvider)?](arkitsession/error/dataprovider.md)
  The data provider that caused an error in a session.
- [var code: ARKitSession.Error.Code](arkitsession/error/code-swift.property.md)
  The error code for an ARKit session error.
- [ARKitSession.Error.Code](arkitsession/error/code-swift.enum.md)
  The error codes for ARKit sessions.
- [var errorDescription: String?](arkitsession/error/errordescription.md)
  A localized message that describes the error that occurred.
### Providing recovery suggestions
- [var recoverySuggestion: String?](arkitsession/error/recoverysuggestion.md)
  A localized message that describes how someone might recover from the error.
- [var failureReason: String?](arkitsession/error/failurereason.md)
  A localized message that describes why the error occurred.
### Instance Properties
- [var description: String](arkitsession/error/description.md)
  A textual representation of this error.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init()](arkitsession/init.md)
  Creates a new session.
- [func run([any DataProvider]) async throws](arkitsession/run(_:).md)
  Runs a session with the data providers you supply.
- [func stop()](arkitsession/stop.md)
  Stops all data providers running in this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/error)*