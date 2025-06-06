# UIAccessibilityCustomRotor

**Framework**: UIKit  
**Kind**: class

A context-sensitive function that helps VoiceOver users find the next instance of a related element.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAccessibilityCustomRotor
```

#### Overview

You might use an instance of this class to find the next link in an article, or the next misspelled word in a document.

> **Note**:  Session 10116: [`VoiceOver Efficiency with Custom Rotors`](https://developer.apple.comhttps://developer.apple.com/wwdc20/10116)

 Session 10116: [`VoiceOver Efficiency with Custom Rotors`](https://developer.apple.comhttps://developer.apple.com/wwdc20/10116)

## Topics

### Creating a rotor object
- [init(attributedName: NSAttributedString, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(attributedname:itemsearch:).md)
  Creates a rotor with the specified name and search block.
- [init(name: String, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(name:itemsearch:).md)
  Creates a rotor with the specified name and search block.
- [init(systemType: UIAccessibilityCustomRotor.SystemRotorType, itemSearch: UIAccessibilityCustomRotor.Search)](uiaccessibilitycustomrotor/init(systemtype:itemsearch:).md)
  Creates a rotor for the specified type of item.
### Navigating to the next item
- [var itemSearchBlock: UIAccessibilityCustomRotor.Search](uiaccessibilitycustomrotor/itemsearchblock.md)
  The block for retrieving the next or previous rotor.
- [UIAccessibilityCustomRotor.Search](uiaccessibilitycustomrotor/search.md)
  The block type for retrieving the next or previous rotor.
- [UIAccessibilityCustomRotor.Direction](uiaccessibilitycustomrotor/direction.md)
  Constants that indicate the search direction.
### Getting the rotor type
- [var systemRotorType: UIAccessibilityCustomRotor.SystemRotorType](uiaccessibilitycustomrotor/systemrotortype-swift.property.md)
  The type of content that the rotor searches.
- [UIAccessibilityCustomRotor.SystemRotorType](uiaccessibilitycustomrotor/systemrotortype-swift.enum.md)
  Constants that indicate the type of content that the rotor represents.
### Identifying the rotor
- [var name: String](uiaccessibilitycustomrotor/name.md)
  The name of the rotor.
- [var attributedName: NSAttributedString](uiaccessibilitycustomrotor/attributedname.md)
  The name of the rotor as an attributed string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIAccessibilityCustomRotorItemResult](uiaccessibilitycustomrotoritemresult.md)
  A target element that a custom rotor references.
- [class UIAccessibilityCustomRotorSearchPredicate](uiaccessibilitycustomrotorsearchpredicate.md)
  The search parameters that help determine the next matching custom rotor item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor)*