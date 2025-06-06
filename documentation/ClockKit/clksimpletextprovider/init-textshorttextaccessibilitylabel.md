# init(text:shortText:accessibilityLabel:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider with the text strings and an accessible string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(text: String, shortText: String?, accessibilityLabel: String?)
```

#### Return Value

A text provider initialized with the specified content.

## Parameters

- `text`: The text that you want to display.
- `shortText`: A shorter version of the value in the   parameter that conveys the same information.
- `accessibilityLabel`: A succinct string that identifies the purpose of the text.

## See Also

- [convenience init(text: String)](clksimpletextprovider/init(text:).md)
  Creates and returns a text provider with the specified long form text.
- [convenience init(text: String, shortText: String?)](clksimpletextprovider/init(text:shorttext:).md)
  Creates and returns a text provider with both long and short versions of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/init(text:shorttext:accessibilitylabel:))*