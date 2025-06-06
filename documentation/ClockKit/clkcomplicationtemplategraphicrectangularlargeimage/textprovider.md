# textProvider

**Framework**: ClockKit  
**Kind**: property

The header text to display in the complication.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var textProvider: CLKTextProvider { get set }
```

#### Discussion

This property supports multicolor text.

In watchOS 5 and earlier, the system converts the text to uppercase before displaying it. In watchOS 6 and later, it displays the text using its original case.

## See Also

- [var imageProvider: CLKFullColorImageProvider](clkcomplicationtemplategraphicrectangularlargeimage/imageprovider.md)
  The image to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularlargeimage/textprovider)*