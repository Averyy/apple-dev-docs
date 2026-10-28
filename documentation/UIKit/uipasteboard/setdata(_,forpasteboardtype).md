# setData(_:forPasteboardType:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setData:(NSData *) data forPasteboardType:(NSString *) pasteboardType;
```

## Discussion

Use this method to put raw data on the pasteboard. For example, you could archive a graph of model objects and pass the resulting [`NSData`](../../Foundation/nsdata.md) object to a related app via a pasteboard using a custom pasteboard type. (To put objects—such as [`NSString`](../../Foundation/nsstring.md), [`NSArray`](../../Foundation/nsarray.md), [`NSDictionary`](../../Foundation/nsdictionary.md), [`NSDate`](../../Foundation/nsdate.md), [`NSNumber`](../../Foundation/nsnumber.md), [`UIImage`](../uiimage.md), or [`NSURL`](../../Foundation/nsurl.md) objects—on the pasteboard, use the [`setValue(_:forPasteboardType:)`](./setvalue%28_,forpasteboardtype%29.md) method.) This method writes data for the first item in the pasteboard. Calling this method replaces any items currently in the pasteboard.

## Parameters

- `data`: The data object to be written to the pasteboard.
- `pasteboardType`: A string identifying the representation type of the pasteboard item. This is typically a UTI.

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
- [func value(forPasteboardType: String) -> Any?](./value%28forpasteboardtype%29.md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](./values%28forpasteboardtype,initemset%29.md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](./setvalue%28_,forpasteboardtype%29.md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/setdata(_:forpasteboardtype:))*