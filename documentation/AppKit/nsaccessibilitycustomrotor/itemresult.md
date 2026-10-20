# NSAccessibilityCustomRotor.ItemResult

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A target accessibility element that a custom rotor references.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class ItemResult
```

```objc
@interface NSAccessibilityCustomRotorItemResult : NSObject
```

## Topics

### Creating an Item Result
- [init(targetElement: any NSAccessibilityElementProtocol)](./itemresult/init%28targetelement%29.md)
  Creates an item result with the specified target element.
- [init(itemLoadingToken: NSAccessibilityLoadingToken, customLabel: String)](./itemresult/init%28itemloadingtoken,customlabel%29.md)
  Creates an item result with the specified item load token and custom label.
### Identifying an Item Result
- [var targetElement: (any NSAccessibilityElementProtocol)?](./itemresult/targetelement.md)
  A target element that references an element to message for accessibility properties.
- [var itemLoadingToken: NSAccessibilityLoadingToken?](./itemresult/itemloadingtoken.md)
  A token to determine which item to return.
- [var targetRange: NSRange](./itemresult/targetrange.md)
  A range that specifies the area of interest for text-based elements.
- [var customLabel: String?](./itemresult/customlabel.md)
  A localized label to use instead of the default item label to describe the item result.

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

### Managing the Current Item
- [var currentItem: NSAccessibilityCustomRotor.ItemResult?](./searchparameters/currentitem.md)
  The current item that determines where the search starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/itemresult)*