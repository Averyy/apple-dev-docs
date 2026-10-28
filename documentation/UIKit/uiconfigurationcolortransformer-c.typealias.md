# UIConfigurationColorTransformer

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

Generates a modified output color from an input color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
typedef UIColor *(^)(UIColor *) UIConfigurationColorTransformer;
```

## Discussion

A color transformer takes an input color and modifies it to produce a different output color. For example, you might have a color transformer that returns a grayscale or reduced alpha version of the input color.

Because color transformers can use the same base input color to produce a number of variants of that color, you can create different appearances for different states of your views.

## Topics

### Creating a color transformer
- [UIConfigurationColorTransformerGrayscale](./uiconfigurationcolortransformergrayscale.md)
  A color transformer that returns a grayscale version of the color.
- [UIConfigurationColorTransformerPreferredTint](./uiconfigurationcolortransformerpreferredtint.md)
  A color transformer that returns the preferred system accent color.
- [UIConfigurationColorTransformerMonochromeTint](./uiconfigurationcolortransformermonochrometint.md)
  A color transformer that returns the color with a monochrome tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-c.typealias)*