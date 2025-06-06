# UIConfigurationColorTransformer

**Framework**: UIKit  
**Kind**: struct

A transformer that generates a modified output color from an input color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct UIConfigurationColorTransformer
```

#### Overview

A color transformer takes an input color and modifies it to produce a different output color. For example, you might have a color transformer that returns a grayscale or reduced alpha version of the input color.

Because color transformers can use the same base input color to produce a number of variants of that color, you can create different appearances for different states of your views.

## Topics

### Creating a color transformer
- [init((UIColor) -> UIColor)](uiconfigurationcolortransformer-swift.struct/init(_:).md)
  Creates a color transformer with the specified closure.
- [static let grayscale: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/grayscale.md)
  Creates a color transformer that generates a grayscale version of the color.
- [static let preferredTint: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/preferredtint.md)
  A color transformer that returns the preferred system accent color.
- [static let monochromeTint: UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct/monochrometint.md)
  A color transformer that returns the color with a monochrome tint.
### Calling the color transformer
- [let transform: (UIColor) -> UIColor](uiconfigurationcolortransformer-swift.struct/transform.md)
  The transform closure of the color transformer.
- [func callAsFunction(UIColor) -> UIColor](uiconfigurationcolortransformer-swift.struct/callasfunction(_:).md)
  Calls the transform closure of the color transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct)*