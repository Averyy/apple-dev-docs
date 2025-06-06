# view

**Framework**: AppKit  
**Kind**: property

The view controller’s primary view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@IBOutlet
@MainActor var view: NSView { get set }
```

#### Discussion

If this property’s value is not already set when you access it, the view controller invokes the [`loadView()`](nsviewcontroller/loadview().md) method. That method, in turn, sets the view from the nib file identified by the view controller’s [`nibName`](nsviewcontroller/nibname.md) and [`nibBundle`](nsviewcontroller/nibbundle.md) properties.

If you want to set a view controller’s view directly, set this property’s value immediately after creating the view controller.

## See Also

- [var title: String?](nsviewcontroller/title.md)
  The localized title of the receiver’s primary view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/view)*