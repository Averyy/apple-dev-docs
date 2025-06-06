# configurationWithoutPointSizeAndWeight()

**Framework**: UIKit  
**Kind**: method

Returns a copy of the current symbol configuration object without point-size and weight information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func configurationWithoutPointSizeAndWeight() -> Self
```

#### Return Value

A new symbol configuration object without the specified information.

#### Discussion

This method sets the weight value in the new object to [`UIImage.SymbolWeight.unspecified`](uiimage/symbolweight/unspecified.md) and removes the point-size information.

## See Also

- [func configurationWithoutScale() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithoutscale.md)
  Returns a copy of the current symbol configuration object without scale information.
- [func configurationWithoutTextStyle() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithouttextstyle.md)
  Returns a copy of the current symbol configuration object without font text style information.
- [func configurationWithoutWeight() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithoutweight.md)
  Returns a copy of the current symbol configuration object without weight information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/configurationwithoutpointsizeandweight())*