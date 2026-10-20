# init(image:hotSpot:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a cursor with the given image and hot spot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

*Mac Catalyst*

```swift
init(image newImage: UIImage, hotSpot point: NSPoint)
```

*macOS*

```swift
init(image newImage: NSImage, hotSpot point: NSPoint)
```

*Mac Catalyst*

```objc
- (instancetype) initWithImage:(UIImage *) newImage hotSpot:(NSPoint) point;
```

*macOS*

```objc
- (instancetype) initWithImage:(NSImage *) newImage hotSpot:(NSPoint) point;
```

#### Return Value

An initialized cursor object.

#### Discussion

This method is the designated initializer for the class.

## Parameters

- `newImage`: The image to assign to the cursor.
- `point`: The point to set as the cursor’s hot spot.

## See Also

### Related Documentation
- [var image: UIImage](./image.md)
  The cursor’s image.
- [Cursor Management](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CursorMgmt/CursorMgmt.html#//apple_ref/doc/uid/10000066i)
- [var hotSpot: NSPoint](./hotspot.md)
  The position of the click location within the cursor.
### Initializing a new cursor
- [init(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscursor/init(image:hotspot:))*