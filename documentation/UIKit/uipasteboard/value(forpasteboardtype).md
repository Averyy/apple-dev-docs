# value(forPasteboardType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id) valueForPasteboardType:(NSString *) pasteboardType;
```

## Return Value

An object that is an instance of the appropriate class based on `pasteboardType` or an [`NSData`](../../Foundation/nsdata.md) object containing “raw” data.

## Discussion

This method attempts to return an object that is of a class type appropriate to the representation type, which typically is a UTI. For example, if the representation type is `kUTTypePlainText` (`public.plain-text`), the method returns an [`NSString`](../../Foundation/nsstring.md) object. If the method can’t determine the class type from the representation type, it returns the object as a generic object, such as an [`NSString`](../../Foundation/nsstring.md), [`NSArray`](../../Foundation/nsarray.md), [`NSDictionary`](../../Foundation/nsdictionary.md), [`NSDate`](../../Foundation/nsdate.md), [`NSNumber`](../../Foundation/nsnumber.md), [`NSURL`](../../Foundation/nsurl.md), [`UIImage`](../uiimage.md), or [`NSData`](../../Foundation/nsdata.md) object. This method works on the first item in the pasteboard. If there are other items, it ignores them.

## Parameters

- `pasteboardType`: A string identifying a representation type of a pasteboard item.

## See Also

### Getting and setting pasteboard items
- [var numberOfItems: Int](./numberofitems.md)
  The number of items for the pasteboard.
- [var items: [[String : Any]]](./items.md)
  The pasteboard items on the pasteboard.
- [func addItems([[String : Any]])](./additems%28_%29.md)
  Appends pasteboard items to the current contents of the pasteboard.
- [func setItems([[String : Any]], options: [UIPasteboard.OptionsKey : Any])](./setitems%28_,options%29.md)
  Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [func data(forPasteboardType: String) -> Data?](./data%28forpasteboardtype%29.md)
  Returns the data on the pasteboard for the given representation type.
- [func data(forPasteboardType: String, inItemSet: IndexSet?) -> [Data]?](./data%28forpasteboardtype,initemset%29.md)
  Returns the data objects in the indicated pasteboard items that have the given representation type.
- [func setData(Data, forPasteboardType: String)](./setdata%28_,forpasteboardtype%29.md)
  Puts data on the pasteboard for the specified representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](./values%28forpasteboardtype,initemset%29.md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](./setvalue%28_,forpasteboardtype%29.md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/value(forpasteboardtype:))*