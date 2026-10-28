# iesProfileURL

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The URL for a file that contains photometry data describing the intended appearance of the light.

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
var iesProfileURL: URL? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSURL * IESProfileURL;
```

## Discussion

A photometric light source is one whose shape, direction, and intensity of illumination is determined by a file in the IES format, containing physical measurements of a light source. Many manufacturers of real-world light fixtures publish such files describing the lighting characteristics of their products. This photometry data measures the light web surrounding a light source—measurements of the light’s intensity in all directions around the source.

By default, this property’s value is `nil`. After setting this property to a URL that references a valid IES profile, you must set the light’s type property to [`IES`](./lighttype/ies.md) to load that file and apply its effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlight/iesprofileurl)*