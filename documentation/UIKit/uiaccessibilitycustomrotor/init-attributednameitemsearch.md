# init(attributedName:itemSearch:)

**Framework**: UIKit  
**Kind**: init

Creates a rotor with the specified name and search block.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(attributedName: NSAttributedString, itemSearch itemSearchBlock: @escaping UIAccessibilityCustomRotor.Search)
```

#### Return Value

An initialized rotor object.

## Parameters

- `attributedName`: The name of the rotor.
- `itemSearchBlock`: The block that provides the next or previous rotor.

## See Also

- [init(name: String, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(name:itemsearch:).md)
  Creates a rotor with the specified name and search block.
- [init(systemType: UIAccessibilityCustomRotor.SystemRotorType, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(systemtype:itemsearch:).md)
  Creates a rotor for the specified type of item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/init(attributedname:itemsearch:))*