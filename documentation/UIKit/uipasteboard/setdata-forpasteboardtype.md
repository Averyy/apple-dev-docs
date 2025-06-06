# setData(_:forPasteboardType:)

**Framework**: UIKit  
**Kind**: method

Puts data on the pasteboard for the specified representation type.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setData(_ data: Data, forPasteboardType pasteboardType: String)
```

#### Discussion

Use this method to put raw data on the pasteboard. For example, you could archive a graph of model objects and pass the resulting [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object to a related app via a pasteboard using a custom pasteboard type. (To put objects—such as [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`UIImage`](uiimage.md), or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects—on the pasteboard, use the [`setValue(_:forPasteboardType:)`](uipasteboard/setvalue(_:forpasteboardtype:).md) method.) This method writes data for the first item in the pasteboard. Calling this method replaces any items currently in the pasteboard.

## Parameters

- `data`: The data object to be written to the pasteboard.
- `pasteboardType`: A string identifying the representation type of the pasteboard item. This is typically a UTI.

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
- [func data(forPasteboardType: String, inItemSet: IndexSet?) -> [Data]?](uipasteboard/data(forpasteboardtype:initemset:).md)
  Returns the data objects in the indicated pasteboard items that have the given representation type.
- [func value(forPasteboardType: String) -> Any?](uipasteboard/value(forpasteboardtype:).md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](uipasteboard/values(forpasteboardtype:initemset:).md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](uipasteboard/setvalue(_:forpasteboardtype:).md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/setdata(_:forpasteboardtype:))*