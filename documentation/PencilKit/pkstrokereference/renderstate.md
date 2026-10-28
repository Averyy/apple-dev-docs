# renderState

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The render details of the stroke, such as particle positioning. Uses default rendering when nil.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderState: PKStrokeRenderStateReference? { get }
```

```objc
@property (nonatomic, readonly, nullable) PKStrokeRenderState * renderState;
```

## Discussion

This may be set on substrokes returned by `-substrokeWithRange:`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/renderstate)*