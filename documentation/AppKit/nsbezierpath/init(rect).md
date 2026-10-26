# init(rect:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new Bézier path object initialized with a rectangular path.

**Availability**:
- macOS

## Declaration

```swift
init(rect: NSRect)
```

```objc
+ (NSBezierPath *) bezierPathWithRect:(NSRect) rect;
```

#### Return Value

A new path object with the rectangular path.

#### Discussion

The path is constructed by starting at the origin of `aRect` and adding line segments in a counterclockwise direction.

## Parameters

- `rect`: The rectangle describing the path to create.

## See Also

### Related Documentation
- [class func fill(NSRect)](./fill%28_%29.md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](./stroke%28_%29.md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [func appendRect(NSRect)](./appendrect%28_%29.md)
  Appends a rectangular path to the path.
- [+ bezierPath](./bezierpath.md)
  Creates and returns a new Bézier path object.
### Creating a Bézier Path
- [init(ovalIn: NSRect)](./init%28ovalin%29.md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](./init%28roundedrect,xradius,yradius%29.md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](./init%28cgpath%29-96cxk.md)
- [var flattened: NSBezierPath](./flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](./reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/init(rect:))*