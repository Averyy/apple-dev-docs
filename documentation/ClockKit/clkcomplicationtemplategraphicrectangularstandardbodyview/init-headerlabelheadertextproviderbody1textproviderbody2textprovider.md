# init(headerLabel:headerTextProvider:body1TextProvider:body2TextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template that has a header row with a SwiftUI view and text, and two rows of body text.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(headerLabel: Label, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, body2TextProvider: CLKTextProvider? = nil)
```

## Parameters

- `headerLabel`: The SwiftUI view displayed by the template.
- `headerTextProvider`: The text provider for the header text. The template supports multicolored text from this text provider.
- `body1TextProvider`: The text provider for the first row of body text. The template supports multicolored text from this text provider.
- `body2TextProvider`: The text provider for the second row of body text. The template supports multicolored text from this text provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbodyview/init(headerlabel:headertextprovider:body1textprovider:body2textprovider:))*