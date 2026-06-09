# resolvesNaturalAlignmentWithBaseWritingDirection

**Framework**: AppKit  
**Kind**: property

Specifies the behavior for resolving [`NSTextAlignment.natural`](nstextalignment/natural.md) to the visual alignment.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var resolvesNaturalAlignmentWithBaseWritingDirection: Bool { get set }
```

#### Discussion

When set to `true`, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language. The default value is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/resolvesnaturalalignmentwithbasewritingdirection)*