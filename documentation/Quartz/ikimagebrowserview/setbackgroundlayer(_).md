# setBackgroundLayer(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

The Core Animation layer used as the view’s background.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setBackgroundLayer(_ aLayer: CALayer!)
```

```objc
- (void) setBackgroundLayer:(CALayer *) aLayer;
```

## Discussion

The background layer can have sublayers. Additionally, the layers can also contain animations.

The layer is optional.

## Parameters

- `aLayer`: A `CALayer` instance.

## See Also

### Core Animation Layer Integration
- [func setForegroundLayer(CALayer!)](./setforegroundlayer%28_%29.md)
  The Core Animation layer used as the foreground overlay.
- [func foregroundLayer() -> CALayer!](./foregroundlayer%28%29.md)
  Returns the foreground Core Animation layer
- [func backgroundLayer() -> CALayer!](./backgroundlayer%28%29.md)
  Returns the foreground Core Animation layer


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setbackgroundlayer(_:))*