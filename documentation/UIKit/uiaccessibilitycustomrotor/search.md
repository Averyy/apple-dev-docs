# UIAccessibilityCustomRotor.Search

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The block type for retrieving the next or previous rotor.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
typealias Search = (UIAccessibilityCustomRotorSearchPredicate) -> UIAccessibilityCustomRotorItemResult?
```

```c
typedef UIAccessibilityCustomRotorItemResult *(^)(UIAccessibilityCustomRotorSearchPredicate *) UIAccessibilityCustomRotorSearch;
```

## See Also

### Navigating to the next item
- [var itemSearchBlock: UIAccessibilityCustomRotor.Search](./itemsearchblock.md)
  The block for retrieving the next or previous rotor.
- [UIAccessibilityCustomRotor.Direction](./direction.md)
  Constants that indicate the search direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/search)*