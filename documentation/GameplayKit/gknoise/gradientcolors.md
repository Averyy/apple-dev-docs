# gradientColors

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

A dictionary mapping noise values to colors for use in colorizing generated noise.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var gradientColors: [NSNumber : UIColor] { get set }
```

*macOS*

```swift
var gradientColors: [NSNumber : NSColor] { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, copy) NSDictionary<NSNumber *,UIColor *> * gradientColors;
```

*macOS*

```objc
@property (nonatomic, copy) NSDictionary<NSNumber *,NSColor *> * gradientColors;
```

## Discussion

The noise object does not store noise values or color bitmap data; instead, this property specifies a color ramp as metadata to accompany the noise object. When you later create a [`GKNoiseMap`](../gknoisemap.md) object from this noise object and use the [`init(noiseMap:)`](../../SpriteKit/sktexture/init%28noisemap%29.md) method to generate a texture image from the noise map, the [`SKTexture`](../../SpriteKit/sktexture.md) class automatically uses the gradient colors from the noise map’s underlying noise objects. If you combine noise objects using the [`init(componentNoises:selectionNoise:)`](./init%28componentnoises,selectionnoise%29.md) method before generating a noise map, texture generation automatically uses the color gradient corresponding to each component noise for the regions of the noise map where that noise appears.

Each key in this dictionary specifies a value in the generated noise field, and the corresponding value for that key is the color to associate with that noise value when generating textures or images from the noise field. When the [`SKTexture`](../../SpriteKit/sktexture.md) class generates a texture image, it creates a gradient by interpolating colors for noise values in between those you specify.

![](https://developer.apple.com/tutorials/images/com.apple.gameplaykit/media-2556371@2x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknoise/gradientcolors)*