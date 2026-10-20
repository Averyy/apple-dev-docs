# init(radialHeadroom:space:start:startRadius:end:endRadius:function:extendStart:extendEnd:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init?(radialHeadroom headroom: Float, space: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)
```

```c
extern CGShadingRefCGShadingCreateRadialWithContentHeadroom(float headroom, CGColorSpaceRef space, CGPoint start, CGFloat startRadius, CGPoint end, CGFloat endRadius, CGFunctionRef function, bool extendStart, bool extendEnd);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgshading/init(radialheadroom:space:start:startradius:end:endradius:function:extendstart:extendend:))*