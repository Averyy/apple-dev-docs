# indicator

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style of the indicator that appears on the button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) UIButtonConfigurationIndicator indicator;
```

#### Discussion

Use this property to control the style of the indicator that appears on the trailing edge of the button. For example, the following code disables the indicator by setting this style to [`UIButtonConfigurationIndicatorNone`](../uibuttonconfigurationindicator/uibuttonconfigurationindicatornone.md).

```objc
UIButtonConfiguration *config = UIButtonConfiguration.filledButtonConfiguration;
config.indicator = UIButtonConfigurationIndicatorNone;
```

## See Also

### Configuring the indicator
- [UIButtonConfigurationIndicator](../uibuttonconfigurationindicator.md)
  Constants that determine the style of the indicator that appears on a button.
- [indicatorColorTransformer](./indicatorcolortransformer.md)
  The color transformer for resolving the indicator color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration/indicator)*