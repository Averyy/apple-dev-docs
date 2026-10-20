# rootItem(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to return the root item of the browser.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func rootItem(for browser: NSBrowser) -> Any?
```

```objc
- (id) rootItemForBrowser:(NSBrowser *) browser;
```

#### Return Value

The browser’s root item.

#### Discussion

By default, `nil` identifies the root item. This method can specify a different root item. To reload the previously set root item, call [`loadColumnZero()`](../nsbrowser/loadcolumnzero%28%29.md), and [`rootItem(for:)`](./rootitem%28for%29.md) will be called again.

## Parameters

- `browser`: The browser.

## See Also

### Accessing Components
- [func browser(NSBrowser, child: Int, ofItem: Any?) -> Any](./browser%28_,child,ofitem%29.md)
  Asks the delegate to return the child of the specified item at the specified index.
- [func browser(NSBrowser, isLeafItem: Any?) -> Bool](./browser%28_,isleafitem%29.md)
  Asks the delegate whether the specified item is a leaf item (an item that cannot be expanded).
- [func browser(NSBrowser, shouldEditItem: Any?) -> Bool](./browser%28_,shouldedititem%29.md)
  Asks the delegate whether the browser may start an editing session for the specified item.
- [func browser(NSBrowser, objectValueForItem: Any?) -> Any?](./browser%28_,objectvalueforitem%29.md)
  Returns the object that the specified item uses to draw its contents.
- [func browser(NSBrowser, setObjectValue: Any?, forItem: Any?)](./browser%28_,setobjectvalue,foritem%29.md)
  Sets the object that the specified item uses to draw its contents to the specified object.
- [func browser(NSBrowser, previewViewControllerForLeafItem: Any) -> NSViewController?](./browser%28_,previewviewcontrollerforleafitem%29.md)
  Asks the delegate for a controller that provides a preview column for the specified leaf item.
- [func browser(NSBrowser, headerViewControllerForItem: Any?) -> NSViewController?](./browser%28_,headerviewcontrollerforitem%29.md)
  Asks the delegate for a controller that provides a header view for the specified column item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/rootitem(for:))*