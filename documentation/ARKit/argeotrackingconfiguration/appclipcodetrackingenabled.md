# appClipCodeTrackingEnabled

**Framework**: ARKit  
**Kind**: property

A Boolean value that indicates if the framework searches the physical environment for App Clip Codes.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+

## Declaration

```swift
var appClipCodeTrackingEnabled: Bool { get set }
```

#### Discussion

When this property’s value is [`true`](https://developer.apple.com/documentation/swift/true), the session delegate receives an [`ARAppClipCodeAnchor`](arappclipcodeanchor.md) via [`session(_:didAdd:)`](arsessiondelegate/session(_:didadd:).md) for every App Clip Code that ARKit detects in the physical environment. The default value is `false`.

Before calling this function, check that the configuration supports App Clip Code tracking by calling [`supportsAppClipCodeTracking`](argeotrackingconfiguration/supportsappclipcodetracking.md).

To avoid scanning a physical code that’s not connected to an App Clip, the system ensures that an app provides an App Clip before allowing the app to interact with App Clip Codes. Without providing an App Clip, the app can recognize codes in the environment by determining their physical location ([`transform`](aranchor/transform.md)), but code URLs ([`url`](arappclipcodeanchor/url.md)) remain `nil`.

## See Also

- [Interacting with App Clip Codes in AR](../AppClip/interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.
- [class var supportsAppClipCodeTracking: Bool](argeotrackingconfiguration/supportsappclipcodetracking.md)
  A flag that indicates if the device tracks App Clip Codes.
- [class ARAppClipCodeAnchor](arappclipcodeanchor.md)
  An anchor that tracks the position and orientation of an App Clip Code in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration/appclipcodetrackingenabled)*