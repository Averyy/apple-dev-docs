# line1ImageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The image to display.

**Availability**:
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var line1ImageProvider: CLKFullColorImageProvider { get set }
```

```objc
@property (nonatomic, copy) CLKFullColorImageProvider * line1ImageProvider;
```

## Discussion

This image provider produces a full-color image, masked to a circle.

## See Also

### Setting the Complicaiton Data
- [var line2TextProvider: CLKTextProvider](./line2textprovider.md)
  The text to display below the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularstackimage/line1imageprovider)*