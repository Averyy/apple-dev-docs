# init(image:hotSpot:)

**Framework**: AppKit  
**Kind**: init

Initializes a cursor with the given image and hot spot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
init(image newImage: NSImage, hotSpot point: NSPoint)
```

#### Return Value

An initialized cursor object.

#### Discussion

This method is the designated initializer for the class.

## Parameters

- `newImage`: The image to assign to the cursor.
- `point`: The point to set as the cursor’s hot spot.

## See Also

- [var image: UIImage](nscursor/image.md)
  The cursor’s image.
- [Cursor Management](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CursorMgmt/CursorMgmt.html#//apple_ref/doc/uid/10000066i)
- [var hotSpot: NSPoint](nscursor/hotspot.md)
  The position of the click location within the cursor.
- [init(coder: NSCoder)](nscursor/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/init(image:hotspot:))*