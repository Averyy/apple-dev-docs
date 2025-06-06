# setForegroundLayer(_:)

**Framework**: Quartz  
**Kind**: method

The Core Animation layer used as the foreground overlay.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setForegroundLayer(_ aLayer: CALayer!)
```

#### Discussion

The foreground overlay layer can have sublayers. Additionally, the layers can also contain animations.

The foreground layer is an overlay that is applied to the view. It can be used to provide information such as loading progress or for pure cosmetic purposes, such as dark gradients on top and bottom of the browser view.

This layer is optional.

## Parameters

- `aLayer`: A   instance.

## See Also

- [func foregroundLayer() -> CALayer!](ikimagebrowserview/foregroundlayer.md)
  Returns the foreground Core Animation layer
- [func setBackgroundLayer(CALayer!)](ikimagebrowserview/setbackgroundlayer(_:).md)
  The Core Animation layer used as the view’s background.
- [func backgroundLayer() -> CALayer!](ikimagebrowserview/backgroundlayer.md)
  Returns the foreground Core Animation layer


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setforegroundlayer(_:))*