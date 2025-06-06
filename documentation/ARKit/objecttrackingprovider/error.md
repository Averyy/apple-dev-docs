# ObjectTrackingProvider.Error

**Framework**: ARKit  
**Kind**: struct

Values that represent an object-tracking error.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Error
```

## Topics

### Describing an error
- [var code: ObjectTrackingProvider.Error.Code](objecttrackingprovider/error/code-swift.property.md)
  The error code.
- [ObjectTrackingProvider.Error.Code](objecttrackingprovider/error/code-swift.enum.md)
  The enumeration of object-tracking provider error codes.
- [var errorDescription: String?](objecttrackingprovider/error/errordescription.md)
  A localized message that describes an error.
- [var failureReason: String?](objecttrackingprovider/error/failurereason.md)
  A localized message that describes the reason for the failure.
### Inspecting an error
- [let bundle: Bundle?](objecttrackingprovider/error/bundle.md)
  The bundle for the model that failed to load, if the source was a bundle.
- [let name: String?](objecttrackingprovider/error/name.md)
  The name of the model that failed to load, if the source was a bundle.
- [var recoverySuggestion: String?](objecttrackingprovider/error/recoverysuggestion.md)
  A localized message that describes how to recover from the failure.
- [let url: URL?](objecttrackingprovider/error/url.md)
  The URL for the model that failed to load, if the source was a URL.
### Instance Properties
- [var description: String](objecttrackingprovider/error/description.md)
  A textual representation of an error.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: DataProviderState](objecttrackingprovider/state.md)
  The state of an object-tracking provider.
- [var allAnchors: [ObjectAnchor]](objecttrackingprovider/allanchors.md)
  An array of all the object anchors the object-tracking provider is tracking.
- [var anchorUpdates: AnchorUpdateSequence<ObjectAnchor>](objecttrackingprovider/anchorupdates.md)
  An asynchronous sequence of anchors the framework updates.
- [var description: String](objecttrackingprovider/description.md)
  A textual representation of this object tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/error)*