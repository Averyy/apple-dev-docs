# init(name:itemSearch:)

**Framework**: UIKit  
**Kind**: init

Creates a rotor with the specified name and search block.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(name: String, itemSearch itemSearchBlock: @escaping UIAccessibilityCustomRotor.Search)
```

#### Return Value

An initialized rotor object.

## Parameters

- `name`: The name of the rotor.
- `itemSearchBlock`: The block that provides the next or previous rotor.

## See Also

- [init(attributedName: NSAttributedString, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(attributedname:itemsearch:).md)
  Creates a rotor with the specified name and search block.
- [init(systemType: UIAccessibilityCustomRotor.SystemRotorType, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(systemtype:itemsearch:).md)
  Creates a rotor for the specified type of item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/init(name:itemsearch:))*