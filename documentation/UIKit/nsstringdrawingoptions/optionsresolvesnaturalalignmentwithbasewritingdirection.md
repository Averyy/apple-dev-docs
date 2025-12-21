# optionsResolvesNaturalAlignmentWithBaseWritingDirection

**Framework**: UIKit  
**Kind**: property

Specifies the behavior for resolving `NSTextAlignment.natural` to the visual alignment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
static var optionsResolvesNaturalAlignmentWithBaseWritingDirection: NSStringDrawingOptions { get }
```

#### Discussion

When set, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingoptions/optionsresolvesnaturalalignmentwithbasewritingdirection)*