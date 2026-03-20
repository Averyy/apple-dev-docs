# bodyVariants

**Framework**: CarPlay  
**Kind**: property

An optional array of strings, ordered from most to least preferred.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var bodyVariants: [NSAttributedString] { get set }
```

#### Discussion

The variant strings should be provided as localized, displayable content. The system will select the first variant that fits the available space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/bodyvariants)*