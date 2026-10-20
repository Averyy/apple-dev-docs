# setOverlay(_:forType:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets an overlay type for a Core Animation layer.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setOverlay(_ layer: CALayer!, forType layerType: String!)
```

```objc
- (void) setOverlay:(CALayer *) layer forType:(NSString *) layerType;
```

## Parameters

- `layer`: A Core Animation layer object.
- `layerType`: A layer type. See [Overlay Types](../overlay-types.md).

## See Also

### Working With Core Animation
- [func overlay(forType: String!) -> CALayer!](./overlay%28fortype%29.md)
  Returns the Core Animation layer associated with a layer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/setoverlay(_:fortype:))*