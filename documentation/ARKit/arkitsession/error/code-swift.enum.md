# ARKitSession.Error.Code

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The error codes for ARKit sessions.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Determining the cause of session errors
- [ARKitSession.Error.Code.dataProviderFailedToRun](./code-swift.enum/dataproviderfailedtorun.md)
  The error code for when a data provider fails to run.
- [ARKitSession.Error.Code.dataProviderNotAuthorized](./code-swift.enum/dataprovidernotauthorized.md)
  The error code for when a data provider is missing at least one authorization it needs to run.
### Instance Properties
- [var description: String](./code-swift.enum/description.md)
  A textual representation of the code.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting ARKit errors
- [let dataProvider: (any DataProvider)?](./dataprovider.md)
  The data provider that causes an error in a session, if any.
- [let code: ARKitSession.Error.Code](./code-swift.property.md)
  The error code for an ARKit session error.
- [let errorDescription: String?](./errordescription.md)
  A localized message that describes the error that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitsession/error/code-swift.enum)*