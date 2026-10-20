# init(draw:delegate:)

**Framework**: AppKit  
**Kind**: init

Returns a representation of an image initialized with the specified delegate information.

**Availability**:
- macOS ?+

## Declaration

```swift
init(draw selector: Selector, delegate: Any)
```

#### Return Value

An initialized [`NSCustomImageRep`](nscustomimagerep.md) object, or `nil` if the object could not be initialized.

#### Discussion

When the receiver is asked to draw the image, it sends the specified message to the selector, passing itself as a parameter to the delegate method. The delegate’s drawing method should have the following form:

```objc
- (void)myCustomDrawMethod:(id)anNSCustomImageRep;
```

## Parameters

- `selector`: The selector to call when it is time to draw the image. The method should take a single parameter of type `id` that represents the [`NSCustomImageRep`](nscustomimagerep.md) object that initiated drawing. The method must draw the image starting at the point (0, 0) in the current coordinate system.
- `delegate`: The delegate object that responds to the selector in `aMethod`.

## See Also

- [func draw() -> Bool](nsimagerep/draw.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [init(size: NSSize, flipped: Bool, drawingHandler: (NSRect) -> Bool)](nscustomimagerep/init(size:flipped:drawinghandler:).md)
  Initializes a representation of an image of the specified size and flipped status, using a block to draw its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomimagerep/init(draw:delegate:))*