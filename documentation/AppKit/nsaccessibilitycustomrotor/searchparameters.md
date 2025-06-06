# NSAccessibilityCustomRotor.SearchParameters

**Framework**: AppKit  
**Kind**: class

Search parameters for a custom rotor.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class SearchParameters
```

#### Overview

Use these parameters to determine the next matching [`NSAccessibilityCustomRotor.ItemResult`](nsaccessibilitycustomrotor/itemresult.md).

## Topics

### Managing the Current Item
- [var currentItem: NSAccessibilityCustomRotor.ItemResult?](nsaccessibilitycustomrotor/searchparameters/currentitem.md)
  The current item that determines where the search starts.
- [NSAccessibilityCustomRotor.ItemResult](nsaccessibilitycustomrotor/itemresult.md)
  A target accessibility element that a custom rotor references.
### Specifying the Filter String
- [var filterString: String](nsaccessibilitycustomrotor/searchparameters/filterstring.md)
  A string of text to filter the results against.
### Specifying Search Direction
- [var searchDirection: NSAccessibilityCustomRotor.SearchDirection](nsaccessibilitycustomrotor/searchparameters/searchdirection.md)
  The direction to search for an item result.
- [NSAccessibilityCustomRotor.SearchDirection](nsaccessibilitycustomrotor/searchdirection.md)
  Constants that describe the direction to search for an item result.

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

- [func rotor(NSAccessibilityCustomRotor, resultFor: NSAccessibilityCustomRotor.SearchParameters) -> NSAccessibilityCustomRotor.ItemResult?](nsaccessibilitycustomrotoritemsearchdelegate/rotor(_:resultfor:).md)
  Performs a search with the specified search parameters and returns the item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/searchparameters)*