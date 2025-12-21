# size

**Framework**: RealityKit  
**Kind**: property

The size of the canvas in points.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var size: CGSize { get set }
```

#### Discussion

This defines both how large the canvas is for text layout, as well as how large it is in world-space. The canvas coordinate system uses the standard CoreGraphics / CoreText coordinate space. There is no explicit backing-buffer size, as it might be dynamic to generate high-fidelity text. The canvas size uses points as 1/72nd of an inch (about 0.352 mm) in world-space. World-size might change as a function of any peer or parent transform component.

This component lays out text using default `AttributedString` behaviors, but respecting the `edgeInsets` property. Text will wrap-around, rather than truncate. It will stay at the given fixed font size, and will not stretch or scale to fit.  CoreText can determine the required canvas size for a particular string or layout. The canvas size is clamped to a maximum of 2048 points in width and height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textcomponent/size)*