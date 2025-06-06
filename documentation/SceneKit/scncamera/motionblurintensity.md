# motionBlurIntensity

**Framework**: SceneKit  
**Kind**: property

A factor that determines the intensity of motion blur effects. Animatable.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var motionBlurIntensity: CGFloat { get set }
```

#### Discussion

The default intensity of zero results in no motion blur effect. Higher values (toward a maximum of 1.0) create more pronounced motion blur effects.

Motion blur is not supported when wide-gamut color rendering is enabled. Wide-gamut rendering is enabled by default on supported devices; to opt out, set the `SCNDisableWideGamut` key in your app’s `Info.plist` file.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/motionblurintensity)*