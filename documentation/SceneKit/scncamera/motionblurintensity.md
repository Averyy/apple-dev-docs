# motionBlurIntensity

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A factor that determines the intensity of motion blur effects. Animatable.

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
var motionBlurIntensity: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat motionBlurIntensity;
```

## Discussion

The default intensity of zero results in no motion blur effect. Higher values (toward a maximum of 1.0) create more pronounced motion blur effects.

Motion blur is not supported when wide-gamut color rendering is enabled. Wide-gamut rendering is enabled by default on supported devices; to opt out, set the `SCNDisableWideGamut` key in your app’s `Info.plist` file.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/motionblurintensity)*