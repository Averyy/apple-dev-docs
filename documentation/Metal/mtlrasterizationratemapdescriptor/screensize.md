# screenSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The size of the viewport coordinate system, in logical pixels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var screenSize: MTLSize { get set }
```

```objc
@property (nonatomic) MTLSize screenSize;
```

## Mentions

- [Creating a rasterization rate map](../creating-a-rasterization-rate-map.md)

#### Discussion

Metal ignores the depth component of this property.

The viewport coordinate system’s origin is always at `(0,0)` and this property determines its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/screensize)*