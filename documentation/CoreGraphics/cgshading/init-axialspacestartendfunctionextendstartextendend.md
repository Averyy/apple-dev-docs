# init(axialSpace:start:end:function:extendStart:extendEnd:)

**Framework**: Core Graphics  
**Kind**: init

Creates a shading object to use for axial shading.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(axialSpace space: CGColorSpace, start: CGPoint, end: CGPoint, function: CGFunction, extendStart: Bool, extendEnd: Bool)
```

#### Return Value

A new Core Graphics axial shading. In Objective-C, you’re responsible for releasing this object using [`CGShadingRelease`](cgshadingrelease.md).

#### Discussion

An axial shading is a color blend that varies along a linear axis between two endpoints and extends indefinitely perpendicular to that axis. When you are ready to draw the shading, call the function [`drawShading(_:)`](cgcontext/drawshading(_:).md).

## Parameters

- `space`: The color space in which color values are expressed. Core Graphics retains this object; upon return, you may safely release it.
- `start`: The starting point of the axis, in the shading’s target coordinate space.
- `end`: The ending point of the axis, in the shading’s target coordinate space.
- `function`: A CGFunction object created by the function  . This object refers to your function for creating an axial shading. Core Graphics retains this object; upon return, you may safely release it.
- `extendStart`: A Boolean value that specifies whether to extend the shading beyond the starting point of the axis.
- `extendEnd`: A Boolean value that specifies whether to extend the shading beyond the ending point of the axis.

## See Also

- [init?(radialSpace: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)](cgshading/init(radialspace:start:startradius:end:endradius:function:extendstart:extendend:).md)
  Creates a shading object to use for radial shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgshading/init(axialspace:start:end:function:extendstart:extendend:))*