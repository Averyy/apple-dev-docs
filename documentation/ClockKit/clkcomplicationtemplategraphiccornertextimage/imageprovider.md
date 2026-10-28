# imageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The image to display.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var imageProvider: CLKFullColorImageProvider { get set }
```

```objc
@property (nonatomic, copy) CLKFullColorImageProvider * imageProvider;
```

## Discussion

This image provider produces a full-color image, masked to a circle.

## See Also

### Setting the Complication Data
- [var textProvider: CLKTextProvider](./textprovider.md)
  The text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornertextimage/imageprovider)*