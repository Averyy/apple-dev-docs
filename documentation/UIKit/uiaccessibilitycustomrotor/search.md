# UIAccessibilityCustomRotor.Search

**Framework**: UIKit  
**Kind**: typealias

The block type for retrieving the next or previous rotor.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
typealias Search = (UIAccessibilityCustomRotorSearchPredicate) -> UIAccessibilityCustomRotorItemResult?
```

## See Also

- [var itemSearchBlock: UIAccessibilityCustomRotor.Search](uiaccessibilitycustomrotor/itemsearchblock.md)
  The block for retrieving the next or previous rotor.
- [UIAccessibilityCustomRotor.Direction](uiaccessibilitycustomrotor/direction.md)
  Constants that indicate the search direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/search)*