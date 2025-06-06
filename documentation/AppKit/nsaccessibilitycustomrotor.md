# NSAccessibilityCustomRotor

**Framework**: AppKit  
**Kind**: class

A context-sensitive function that helps VoiceOver users find the next instance of a related accessibility element.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class NSAccessibilityCustomRotor
```

#### Overview

Assistive apps, like VoiceOver, provide interfaces to quickly search apps for content of a specific type. For example, in a web browser, a user can quickly explore a list of navigational links or buttons using VoiceOver’s content menus.

[`NSAccessibilityCustomRotor`](nsaccessibilitycustomrotor.md) provides a way for apps to vend their own content menus. For example, Pages can create a  custom rotor that allows assistive apps to search the Pages document for all headings.

## Topics

### Creating a Rotor
- [init(label: String, itemSearchDelegate: any NSAccessibilityCustomRotorItemSearchDelegate)](nsaccessibilitycustomrotor/init(label:itemsearchdelegate:).md)
  Creates a custom rotor with the specified label and item search delegate.
- [init(rotorType: NSAccessibilityCustomRotor.RotorType, itemSearchDelegate: any NSAccessibilityCustomRotorItemSearchDelegate)](nsaccessibilitycustomrotor/init(rotortype:itemsearchdelegate:).md)
  Creates a custom rotor with the specified rotor type and item search delegate.
### Navigating to the Next Item
- [var itemSearchDelegate: (any NSAccessibilityCustomRotorItemSearchDelegate)?](nsaccessibilitycustomrotor/itemsearchdelegate.md)
  The delegate for finding the next item result.
- [protocol NSAccessibilityCustomRotorItemSearchDelegate](nsaccessibilitycustomrotoritemsearchdelegate.md)
  A delegate for a custom rotor that finds the next item result after performing a search with the specified search parameters.
### Loading the Item
- [var itemLoadingDelegate: (any NSAccessibilityElementLoading)?](nsaccessibilitycustomrotor/itemloadingdelegate.md)
  The delegate for loading item results that don’t have a backing UI element at loading time.
- [protocol NSAccessibilityElementLoading](nsaccessibilityelementloading.md)
  A role-based protocol that declares the minimum interface necessary for an accessibility element to support loading.
### Getting the Rotor Type
- [var type: NSAccessibilityCustomRotor.RotorType](nsaccessibilitycustomrotor/type.md)
  The type of content that the rotor represents.
- [NSAccessibilityCustomRotor.RotorType](nsaccessibilitycustomrotor/rotortype.md)
  Constants that indicate the type of content that the rotor represents.
### Identifying the Rotor
- [var label: String](nsaccessibilitycustomrotor/label.md)
  The localized label that assistive apps use to describe the custom rotor.

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

## See Also

- [func accessibilityCustomRotors() -> [NSAccessibilityCustomRotor]](nsaccessibilityprotocol/accessibilitycustomrotors.md)
  Returns the custom rotors of the current accessibility element.
- [func setAccessibilityCustomRotors([NSAccessibilityCustomRotor])](nsaccessibilityprotocol/setaccessibilitycustomrotors(_:).md)
  Sets the custom rotors of the current accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor)*