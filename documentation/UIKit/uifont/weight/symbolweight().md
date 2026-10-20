# symbolWeight()

**Framework**: UIKit  
**Kind**: method

Provides the corresponding symbol weight for this font weight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func symbolWeight() -> UIImage.SymbolWeight
```

#### Return Value

The [`UIImage.SymbolWeight`](uiimage/symbolweight.md) that most closely coordinates with the provided font weight.

#### Discussion

When placing symbols adjacent to text, use this method to find the appropriate symbol weight to match the weight of the text. Similarly, if you want to display a symbol with a particular weight, you can use [`fontWeight()`](uiimage/symbolweight/fontweight().md) to look up the matching font weight for adjacent text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/weight/symbolweight())*