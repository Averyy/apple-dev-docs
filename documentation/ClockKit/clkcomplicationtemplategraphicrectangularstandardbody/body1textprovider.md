# body1TextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The main body text to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var body1TextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * body1TextProvider;
```

#### Discussion

In watchOS 5 and earlier, the system always displays the text as white. In watchOS 6 and later, it can display multicolor text.

## See Also

### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The header text to display in the complication.
- [var headerImageProvider: CLKFullColorImageProvider?](./headerimageprovider.md)
  The header image to display.
- [var body2TextProvider: CLKTextProvider?](./body2textprovider.md)
  The secondary body text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbody/body1textprovider)*