# isObjectMaskingEnabled

**Framework**: RealityKit  
**Kind**: property

A Boolean value that indicates whether the session uses object masks.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var isObjectMaskingEnabled: Bool
```

#### Discussion

If this value is true, but the samples don’t contain object masks, RealityKit attempts to automatically create a mask algorithmically. If it’s unable to create a mask, RealityKit reverts to reconstructing the object using the entire image.

If this value is true and the request’s samples do include object masks, RealityKit uses the provided masks to separate the foreground object from the background.

If this value is false, RealityKit doesn’t attempt to separate the sample foreground from the background, even if the samples have object masks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/isobjectmaskingenabled)*