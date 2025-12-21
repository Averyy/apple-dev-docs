# supportsAppClipCodeTracking

**Framework**: ARKit  
**Kind**: property

A flag that indicates if the device tracks App Clip Codes.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+

## Declaration

```swift
class var supportsAppClipCodeTracking: Bool { get }
```

#### Discussion

Devices require the Apple Neural Engine (ANE) to track App Clip Codes. The system sets this property to [`true`](https://developer.apple.com/documentation/Swift/true) if the device contains the ANE chip. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

Call this function before setting [`appClipCodeTrackingEnabled`](arworldtrackingconfiguration/appclipcodetrackingenabled.md).

## See Also

- [Interacting with App Clip Codes in AR](../AppClip/interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.
- [var appClipCodeTrackingEnabled: Bool](argeotrackingconfiguration/appclipcodetrackingenabled.md)
  A Boolean value that indicates if the framework searches the physical environment for App Clip Codes.
- [class ARAppClipCodeAnchor](arappclipcodeanchor.md)
  An anchor that tracks the position and orientation of an App Clip Code in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration/supportsappclipcodetracking)*