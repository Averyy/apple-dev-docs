# data(forPasteboardType:inItemSet:)

**Framework**: UIKit  
**Kind**: method

Returns the data objects in the indicated pasteboard items that have the given representation type.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func data(forPasteboardType pasteboardType: String, inItemSet itemSet: IndexSet?) -> [Data]?
```

#### Return Value

An array of [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) objects or, if a requested pasteboard item has no data of the the type indicated by `pasteboardType`, a [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) object.

## Parameters

- `pasteboardType`: A string identifying a representation type. Typically this is a UTI.
- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in   to request all pasteboard items.

## See Also

- [var numberOfItems: Int](uipasteboard/numberofitems.md)
  The number of items for the pasteboard.
- [var items: [[String : Any]]](uipasteboard/items.md)
  The pasteboard items on the pasteboard.
- [func addItems([[String : Any]])](uipasteboard/additems(_:).md)
  Appends pasteboard items to the current contents of the pasteboard.
- [func setItems([[String : Any]], options: [UIPasteboard.OptionsKey : Any])](uipasteboard/setitems(_:options:).md)
  Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [func data(forPasteboardType: String) -> Data?](uipasteboard/data(forpasteboardtype:).md)
  Returns the data on the pasteboard for the given representation type.
- [func setData(Data, forPasteboardType: String)](uipasteboard/setdata(_:forpasteboardtype:).md)
  Puts data on the pasteboard for the specified representation type.
- [func value(forPasteboardType: String) -> Any?](uipasteboard/value(forpasteboardtype:).md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](uipasteboard/values(forpasteboardtype:initemset:).md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](uipasteboard/setvalue(_:forpasteboardtype:).md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/data(forpasteboardtype:initemset:))*