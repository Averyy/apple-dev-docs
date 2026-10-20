# textProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var textProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * textProvider;
```

#### Discussion

This property supports multicolor text.

## See Also

### Setting the Complication Data
- [var imageProvider: CLKFullColorImageProvider](./imageprovider.md)
  The image to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornertextimage/textprovider)*