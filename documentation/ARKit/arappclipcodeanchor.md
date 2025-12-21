# ARAppClipCodeAnchor

**Framework**: ARKit  
**Kind**: class

An anchor that tracks the position and orientation of an App Clip Code in the physical environment.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+

## Declaration

```swift
class ARAppClipCodeAnchor
```

#### Overview

Your App Clip gives users immediate access to critical or context-specific parts of your app’s AR experience, and makes it easy for them to download and launch your full app if they choose.

You can use physical App Clip Codes in the real world to enable users to discover your App Clip. An App Clip Code includes a unique URL and can incorporate an NFC tag. When users hold their iPhone near the code or scan it with the camera or Code Scanner in Control Center, the system offers to launch the code’s associated App Clip.

For more on App Clip Codes, see [`App Clips`](https://developer.apple.com/documentation/AppClip). For an app that reacts to App Clip Codes in AR, see [`Interacting with App Clip Codes in AR`](https://developer.apple.com/documentation/AppClip/interacting-with-app-clip-codes-in-ar).

##### Distinguish Between App Clip Codes

There may be multiple App Clip Codes visible in the camera feed that share the same [`url`](arappclipcodeanchor/url.md), so ARKit also relies on the App Clip Code’s location (see [`transform`](aranchor/transform.md)) to distinguish different App Clip Codes in the physical environment.

When the framework recognizes an App Clip Code, it initializes an [`ARAppClipCodeAnchor`](arappclipcodeanchor.md) and passes it to the session delegate via [`session(_:didAdd:)`](arsessiondelegate/session(_:didadd:).md). If a recognized App Clip Code becomes obscured or is no longer visible in the camera feed, the framework sets the anchor’s [`isTracked`](artrackable/istracked.md) property to [`false`](https://developer.apple.com/documentation/Swift/false) and passes it into the [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md) callback. If the same App Clip Code becomes visible once again:

- ARKit sets [`isTracked`](artrackable/istracked.md) to [`true`](https://developer.apple.com/documentation/Swift/true) if the App Clip Code maintained its relative position in the physical environment.
- ARKit intializes a new [`ARAppClipCodeAnchor`](arappclipcodeanchor.md) if the App Clip Code position in the physical environment changed significantly.

##### Remove App Clip Codes

To prevent App Clip Codes from accumulating in the session, ARKit removes anchors by passing them in to the [`session(_:didRemove:)`](arsessiondelegate/session(_:didremove:).md) callback. ARKit removes an [`ARAppClipCodeAnchor`](arappclipcodeanchor.md) if all of the following conditions are true:

- The framework instantiates a new [`ARAppClipCodeAnchor`](arappclipcodeanchor.md).
- The new anchor’s [`url`](arappclipcodeanchor/url.md) matches one or more existing anchors with substantially different positions in the physical environment.
- The existing anchors are untracked ([`isTracked`](artrackable/istracked.md) is [`false`](https://developer.apple.com/documentation/Swift/false)).

## Topics

### Decoding the URL
- [var url: URL?](arappclipcodeanchor/url.md)
  The URL encoded in an App Clip Code.
- [var urlDecodingState: ARAppClipCodeAnchor.URLDecodingState](arappclipcodeanchor/urldecodingstate-swift.property.md)
  A state that indicates the process of decoding an App Clip Code URL.
- [ARAppClipCodeAnchor.URLDecodingState](arappclipcodeanchor/urldecodingstate-swift.enum.md)
  The states in the process of decoding an App Clip code URL.
### Measuring Physical Size
- [var radius: Float](arappclipcodeanchor/radius.md)
  The App Clip Code’s radius in meters.

## Relationships

### Inherits From
- [ARAnchor](aranchor.md)
### Conforms To
- [ARAnchorCopying](aranchorcopying.md)
- [ARTrackable](artrackable.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Interacting with App Clip Codes in AR](../AppClip/interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arappclipcodeanchor)*