# transform(using:)

**Framework**: AppKit  
**Kind**: method

Transforms all points in the path using the specified transform.

**Availability**:
- macOS ?+

## Declaration

```swift
func transform(using transform: AffineTransform)
```

#### Discussion

This method applies the transform to the path’s points immediately. The following code translates a line from 0,0 to 100,100 to a line from 10,10 to 110,110.

```objc
NSBezierPath *bezierPath = [NSBezierPath bezierPath];
NSAffineTransform *transform = [NSAffineTransform transform];
 
[bezierPath moveToPoint: NSMakePoint(0.0, 0.0)];
[bezierPath lineToPoint: NSMakePoint(100.0, 100.0)];
 
[transform translateXBy: 10.0 yBy: 10.0];
[bezierPath transformUsingAffineTransform: transform];
```

## Parameters

- `transform`: The transform to apply to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/transform(using:))*