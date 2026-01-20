# init(string:)

**Framework**: Core Image  
**Kind**: init

Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
convenience init(string representation: String)
```

#### Return Value

 An autoreleased [`CIColor`](cicolor.md) instance.

#### Discussion

On macOS before 10.10, the CIColor’s color space will be Generic RGB.

## Parameters

- `representation`: A string that contains color and alpha float values.   For example, the string:   indicates an RGB color whose components   are 50% red, 70% green, 30% blue, and 100% opaque.   If the string contains only 3 float values, the alpha component will be    If the string contains no float values, then   will be returned.

## See Also

- [convenience init(red: CGFloat, green: CGFloat, blue: CGFloat)](cicolor/init(red:green:blue:).md)
  Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolor/init(string:))*