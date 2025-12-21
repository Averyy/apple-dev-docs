# resolvesNaturalAlignmentWithBaseWritingDirection

**Framework**: UIKit  
**Kind**: property

Specifies the behavior for resolving `NSTextAlignment.natural` to the visual alignment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var resolvesNaturalAlignmentWithBaseWritingDirection: Bool { get set }
```

#### Discussion

When set to `true`, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language. The default value is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/resolvesnaturalalignmentwithbasewritingdirection)*