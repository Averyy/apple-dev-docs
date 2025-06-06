# weight(forTargetAt:)

**Framework**: SceneKit  
**Kind**: method

Returns the weight value for the specified target index.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func weight(forTargetAt targetIndex: Int) -> CGFloat
```

#### Return Value

A number indicating the contribution of the target geometry to the blended surface, generally between `0.0` and `1.0`.

#### Discussion

Target geometries and their weights determine the current form of the surface produced by the morpher. For example, if a morpher has one target whose weight is `0.5`, the form of the resulting surface will be halfway between those of the base geometry and the target geometry.

## Parameters

- `targetIndex`: The index of a geometry in the morpher’s   array.

## See Also

- [func setWeight(CGFloat, forTargetAt: Int)](scnmorpher/setweight(_:fortargetat:).md)
  Specifies a weight value at a specified target index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmorpher/weight(fortargetat:))*