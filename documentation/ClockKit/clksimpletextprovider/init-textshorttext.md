# init(text:shortText:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider with both long and short versions of the text.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(text: String, shortText: String?)
```

#### Return Value

A text provider initialized with the specified content.

## Parameters

- `text`: The text that you want to display. This value is assigned to the   property of your text provider object.
- `shortText`: A shorter version of the value in the   parameter that conveys the same information.

## See Also

- [convenience init(text: String)](clksimpletextprovider/init(text:).md)
  Creates and returns a text provider with the specified long form text.
- [convenience init(text: String, shortText: String?, accessibilityLabel: String?)](clksimpletextprovider/init(text:shorttext:accessibilitylabel:).md)
  Creates and returns a text provider with the text strings and an accessible string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/init(text:shorttext:))*