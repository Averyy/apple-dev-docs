# view

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The custom view you use to draw the toolbar item.

**Availability**:
- macOS

## Declaration

```swift
var view: NSView? { get set }
```

```objc
@property (strong, nullable) NSView * view;
```

#### Discussion

Many properties of [`NSToolbarItem`](../nstoolbaritem.md) automatically forward changes to the associated custom [`NSView`](../nsview.md) object, if the view has a property or accessor method with a matching name.

## See Also

### Getting the item’s visual appearance
- [var image: UIImage?](./image.md)
  The image to display for the toolbar item.
- [var backgroundTintColor: UIColor?](./backgroundtintcolor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/view)*