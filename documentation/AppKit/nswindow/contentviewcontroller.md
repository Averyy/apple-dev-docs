# contentViewController

**Framework**: AppKit  
**Kind**: property

The main content view controller for the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var contentViewController: NSViewController? { get set }
```

#### Discussion

The value of this property provides the content view of the window. Setting this value removes the existing value of [`contentView`](nswindow/contentview.md) and makes the `contentViewController.view` the main content view for the window. By default, the value of this property is `nil`.

The content view controller controls only the [`contentView`](nswindow/contentview.md) object, and not the title of the window. The window title can easily be bound to the [`contentViewController`](nswindow/contentviewcontroller.md) object using code such as: `[window bind:NSTitleBinding toObject:contentViewController withKeyPath:@"title" options:nil]`. Setting [`contentViewController`](nswindow/contentviewcontroller.md) causes the window to resize based on the current size of the [`contentViewController`](nswindow/contentviewcontroller.md); to restrict the size of the window, use Auto Layout (note that the value of this property is encoded in the NIB). Directly assigning a [`contentView`](nswindow/contentview.md) value clears out the root view controller.

## See Also

- [convenience init(contentViewController: NSViewController)](nswindow/init(contentviewcontroller:).md)
  Creates a titled window that contains the specified content view controller.
- [var contentView: NSView?](nswindow/contentview.md)
  The window’s content view, the highest accessible view object in the window’s view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentviewcontroller)*