# setItems(_:options:)

**Framework**: UIKit  
**Kind**: method

Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setItems(_ items: [[String : Any]], options: [UIPasteboard.OptionsKey : Any] = [:])
```

## Parameters

- `items`: An array of items to add to the pasteboard.
- `options`: The privacy options to apply to all the items on the pasteboard. The available options are described in  .

## See Also

- [var numberOfItems: Int](uipasteboard/numberofitems.md)
  The number of items for the pasteboard.
- [var items: [[String : Any]]](uipasteboard/items.md)
  The pasteboard items on the pasteboard.
- [func addItems([[String : Any]])](uipasteboard/additems(_:).md)
  Appends pasteboard items to the current contents of the pasteboard.
- [func data(forPasteboardType: String) -> Data?](uipasteboard/data(forpasteboardtype:).md)
  Returns the data on the pasteboard for the given representation type.
- [func data(forPasteboardType: String, inItemSet: IndexSet?) -> [Data]?](uipasteboard/data(forpasteboardtype:initemset:).md)
  Returns the data objects in the indicated pasteboard items that have the given representation type.
- [func setData(Data, forPasteboardType: String)](uipasteboard/setdata(_:forpasteboardtype:).md)
  Puts data on the pasteboard for the specified representation type.
- [func value(forPasteboardType: String) -> Any?](uipasteboard/value(forpasteboardtype:).md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](uipasteboard/values(forpasteboardtype:initemset:).md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](uipasteboard/setvalue(_:forpasteboardtype:).md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/setitems(_:options:))*