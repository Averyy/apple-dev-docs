# contentViewController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The main content view controller for the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var contentViewController: NSViewController? { get set }
```

```objc
@property (strong, nullable) NSViewController * contentViewController;
```

#### Discussion

The value of this property provides the content view of the window. Setting this value removes the existing value of [`contentView`](./contentview.md) and makes the `contentViewController.view` the main content view for the window. By default, the value of this property is `nil`.

The content view controller controls only the [`contentView`](./contentview.md) object, and not the title of the window. The window title can easily be bound to the [`contentViewController`](./contentviewcontroller.md) object using code such as: `[window bind:NSTitleBinding toObject:contentViewController withKeyPath:@"title" options:nil]`. Setting [`contentViewController`](./contentviewcontroller.md) causes the window to resize based on the current size of the [`contentViewController`](./contentviewcontroller.md); to restrict the size of the window, use Auto Layout (note that the value of this property is encoded in the NIB). Directly assigning a [`contentView`](./contentview.md) value clears out the root view controller.

## See Also

### Related Documentation
- [convenience init(contentViewController: NSViewController)](./init%28contentviewcontroller%29.md)
  Creates a titled window that contains the specified content view controller.
### Configuring the Window’s Content
- [var contentView: NSView?](./contentview.md)
  The window’s content view, the highest accessible view object in the window’s view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/contentviewcontroller)*