# browser(_:setObjectValue:forItem:)

**Framework**: AppKit  
**Kind**: method

Sets the object that the specified item uses to draw its contents to the specified object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func browser(_ browser: NSBrowser, setObjectValue object: Any?, forItem item: Any?)
```

## Parameters

- `browser`: The browser.
- `object`: The object to set.
- `item`: The item whose object is set.

## See Also

- [func browser(NSBrowser, child: Int, ofItem: Any?) -> Any](nsbrowserdelegate/browser(_:child:ofitem:).md)
  Asks the delegate to return the child of the specified item at the specified index.
- [func browser(NSBrowser, isLeafItem: Any?) -> Bool](nsbrowserdelegate/browser(_:isleafitem:).md)
  Asks the delegate whether the specified item is a leaf item (an item that cannot be expanded).
- [func browser(NSBrowser, shouldEditItem: Any?) -> Bool](nsbrowserdelegate/browser(_:shouldedititem:).md)
  Asks the delegate whether the browser may start an editing session for the specified item.
- [func browser(NSBrowser, objectValueForItem: Any?) -> Any?](nsbrowserdelegate/browser(_:objectvalueforitem:).md)
  Returns the object that the specified item uses to draw its contents.
- [func rootItem(for: NSBrowser) -> Any?](nsbrowserdelegate/rootitem(for:).md)
  Asks the delegate to return the root item of the browser.
- [func browser(NSBrowser, previewViewControllerForLeafItem: Any) -> NSViewController?](nsbrowserdelegate/browser(_:previewviewcontrollerforleafitem:).md)
  Asks the delegate for a controller that provides a preview column for the specified leaf item.
- [func browser(NSBrowser, headerViewControllerForItem: Any?) -> NSViewController?](nsbrowserdelegate/browser(_:headerviewcontrollerforitem:).md)
  Asks the delegate for a controller that provides a header view for the specified column item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:setobjectvalue:foritem:))*