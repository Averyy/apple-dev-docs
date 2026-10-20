# preferringMonochrome()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a color configuration that specifies that the symbol image uses its monochrome variant.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func preferringMonochrome() -> Self
```

```objc
+ (instancetype) configurationPreferringMonochrome;
```

## Mentions

- [Configuring and displaying symbol images in your UI](../../configuring-and-displaying-symbol-images-in-your-ui.md)

#### Return Value

A symbol configuration that acquires the monochrome variant of a symbol.

## See Also

### Creating a color configuration
- [convenience init(hierarchicalColor: UIColor)](./init%28hierarchicalcolor%29.md)
  Creates a color configuration with a color scheme that originates from one color.
- [convenience init(paletteColors: [UIColor])](./init%28palettecolors%29.md)
  Creates a color configuration with a color scheme from a palette of multiple colors.
- [class func preferringMulticolor() -> Self](./preferringmulticolor%28%29.md)
  Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/preferringmonochrome())*