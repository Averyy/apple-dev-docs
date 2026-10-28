# resolvesNaturalAlignmentWithBaseWritingDirection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Specifies the behavior for resolving [`NSTextAlignment.natural`](../nstextalignment/natural.md) to the visual alignment.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var resolvesNaturalAlignmentWithBaseWritingDirection: Bool { get set }
```

```objc
@property BOOL resolvesNaturalAlignmentWithBaseWritingDirection;
```

## Discussion

When set to `true`, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language. The default value is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/resolvesnaturalalignmentwithbasewritingdirection)*