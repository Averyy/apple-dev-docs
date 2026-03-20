# imageDidNotDraw(_:in:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the image object is unable, for whatever reason, to lock focus on its image or draw in the specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
optional func imageDidNotDraw(_ sender: NSImage, in rect: NSRect) -> NSImage?
```

#### Return Value

An `NSImage` to draw in place of the one in `sender`, or `nil` if the delegate wants to draw the image itself.

#### Discussion

The delegate can do one of the following:

- Return another `NSImage` object to draw in the sender’s place.
- Draw the image itself and return `nil`.
- Simply return `nil` to indicate that `sender` should give up on the attempt at drawing the image.

## Parameters

- `sender`: The `NSImage` object that encountered the problem.
- `rect`: The rectangle that the image object was attempting to draw.

## See Also

- [class NSImage](nsimage.md)
  A high-level interface for manipulating image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagedelegate/imagedidnotdraw(_:in:))*