# ARKitSession.Error.Code

**Framework**: ARKit  
**Kind**: enum

The error codes for ARKit sessions.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Determining the cause of session errors
- [ARKitSession.Error.Code.dataProviderFailedToRun](arkitsession/error/code-swift.enum/dataproviderfailedtorun.md)
  The error code for when a data provider fails to run.
- [ARKitSession.Error.Code.dataProviderNotAuthorized](arkitsession/error/code-swift.enum/dataprovidernotauthorized.md)
  The error code for when a data provider is missing at least one authorization it needs to run.
### Instance Properties
- [var description: String](arkitsession/error/code-swift.enum/description.md)
  A textual representation of the code.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [let dataProvider: (any DataProvider)?](arkitsession/error/dataprovider.md)
  The data provider that caused an error in a session.
- [var code: ARKitSession.Error.Code](arkitsession/error/code-swift.property.md)
  The error code for an ARKit session error.
- [var errorDescription: String?](arkitsession/error/errordescription.md)
  A localized message that describes the error that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/error/code-swift.enum)*