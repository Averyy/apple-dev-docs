# browser(_:shouldEditItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the browser may start an editing session for the specified item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, shouldEditItem item: Any?) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) browser shouldEditItem:(id) item;
```

## Return Value

[`true`](../../Swift/true.md) to allow the editing session to begin; [`false`](../../Swift/false.md) to disallow it.

## Parameters

- `browser`: The browser.
- `item`: The item to edit.

## See Also

### Accessing Components
- [func browser(NSBrowser, child: Int, ofItem: Any?) -> Any](./browser%28_,child,ofitem%29.md)
  Asks the delegate to return the child of the specified item at the specified index.
- [func browser(NSBrowser, isLeafItem: Any?) -> Bool](./browser%28_,isleafitem%29.md)
  Asks the delegate whether the specified item is a leaf item (an item that cannot be expanded).
- [func browser(NSBrowser, objectValueForItem: Any?) -> Any?](./browser%28_,objectvalueforitem%29.md)
  Returns the object that the specified item uses to draw its contents.
- [func browser(NSBrowser, setObjectValue: Any?, forItem: Any?)](./browser%28_,setobjectvalue,foritem%29.md)
  Sets the object that the specified item uses to draw its contents to the specified object.
- [func rootItem(for: NSBrowser) -> Any?](./rootitem%28for%29.md)
  Asks the delegate to return the root item of the browser.
- [func browser(NSBrowser, previewViewControllerForLeafItem: Any) -> NSViewController?](./browser%28_,previewviewcontrollerforleafitem%29.md)
  Asks the delegate for a controller that provides a preview column for the specified leaf item.
- [func browser(NSBrowser, headerViewControllerForItem: Any?) -> NSViewController?](./browser%28_,headerviewcontrollerforitem%29.md)
  Asks the delegate for a controller that provides a header view for the specified column item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:shouldedititem:))*