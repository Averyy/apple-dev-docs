# metricsForTextStyle:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a font metrics object for the specified text style.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```objc
+ (instancetype) metricsForTextStyle:(UIFontTextStyle) textStyle;
```

#### Return Value

An initialized font metrics object.

## Parameters

- `textStyle`: The text style that you want to apply to the font. For example, you might specify [`body`](../uifont/textstyle/body.md) for your app’s main content.

## See Also

### Creating a Font Metrics Object
- [init(forTextStyle: UIFont.TextStyle)](./init%28fortextstyle%29.md)
  Creates a font metrics object for the specified text style.
- [class var `default`: UIFontMetrics](./default.md)
  The default font metrics object for content.
- [UIFont.TextStyle](../uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/metricsfortextstyle:)*