# totalBounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The most recent bounding rectangle that the system used to draw the string.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var totalBounds: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect totalBounds;
```

#### Discussion

This property contains the bounding rectangle that was last used when calling the [`draw(with:options:context:)`](../../Foundation/nsattributedstring/draw%28with,options,context%29.md) method. The rectangle is specified in the coordinate system of the drawn string. (The origin of the bounds corresponds to neither a view the string might have been drawn into nor the origin of a possible [`draw(in:)`](../../Foundation/nsattributedstring/draw%28in%29.md) call.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/totalbounds)*