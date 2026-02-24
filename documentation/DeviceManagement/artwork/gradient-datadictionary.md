# Artwork.Gradient

**Framework**: Device Management  
**Kind**: dictionary

An object that represents the properties of a color gradient for an artwork object.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Artwork.Gradient
```

## Properties

- `color` (string): An ‘rrggbb’ field that defines the color of the gradient. The textColor* fields are not used to define the gradient color when this field is present.
- `y1` (number): A height between 0 and 1 that indicates where the gradient starts, measured from the bottom. If y1 is not present, it defaults to 0.
- `y2` (number): A height between 0 and 1 that indicates where the gradient stops, measured from the bottom of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/artwork/gradient-data.dictionary)*