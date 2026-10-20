# NSAccessibilityCustomRotorItemSearchDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A delegate for a custom rotor that finds the next item result after performing a search with the specified search parameters.

**Availability**:
- macOS 10.13+

## Declaration

```swift
protocol NSAccessibilityCustomRotorItemSearchDelegate : NSObjectProtocol
```

```objc
@protocol NSAccessibilityCustomRotorItemSearchDelegate <NSObject>
```

## Topics

### Finding the Next Item
- [func rotor(NSAccessibilityCustomRotor, resultFor: NSAccessibilityCustomRotor.SearchParameters) -> NSAccessibilityCustomRotor.ItemResult?](./nsaccessibilitycustomrotoritemsearchdelegate/rotor%28_,resultfor%29.md)
  Performs a search with the specified search parameters and returns the item result.
- [NSAccessibilityCustomRotor.SearchParameters](./nsaccessibilitycustomrotor/searchparameters.md)
  Search parameters for a custom rotor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Navigating to the Next Item
- [var itemSearchDelegate: (any NSAccessibilityCustomRotorItemSearchDelegate)?](./nsaccessibilitycustomrotor/itemsearchdelegate.md)
  The delegate for finding the next item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotoritemsearchdelegate)*