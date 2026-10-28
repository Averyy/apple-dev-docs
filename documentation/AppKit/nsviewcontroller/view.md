# view

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view controller’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@IBOutlet
var view: NSView { get set }
```

```objc
@property (strong) NSView * view;
```

## Discussion

If this property’s value is not already set when you access it, the view controller invokes the [`loadView()`](./loadview%28%29.md) method. That method, in turn, sets the view from the nib file identified by the view controller’s [`nibName`](./nibname.md) and [`nibBundle`](./nibbundle.md) properties.

If you want to set a view controller’s view directly, set this property’s value immediately after creating the view controller.

## See Also

### View Properties
- [var title: String?](./title.md)
  The localized title of the receiver’s primary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/view)*