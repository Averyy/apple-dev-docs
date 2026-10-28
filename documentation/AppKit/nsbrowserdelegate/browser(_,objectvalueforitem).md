# browser(_:objectValueForItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the object that the specified item uses to draw its contents.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, objectValueForItem item: Any?) -> Any?
```

```objc
- (id) browser:(NSBrowser *) browser objectValueForItem:(id) item;
```

## Return Value

The item’s object.

## Parameters

- `browser`: The browser.
- `item`: The item in question.

## See Also

### Accessing Components
- [func browser(NSBrowser, child: Int, ofItem: Any?) -> Any](./browser%28_,child,ofitem%29.md)
  Asks the delegate to return the child of the specified item at the specified index.
- [func browser(NSBrowser, isLeafItem: Any?) -> Bool](./browser%28_,isleafitem%29.md)
  Asks the delegate whether the specified item is a leaf item (an item that cannot be expanded).
- [func browser(NSBrowser, shouldEditItem: Any?) -> Bool](./browser%28_,shouldedititem%29.md)
  Asks the delegate whether the browser may start an editing session for the specified item.
- [func browser(NSBrowser, setObjectValue: Any?, forItem: Any?)](./browser%28_,setobjectvalue,foritem%29.md)
  Sets the object that the specified item uses to draw its contents to the specified object.
- [func rootItem(for: NSBrowser) -> Any?](./rootitem%28for%29.md)
  Asks the delegate to return the root item of the browser.
- [func browser(NSBrowser, previewViewControllerForLeafItem: Any) -> NSViewController?](./browser%28_,previewviewcontrollerforleafitem%29.md)
  Asks the delegate for a controller that provides a preview column for the specified leaf item.
- [func browser(NSBrowser, headerViewControllerForItem: Any?) -> NSViewController?](./browser%28_,headerviewcontrollerforitem%29.md)
  Asks the delegate for a controller that provides a header view for the specified column item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:objectvalueforitem:))*