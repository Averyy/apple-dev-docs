# init(named:inBundle:compatibleWithTraitCollection:)

**Framework**: UIKit  
**Kind**: init

Creates a color object using the named asset that’s compatible with the specified trait collection.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(named name: String, inBundle bundle: Bundle?, compatibleWithTraitCollection traitCollection: UITraitCollection?)
```

#### Return Value

An initialized color object. The returned object uses the color space specified for the asset.

## Parameters

- `name`: The name of the asset containing the color.
- `bundle`: The bundle containing the asset.
- `traitCollection`: The trait collection that specifies the gamut to use when selecting the color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicolor/init(named:inbundle:compatiblewithtraitcollection:))*