# body2TextProvider

**Framework**: ClockKit  
**Kind**: property

The secondary body text to display in the complication.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var body2TextProvider: CLKTextProvider? { get set }
```

#### Discussion

In watchOS 5 and earlier, the system always displays the text as white. In watchOS 6 and later, it can display multicolor text.

## See Also

- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularstandardbody/headertextprovider.md)
  The header text to display in the complication.
- [var headerImageProvider: CLKFullColorImageProvider?](clkcomplicationtemplategraphicrectangularstandardbody/headerimageprovider.md)
  The header image to display.
- [var body1TextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangularstandardbody/body1textprovider.md)
  The main body text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbody/body2textprovider)*