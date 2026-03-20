# residencySet

**Framework**: MetalKit  
**Kind**: property

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+

## Declaration

```swift
var residencySet: any MTLResidencySet { get }
```

#### Discussion

Get the view’s residency set.

Get the view’s residency set. The residency set contains all MTLTextures created by the view. Applications should use this residency set and the residency set of the view’s underlying CAMetalLayer to ensure all required MTLTextures are resident before use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/residencyset)*