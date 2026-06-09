# init(imageCell:)

**Framework**: AppKit  
**Kind**: init

Returns an `NSCell` object initialized with the specified image and set to have the cell’s default menu.

**Availability**:
- macOS ?+

## Declaration

```swift
init(imageCell image: NSImage?)
```

#### Return Value

An initialized `NSCell` object, or `nil` if the cell could not be initialized.

#### Discussion

This is one of four designated initializers you must implement when subclassing. See [`Designated Initializers`](nscell#Designated-Initializers.md) for the complete list.

## Parameters

- `image`: The image to use for the cell. If this parameter is `nil`, no image is set.

## See Also

- [class NSCell](nscell.md)
  A mechanism for displaying text or images in a view object without the overhead of a full [`NSView`](nsview.md) subclass.
- [init(textCell: String)](nscell/init(textcell:).md)
  Returns an NSCell object initialized with the specified string and set to have the cell’s default menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/init(imagecell:))*