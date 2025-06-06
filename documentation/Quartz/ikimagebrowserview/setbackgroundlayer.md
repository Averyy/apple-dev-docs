# setBackgroundLayer(_:)

**Framework**: Quartz  
**Kind**: method

The Core Animation layer used as the view’s background.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setBackgroundLayer(_ aLayer: CALayer!)
```

#### Discussion

The background layer can have sublayers. Additionally, the layers can also contain animations.

The layer is optional.

## Parameters

- `aLayer`: A   instance.

## See Also

- [func setForegroundLayer(CALayer!)](ikimagebrowserview/setforegroundlayer(_:).md)
  The Core Animation layer used as the foreground overlay.
- [func foregroundLayer() -> CALayer!](ikimagebrowserview/foregroundlayer.md)
  Returns the foreground Core Animation layer
- [func backgroundLayer() -> CALayer!](ikimagebrowserview/backgroundlayer.md)
  Returns the foreground Core Animation layer


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setbackgroundlayer(_:))*