# draggingImageComponents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns dragging images for the cell.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var draggingImageComponents: [NSDraggingImageComponent] { get }
```

```objc
@property (strong, readonly) NSArray<NSDraggingImageComponent *> * draggingImageComponents;
```

#### Discussion

The default implementation of this method returns an array of up to two `NSDraggingImageComponent` instances – one for the [`imageView`](./imageview.md) and another for the [`textField`](./textfield.md) (unless the property is `nil`).

These method can be subclassed and overridden to provide a custom set of `NSDraggingImageComponent` objects to create the drag image from this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecellview/draggingimagecomponents)*