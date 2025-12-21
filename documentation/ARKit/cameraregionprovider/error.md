# CameraRegionProvider.Error

**Framework**: ARKit  
**Kind**: struct

A camera region error.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct Error
```

## Topics

### Instance Properties
- [var code: CameraRegionProvider.Error.Code](cameraregionprovider/error/code-swift.property.md)
  The error code.
- [let dataProvider: (any DataProvider)?](cameraregionprovider/error/dataprovider.md)
  The data provider which encountered an error (if any).
- [var description: String](cameraregionprovider/error/description.md)
  A textual representation of this error.
- [var errorDescription: String?](cameraregionprovider/error/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](cameraregionprovider/error/failurereason.md)
  A localized message describing the reason for the failure.
- [var recoverySuggestion: String?](cameraregionprovider/error/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
### Enumerations
- [CameraRegionProvider.Error.Code](cameraregionprovider/error/code-swift.enum.md)
  Enumeration of all possible camera region error codes.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraregionprovider/error)*