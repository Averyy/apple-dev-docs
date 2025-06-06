# NSAccessibilityCustomRotor.ItemResult

**Framework**: AppKit  
**Kind**: class

A target accessibility element that a custom rotor references.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class ItemResult
```

## Topics

### Creating an Item Result
- [init(targetElement: any NSAccessibilityElementProtocol)](nsaccessibilitycustomrotor/itemresult/init(targetelement:).md)
  Creates an item result with the specified target element.
- [init(itemLoadingToken: NSAccessibilityLoadingToken, customLabel: String)](nsaccessibilitycustomrotor/itemresult/init(itemloadingtoken:customlabel:).md)
  Creates an item result with the specified item load token and custom label.
### Identifying an Item Result
- [var targetElement: (any NSAccessibilityElementProtocol)?](nsaccessibilitycustomrotor/itemresult/targetelement.md)
  A target element that references an element to message for accessibility properties.
- [var itemLoadingToken: NSAccessibilityLoadingToken?](nsaccessibilitycustomrotor/itemresult/itemloadingtoken.md)
  A token to determine which item to return.
- [var targetRange: NSRange](nsaccessibilitycustomrotor/itemresult/targetrange.md)
  A range that specifies the area of interest for text-based elements.
- [var customLabel: String?](nsaccessibilitycustomrotor/itemresult/customlabel.md)
  A localized label to use instead of the default item label to describe the item result.

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

- [var currentItem: NSAccessibilityCustomRotor.ItemResult?](nsaccessibilitycustomrotor/searchparameters/currentitem.md)
  The current item that determines where the search starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/itemresult)*