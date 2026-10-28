# init(forTextStyle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a font metrics object for the specified text style.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(forTextStyle textStyle: UIFont.TextStyle)
```

```objc
- (instancetype) initForTextStyle:(UIFontTextStyle) textStyle;
```

## Return Value

An initialized font metrics object.

## Parameters

- `textStyle`: The text style that you want to apply to the font. For example, you might specify [`body`](../uifont/textstyle/body.md) for your app’s main content.

## See Also

### Creating a Font Metrics Object
- [class var `default`: UIFontMetrics](./default.md)
  The default font metrics object for content.
- [UIFont.TextStyle](../uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [+ metricsForTextStyle:](./metricsfortextstyle_.md)
  Creates and returns a font metrics object for the specified text style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/init(fortextstyle:))*