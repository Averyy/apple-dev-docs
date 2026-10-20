# ctm

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the current transformation matrix.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var ctm: CGAffineTransform { get }
```

```c
extern CGAffineTransform CGContextGetCTM(CGContextRef c);
```

## See Also

### Working with the Current Transformation Matrix
- [func rotate(by: CGFloat)](./rotate%28by%29.md)
  Rotates the user coordinate system in a context.
- [func scaleBy(x: CGFloat, y: CGFloat)](./scaleby%28x,y%29.md)
  Changes the scale of the user coordinate system in a context.
- [func translateBy(x: CGFloat, y: CGFloat)](./translateby%28x,y%29.md)
  Changes the origin of the user coordinate system in a context.
- [func concatenate(CGAffineTransform)](./concatenate%28_%29.md)
  Transforms the user coordinate system in a context using a specified matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/ctm)*