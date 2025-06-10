# APActivationPayload

**Framework**: App Clips  
**Kind**: class

Information that’s passed to an App Clip on launch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class APActivationPayload
```

#### Overview

When users launch an App Clip, the platform passes an activation payload to the App Clip as part of an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object. When the App Clip receives the payload, confirm the user’s physical location at the time of the invocation.

For more information, see [`Responding to invocations`](responding-to-invocations.md).

## Topics

### Passing data to the App Clip
- [var url: URL?](apactivationpayload/url.md)
  The URL of the link that launched the App Clip.
### Confirming a person’s physical location
- [func confirmAcquired(in: CLRegion, completionHandler: (Bool, (any Error)?) -> Void)](apactivationpayload/confirmacquired(in:completionhandler:).md)
  Checks whether an App Clip invocation happened at an expected physical location.
### Understanding errors
- [let APActivationPayloadErrorDomain: String](apactivationpayloaderrordomain.md)
  A string that identifies the activation payload’s error domain.
- [struct APActivationPayloadError](apactivationpayloaderror.md)
  An error that an App Clip activation payload returns.
- [APActivationPayloadError.Code](apactivationpayloaderror/code.md)
  Error codes that an App Clip activation payload returns.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Responding to invocations](responding-to-invocations.md)
  Add code to respond to invocations and offer a focused launch experience.
- [Associating your App Clip with your website](associating-your-app-clip-with-your-website.md)
  Enable the system to verify your App Clip to support invocations from your website and devices running iOS 16.3 or earlier.
- [Supporting invocations from your website and the Messages app](supporting-invocations-from-your-website-and-the-messages-app.md)
  Display a Smart App Banner and the App Clip card on your website that people tap to launch your App Clip, and add support for invocations from the Messages app.
- [Confirming a person’s physical location](confirming-a-person-s-physical-location.md)
  Add code to quickly confirm a person’s physical location while respecting their privacy.
- [Launching another app’s App Clip from your app](launching-another-app-s-app-clip-from-your-app.md)
  Enable people to launch another app’s App Clip from your app with App Clip links and offer a rich preview of it with the Link Presentation framework.
- [NSAppClip](../BundleResources/Information-Property-List/NSAppClip.md)
  A collection of keys that an App Clip uses to get additional capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appclip/apactivationpayload)*