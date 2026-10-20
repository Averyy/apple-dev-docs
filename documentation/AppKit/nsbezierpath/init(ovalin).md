# init(ovalIn:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
init(ovalIn rect: NSRect)
```

```objc
+ (NSBezierPath *) bezierPathWithOvalInRect:(NSRect) rect;
```

#### Return Value

An `NSBezierPath` new path object with the oval path.

#### Discussion

If the `aRect` parameter specifies a square, the inscribed path is a circle. The path is constructed by starting in the lower-right quadrant of the rectangle and adding arc segments counterclockwise to complete the oval.

## Parameters

- `rect`: The rectangle in which to inscribe an oval.

## See Also

### Related Documentation
- [func appendOval(in: NSRect)](./appendoval%28in%29.md)
  Appends an oval path to the path, inscribing the oval in the specified rectangle.
### Creating a Bézier Path
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](./init%28roundedrect,xradius,yradius%29.md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](./init%28cgpath%29-96cxk.md)
- [var flattened: NSBezierPath](./flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](./reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/init(ovalin:))*