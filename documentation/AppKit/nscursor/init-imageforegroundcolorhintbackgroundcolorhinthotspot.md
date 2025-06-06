# init(image:foregroundColorHint:backgroundColorHint:hotSpot:)

**Framework**: AppKit  
**Kind**: init

Initializes the cursor with the specified image and hot spot.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init(image newImage: NSImage, foregroundColorHint fg: NSColor?, backgroundColorHint bg: NSColor?, hotSpot: NSPoint)
```

#### Return Value

The initialized cursor object.

## Parameters

- `newImage`: The image to assign to the cursor.
- `fg`: The foreground color. This is currently ignored.
- `bg`: The background color. This is currently ignored.
- `hotSpot`: The point to assign as the cursor’s hot spot.

## See Also

- [init(image: UIImage, hotSpot: NSPoint)](nscursor/init(image:hotspot:).md)
  Initializes a cursor with the given image and hot spot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/init(image:foregroundcolorhint:backgroundcolorhint:hotspot:))*