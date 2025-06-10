# AVDisplayCriteria

**Framework**: AVFoundation  
**Kind**: class

An object the system uses to guide the selection of a display mode in tvOS.

**Availability**:
- tvOS 11.2+
- visionOS 1.0+

## Declaration

```swift
class AVDisplayCriteria
```

#### Overview

In tvOS, this object provides the display criteria that an [`AVDisplayManager`](https://developer.apple.com/documentation/AVKit/AVDisplayManager) uses to set an appropriate display mode, such as switching to HDR, when presenting a video asset. If your app uses [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) for its player user interface, the system automatically applies the display critera when it presents the asset. If you use a custom player interface, load the value of an asset’s [`preferredDisplayCriteria`](avpartialasyncproperty/preferreddisplaycriteria.md) property and set it on the window’s [`avDisplayManager`](https://developer.apple.com/documentation/UIKit/UIWindow/avDisplayManager) object.

> ❗ **Important**:  Most apps don’t create instances of this class, and instead retrieve the preferred display criteria from a media asset. If your app doesn’t use [`AVAsset`](avasset.md), such as a streaming app that renders sample buffers using [`AVSampleBufferDisplayLayer`](avsamplebufferdisplaylayer.md), you can manually create an instance using the [`init(refreshRate:formatDescription:)`](avdisplaycriteria/init(refreshrate:formatdescription:).md) initializer.

## Topics

### Create a display criteria
- [init(refreshRate: Float, formatDescription: CMFormatDescription)](avdisplaycriteria/init(refreshrate:formatdescription:).md)
  Creates a display criteria object with the specified refresh rate and format description.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var preferredRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredrate.md)
  The asset’s rate preference for playing its media.
- [static var preferredVolume: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredvolume-20mb3.md)
  The asset’s volume preference for playing its audible media.
- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](avpartialasyncproperty/preferredtransform-80d13.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [static var preferredDisplayCriteria: AVAsyncProperty<Root, AVDisplayCriteria>](avpartialasyncproperty/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdisplaycriteria)*