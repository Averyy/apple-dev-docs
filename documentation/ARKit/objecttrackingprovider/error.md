# ObjectTrackingProvider.Error

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

Values that represent an object-tracking error.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Error
```

## Topics

### Describing an error
- [var code: ObjectTrackingProvider.Error.Code](./error/code-swift.property.md)
  The error code.
- [ObjectTrackingProvider.Error.Code](./error/code-swift.enum.md)
  The enumeration of object-tracking provider error codes.
- [var errorDescription: String?](./error/errordescription.md)
  A localized message that describes an error.
- [var failureReason: String?](./error/failurereason.md)
  A localized message that describes the reason for the failure.
### Inspecting an error
- [let bundle: Bundle?](./error/bundle.md)
  The bundle for the model that failed to load, if the source was a bundle.
- [let name: String?](./error/name.md)
  The name of the model that failed to load, if the source was a bundle.
- [var recoverySuggestion: String?](./error/recoverysuggestion.md)
  A localized message that describes how to recover from the failure.
- [let url: URL?](./error/url.md)
  The URL for the model that failed to load, if the source was a URL.
### Instance Properties
- [var description: String](./error/description.md)
  A textual representation of an error.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an object-tracking provider
- [var state: DataProviderState](./state.md)
  The state of an object-tracking provider.
- [var allAnchors: [ObjectAnchor]](./allanchors.md)
  An array of all the object anchors the object-tracking provider is tracking.
- [var anchorUpdates: AnchorUpdateSequence<ObjectAnchor>](./anchorupdates.md)
  An asynchronous sequence of anchors the framework updates.
- [var description: String](./description.md)
  A textual representation of this object tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/error)*