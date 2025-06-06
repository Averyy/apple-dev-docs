# itemSearchBlock

**Framework**: UIKit  
**Kind**: property

The block for retrieving the next or previous rotor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var itemSearchBlock: UIAccessibilityCustomRotor.Search { get set }
```

#### Discussion

Your implementation of the block facilitates navigation from the current rotor to the next or previous rotor.

## See Also

- [UIAccessibilityCustomRotor.Search](uiaccessibilitycustomrotor/search.md)
  The block type for retrieving the next or previous rotor.
- [UIAccessibilityCustomRotor.Direction](uiaccessibilitycustomrotor/direction.md)
  Constants that indicate the search direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/itemsearchblock)*