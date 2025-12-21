# isListenerHeadTrackingEnabled

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the listener orientation is automatically rotated based on head orientation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isListenerHeadTrackingEnabled: Bool { get set }
```

#### Discussion

To enable head tracking, your app must have the [`com.apple.developer.coremotion.head-pose`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.coremotion.head-pose) entitlement.

Set this value to [`true`](https://developer.apple.com/documentation/Swift/true) to enable head tracking with compatible AirPods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/islistenerheadtrackingenabled)*