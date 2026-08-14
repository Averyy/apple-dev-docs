# browser(_:isLeafItem:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate whether the specified item is a leaf item (an item that cannot be expanded).

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, isLeafItem item: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified item is a leaf item; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `browser`: The browser.
- `item`: The item to be checked.

## See Also

- [func browser(NSBrowser, child: Int, ofItem: Any?) -> Any](nsbrowserdelegate/browser(_:child:ofitem:).md)
  Asks the delegate to return the child of the specified item at the specified index.
- [func browser(NSBrowser, shouldEditItem: Any?) -> Bool](nsbrowserdelegate/browser(_:shouldedititem:).md)
  Asks the delegate whether the browser may start an editing session for the specified item.
- [func browser(NSBrowser, objectValueForItem: Any?) -> Any?](nsbrowserdelegate/browser(_:objectvalueforitem:).md)
  Returns the object that the specified item uses to draw its contents.
- [func browser(NSBrowser, setObjectValue: Any?, forItem: Any?)](nsbrowserdelegate/browser(_:setobjectvalue:foritem:).md)
  Sets the object that the specified item uses to draw its contents to the specified object.
- [func rootItem(for: NSBrowser) -> Any?](nsbrowserdelegate/rootitem(for:).md)
  Asks the delegate to return the root item of the browser.
- [func browser(NSBrowser, previewViewControllerForLeafItem: Any) -> NSViewController?](nsbrowserdelegate/browser(_:previewviewcontrollerforleafitem:).md)
  Asks the delegate for a controller that provides a preview column for the specified leaf item.
- [func browser(NSBrowser, headerViewControllerForItem: Any?) -> NSViewController?](nsbrowserdelegate/browser(_:headerviewcontrollerforitem:).md)
  Asks the delegate for a controller that provides a header view for the specified column item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:isleafitem:))*