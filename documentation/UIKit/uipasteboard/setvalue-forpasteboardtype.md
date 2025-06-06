# setValue(_:forPasteboardType:)

**Framework**: UIKit  
**Kind**: method

Puts an object on the pasteboard for the specified representation type.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: Any, forPasteboardType pasteboardType: String)
```

#### Discussion

Use this method to put an object—such as an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`UIImage`](uiimage.md), or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object—on the pasteboard. (For images, you can also use the [`image`](uipasteboard/image.md) or [`images`](uipasteboard/images.md) properties; for all other data, such as raw binary data, use the [`setData(_:forPasteboardType:)`](uipasteboard/setdata(_:forpasteboardtype:).md) method.) This method writes the object as the first item in the pasteboard. Calling this method replaces any items currently in the pasteboard.

## Parameters

- `value`: The object to be written to the pasteboard.
- `pasteboardType`: A string identifying the representation type of the pasteboard item. If the type is a UTI, it must be compatible with the class of  ; otherwise, nothing is written to the pasteboard.

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
- [func setData(Data, forPasteboardType: String)](uipasteboard/setdata(_:forpasteboardtype:).md)
  Puts data on the pasteboard for the specified representation type.
- [func value(forPasteboardType: String) -> Any?](uipasteboard/value(forpasteboardtype:).md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](uipasteboard/values(forpasteboardtype:initemset:).md)
  Returns the objects on the indicated pasteboard items that have the given representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/setvalue(_:forpasteboardtype:))*