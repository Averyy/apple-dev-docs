# indicatorColorTransformer

**Framework**: UIKit  
**Kind**: property

The color transformer for resolving the indicator color.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
var indicatorColorTransformer: UIConfigurationColorTransformer? { get set }
```

#### Discussion

Use this color transformer to set a custom color for [`indicator`](uibuttonconfiguration/indicator.md). For example, the following code uses a grayscale color for the indicator instead of the default color.

```swift
var config = UIButton.Configuration.filled()
config.indicatorColorTransformer = UIConfigurationColorTransformer.grayscale
```

## See Also

- [var indicator: UIButton.Configuration.Indicator](uibutton/configuration-swift.struct/indicator-swift.property.md)
  The style of the indicator that appears on the button.
- [UIButton.Configuration.Indicator](uibutton/configuration-swift.struct/indicator-swift.enum.md)
  Constants that determine the style of the indicator that appears on a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/indicatorcolortransformer)*