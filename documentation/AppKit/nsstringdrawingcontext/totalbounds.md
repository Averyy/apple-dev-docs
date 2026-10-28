# totalBounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The most recent bounding rectangle that the system used to draw the string.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var totalBounds: CGRect { get }
```

```objc
@property (readonly) CGRect totalBounds;
```

## Discussion

This property contains the bounding rectangle that was last used when calling the [`draw(with:options:context:)`](../../Foundation/nsattributedstring/draw%28with,options,context%29.md) method. The rectangle is specified in the coordinate system of the drawn string. (The origin of the bounds corresponds to neither a view the string might have been drawn into nor the origin of a possible [`draw(in:)`](../../Foundation/nsattributedstring/draw%28in%29.md) call.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext/totalbounds)*