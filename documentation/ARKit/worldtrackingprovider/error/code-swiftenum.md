# WorldTrackingProvider.Error.Code

**Framework**: ARKit  
**Kind**: enum

The error codes for errors that world tracking providers throw.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Determining causes for tracking failures
- [WorldTrackingProvider.Error.Code.addWorldAnchorFailed](worldtrackingprovider/error/code-swift.enum/addworldanchorfailed.md)
  The error code for when a world-tracking provider can’t add a world anchor.
- [WorldTrackingProvider.Error.Code.removeWorldAnchorFailed](worldtrackingprovider/error/code-swift.enum/removeworldanchorfailed.md)
  The error code for when a world-tracking provider can’t remove a world anchor.
- [WorldTrackingProvider.Error.Code.worldAnchorLimitReached](worldtrackingprovider/error/code-swift.enum/worldanchorlimitreached.md)
  The error code for when a world-tracking provider reaches its world anchor limit.
### Instance Properties
- [var description: String](worldtrackingprovider/error/code-swift.enum/description.md)
  A textual representation of the code.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [let anchor: WorldAnchor?](worldtrackingprovider/error/anchor.md)
  The anchor that caused a world-tracking error.
- [var code: WorldTrackingProvider.Error.Code](worldtrackingprovider/error/code-swift.property.md)
  The error code.
- [var errorDescription: String?](worldtrackingprovider/error/errordescription.md)
  A localized message that describes the error that occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/error/code-swift.enum)*