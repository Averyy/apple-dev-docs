# addItems(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Appends pasteboard items to the current contents of the pasteboard.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addItems(_ items: [[String : Any]])
```

```objc
- (void) addItems:(NSArray<NSDictionary<NSString *,id> *> *) items;
```

## Parameters

- `items`: An array of dictionaries. Each dictionary represents a pasteboard item, with the key being the representation type and the value being the object associated with that type.

## See Also

### Getting and setting pasteboard items
- [var numberOfItems: Int](./numberofitems.md)
  The number of items for the pasteboard.
- [var items: [[String : Any]]](./items.md)
  The pasteboard items on the pasteboard.
- [func setItems([[String : Any]], options: [UIPasteboard.OptionsKey : Any])](./setitems%28_,options%29.md)
  Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [func data(forPasteboardType: String) -> Data?](./data%28forpasteboardtype%29.md)
  Returns the data on the pasteboard for the given representation type.
- [func data(forPasteboardType: String, inItemSet: IndexSet?) -> [Data]?](./data%28forpasteboardtype,initemset%29.md)
  Returns the data objects in the indicated pasteboard items that have the given representation type.
- [func setData(Data, forPasteboardType: String)](./setdata%28_,forpasteboardtype%29.md)
  Puts data on the pasteboard for the specified representation type.
- [func value(forPasteboardType: String) -> Any?](./value%28forpasteboardtype%29.md)
  Returns an object on the pasteboard for the given representation type.
- [func values(forPasteboardType: String, inItemSet: IndexSet?) -> [Any]?](./values%28forpasteboardtype,initemset%29.md)
  Returns the objects on the indicated pasteboard items that have the given representation type.
- [func setValue(Any, forPasteboardType: String)](./setvalue%28_,forpasteboardtype%29.md)
  Puts an object on the pasteboard for the specified representation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/additems(_:))*