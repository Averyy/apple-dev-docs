# render(using:)

**Framework**: Touch Controller  
**Kind**: method  
**Role**: Instance Method

Renders the touch controls using the provided Metal render command encoder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
func render(using encoder: any MTLRenderCommandEncoder)
```

```objc
- (void) renderUsingRenderCommandEncoder:(id<MTLRenderCommandEncoder>) encoder;
```

## Parameters

- `encoder`: The `MTLRenderCommandEncoder` to use for rendering.

## See Also

### Handling layout updates
- [func automaticallyLayoutControls(for: [TCControlLabel])](./automaticallylayoutcontrols%28for%29.md)
  Automatically lays out the provided control labels, creating them if needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tctouchcontroller/render(using:))*