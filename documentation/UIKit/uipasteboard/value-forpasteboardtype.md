# value(forPasteboardType:)

**Framework**: UIKit  
**Kind**: method

Returns an object on the pasteboard for the given representation type.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func value(forPasteboardType pasteboardType: String) -> Any?
```

#### Return Value

An object that is an instance of the appropriate class based on `pasteboardType` or an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing “raw” data.

#### Discussion

This method attempts to return an object that is of a class type appropriate to the representation type, which typically is a UTI. For example, if the representation type is `kUTTypePlainText` (`public.plain-text`), the method returns an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object. If the method can’t determine the class type from the representation type, it returns the object as a generic object, such as an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`UIImage`](uiimage.md), or [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object. This method works on the first item in the pasteboard. If there are other items, it ignores them.

## Parameters

- `pasteboardType`: A string identifying a representation type of a pasteboard item.

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
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](uipasteboard/values(forpasteboardtype:initemset:).md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](uipasteboard/setvalue(_:forpasteboardtype:).md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/value(forpasteboardtype:))*