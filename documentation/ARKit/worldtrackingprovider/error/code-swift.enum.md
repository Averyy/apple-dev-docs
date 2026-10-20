# WorldTrackingProvider.Error.Code

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The error codes for errors that world tracking providers throw.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Determining causes for tracking failures
- [WorldTrackingProvider.Error.Code.addWorldAnchorFailed](./code-swift.enum/addworldanchorfailed.md)
  The error code for when a world-tracking provider can’t add a world anchor.
- [WorldTrackingProvider.Error.Code.removeWorldAnchorFailed](./code-swift.enum/removeworldanchorfailed.md)
  The error code for when a world-tracking provider can’t remove a world anchor.
- [WorldTrackingProvider.Error.Code.worldAnchorLimitReached](./code-swift.enum/worldanchorlimitreached.md)
  The error code for when a world-tracking provider reaches its world anchor limit.
### Instance Properties
- [var description: String](./code-swift.enum/description.md)
  A textual representation of the code.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Inspecting world-tracking errors
- [let anchor: WorldAnchor?](./anchor.md)
  The anchor that caused a world-tracking error.
- [var code: WorldTrackingProvider.Error.Code](./code-swift.property.md)
  The error code.
- [var errorDescription: String?](./errordescription.md)
  A localized message that describes the error that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/error/code-swift.enum)*