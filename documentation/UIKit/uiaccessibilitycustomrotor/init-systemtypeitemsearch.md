# init(systemType:itemSearch:)

**Framework**: UIKit  
**Kind**: init

Creates a rotor for the specified type of item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(systemType type: UIAccessibilityCustomRotor.SystemRotorType, itemSearch itemSearchBlock: @escaping UIAccessibilityCustomRotor.Search)
```

#### Return Value

An initialized rotor object.

## Parameters

- `type`: The type of content navigated by the rotor. For a list of possible values, see  .
- `itemSearchBlock`: The block that provides the next or previous rotor for the given type.

## See Also

- [init(attributedName: NSAttributedString, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(attributedname:itemsearch:).md)
  Creates a rotor with the specified name and search block.
- [init(name: String, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(name:itemsearch:).md)
  Creates a rotor with the specified name and search block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/init(systemtype:itemsearch:))*