# wantsAdaptiveBackgroundStyle

**Framework**: CarPlay  
**Kind**: property

A Boolean value that determines whether to use a custom background style.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var wantsAdaptiveBackgroundStyle: Bool { get set }
```

#### Discussion

When set to YES, the header will use a custom background style derived from the thumbnail image. This creates an adaptive background that automatically generates light and dark mode variants.

When set to NO (default), the header uses the standard CarPlay background.

The custom background style uses perceptually-aware color transformation to create visually harmonious backgrounds that adapt to the user’s interface style preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/wantsadaptivebackgroundstyle)*