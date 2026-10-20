# default

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The default font metrics object for content.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class var `default`: UIFontMetrics { get }
```

```objc
@property (class, strong, readonly) UIFontMetrics * defaultMetrics;
```

#### Discussion

The font metrics object in this property uses the [`body`](../uifont/textstyle/body.md) style.

## See Also

### Creating a Font Metrics Object
- [init(forTextStyle: UIFont.TextStyle)](./init%28fortextstyle%29.md)
  Creates a font metrics object for the specified text style.
- [UIFont.TextStyle](../uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/default)*