# residencySet

**Framework**: MetalKit  
**Kind**: property

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
var residencySet: any MTLResidencySet { get }
```

#### Discussion

Get the view’s residency set.

Get the view’s residency set. The residency set contains all MTLTextures created by the view. Applications should use this residency set and the residency set of the view’s underlying CAMetalLayer to ensure all required MTLTextures are resident before use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/residencyset)*