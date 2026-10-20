# overlay(forType:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the Core Animation layer associated with a layer type.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func overlay(forType layerType: String!) -> CALayer!
```

```objc
- (CALayer *) overlayForType:(NSString *) layerType;
```

#### Return Value

The Core Animation layer.

## Parameters

- `layerType`: A layer type. See [Overlay Types](../overlay-types.md).

## See Also

### Working With Core Animation
- [func setOverlay(CALayer!, forType: String!)](./setoverlay%28_,fortype%29.md)
  Sets an overlay type for a Core Animation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageview/overlay(fortype:))*