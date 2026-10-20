# setWeight(_:forTargetAt:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Specifies a weight value at a specified target index.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func setWeight(_ weight: CGFloat, forTargetAt targetIndex: Int)
```

```objc
- (void) setWeight:(CGFloat) weight forTargetAtIndex:(NSUInteger) targetIndex;
```

#### Discussion

Target geometries and their weights determine the current form of the surface produced by the morpher. For example, if a morpher has one target whose weight is `0.5`, the form of the resulting surface will be halfway between those of the base geometry and the target geometry.

You can also animate weights implicitly or explicitly using the keypath `weights[index]`, where `index` corresponds to the `targetIndex` parameter of this method.

## Parameters

- `weight`: A number specifying the contribution of the target geometry to the blended surface, generally between `0.0` and `1.0`.
- `targetIndex`: The index of a geometry in the morpher’s [`targets`](./targets.md) array.

## See Also

### Blending between Morph Targets
- [func weight(forTargetAt: Int) -> CGFloat](./weight%28fortargetat%29.md)
  Returns the weight value for the specified target index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorpher/setweight(_:fortargetat:))*