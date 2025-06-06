# configurationWithoutScale()

**Framework**: UIKit  
**Kind**: method

Returns a copy of the current symbol configuration object without scale information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func configurationWithoutScale() -> Self
```

#### Return Value

A new symbol configuration object without the specified information.

#### Discussion

This method sets the scale value in the new object to [`UIImage.SymbolScale.unspecified`](uiimage/symbolscale/unspecified.md).

## See Also

- [func configurationWithoutPointSizeAndWeight() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithoutpointsizeandweight.md)
  Returns a copy of the current symbol configuration object without point-size and weight information.
- [func configurationWithoutTextStyle() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithouttextstyle.md)
  Returns a copy of the current symbol configuration object without font text style information.
- [func configurationWithoutWeight() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithoutweight.md)
  Returns a copy of the current symbol configuration object without weight information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutscale())*