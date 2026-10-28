# intensity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A number between `0.0` and `1.0` that modulates the effect of the material property. Animatable.

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
var intensity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat intensity;
```

## Discussion

The default intensity is `1.0`. Reducing the intensity fades out the contents of the material property, causing different effects depending on which visual property of an [`SCNMaterial`](../scnmaterial.md) object it represents:

- For the [`normal`](../scnmaterial/normal.md) property, intensity varies the apparent roughness of the normal-mapped surface. Reducing intensity makes the surface appear more smooth.
- For the [`multiply`](../scnmaterial/multiply.md) property, reducing intensity blends the material property’s colors with white, effectively reducing the strength of the color multiplication effect.
- For all other properties, reducing intensity dims the material property’s contents.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Working with Material Property Contents
- [var contents: Any?](./contents.md)
  The visual contents of the material property—a color, image, or source of animated content. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/intensity)*