# indicatorColorTransformer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color transformer for resolving the indicator color.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) UIConfigurationColorTransformer indicatorColorTransformer;
```

## Discussion

Use this color transformer to set a custom color for [`indicator`](./indicator.md). For example, the following code uses a grayscale color for the indicator instead of the default color.

```objc
UIButtonConfiguration *config = UIButtonConfiguration.filledButtonConfiguration;
config.indicatorColorTransformer = UIConfigurationColorTransformerGrayscale;
```

## See Also

### Configuring the indicator
- [indicator](./indicator.md)
  The style of the indicator that appears on the button.
- [UIButtonConfigurationIndicator](../uibuttonconfigurationindicator.md)
  Constants that determine the style of the indicator that appears on a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration/indicatorcolortransformer)*