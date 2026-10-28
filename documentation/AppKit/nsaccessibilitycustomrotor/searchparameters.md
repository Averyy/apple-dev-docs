# NSAccessibilityCustomRotor.SearchParameters

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

Search parameters for a custom rotor.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class SearchParameters
```

```objc
@interface NSAccessibilityCustomRotorSearchParameters : NSObject
```

## Overview

Use these parameters to determine the next matching [`NSAccessibilityCustomRotor.ItemResult`](./itemresult.md).

## Topics

### Managing the Current Item
- [var currentItem: NSAccessibilityCustomRotor.ItemResult?](./searchparameters/currentitem.md)
  The current item that determines where the search starts.
- [NSAccessibilityCustomRotor.ItemResult](./itemresult.md)
  A target accessibility element that a custom rotor references.
### Specifying the Filter String
- [var filterString: String](./searchparameters/filterstring.md)
  A string of text to filter the results against.
### Specifying Search Direction
- [var searchDirection: NSAccessibilityCustomRotor.SearchDirection](./searchparameters/searchdirection.md)
  The direction to search for an item result.
- [NSAccessibilityCustomRotor.SearchDirection](./searchdirection.md)
  Constants that describe the direction to search for an item result.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Finding the Next Item
- [func rotor(NSAccessibilityCustomRotor, resultFor: NSAccessibilityCustomRotor.SearchParameters) -> NSAccessibilityCustomRotor.ItemResult?](../nsaccessibilitycustomrotoritemsearchdelegate/rotor%28_,resultfor%29.md)
  Performs a search with the specified search parameters and returns the item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/searchparameters)*