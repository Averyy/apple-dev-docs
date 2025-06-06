# indicator

**Framework**: UIKit  
**Kind**: property

The style of the indicator that appears on the button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
var indicator: UIButton.Configuration.Indicator { get set }
```

#### Discussion

Use this property to control the style of the indicator that appears on the trailing edge of the button. For example, the following code disables the indicator by setting this style to [`UIButton.Configuration.Indicator.none`](uibutton/configuration-swift.struct/indicator-swift.enum/none.md).

```swift
var config = UIButton.Configuration.filled()
config.indicator = .none
```

## See Also

- [UIButton.Configuration.Indicator](uibutton/configuration-swift.struct/indicator-swift.enum.md)
  Constants that determine the style of the indicator that appears on a button.
- [var indicatorColorTransformer: UIConfigurationColorTransformer?](uibutton/configuration-swift.struct/indicatorcolortransformer.md)
  The color transformer for resolving the indicator color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/indicator-swift.property)*