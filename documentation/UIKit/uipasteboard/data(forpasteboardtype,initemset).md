# data(forPasteboardType:inItemSet:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<NSData *> *) dataForPasteboardType:(NSString *) pasteboardType inItemSet:(NSIndexSet *) itemSet;
```

## Return Value

An array of [`NSData`](../../Foundation/nsdata.md) objects or, if a requested pasteboard item has no data of the the type indicated by `pasteboardType`, a [`NSNull`](../../Foundation/nsnull.md) object.

## Parameters

- `pasteboardType`: A string identifying a representation type. Typically this is a UTI.
- `itemSet`: An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in `nil` to request all pasteboard items.

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
- [func setData(Data, forPasteboardType: String)](./setdata%28_,forpasteboardtype%29.md)
  Puts data on the pasteboard for the specified representation type.
- [func value(forPasteboardType: String) -> Any?](./value%28forpasteboardtype%29.md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](./values%28forpasteboardtype,initemset%29.md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](./setvalue%28_,forpasteboardtype%29.md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/data(forpasteboardtype:initemset:))*