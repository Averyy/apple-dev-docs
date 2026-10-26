# init(text:shortText:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a text provider with both long and short versions of the text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(text: String, shortText: String?)
```

```objc
+ (instancetype) textProviderWithText:(NSString *) text shortText:(NSString *) shortText;
```

#### Return Value

A text provider initialized with the specified content.

## Parameters

- `text`: The text that you want to display. This value is assigned to the [`text`](./text.md) property of your text provider object.
- `shortText`: A shorter version of the value in the `text` parameter that conveys the same information.

## See Also

### Creating a Text Provider
- [convenience init(text: String)](./init%28text%29.md)
  Creates and returns a text provider with the specified long form text.
- [convenience init(text: String, shortText: String?, accessibilityLabel: String?)](./init%28text,shorttext,accessibilitylabel%29.md)
  Creates and returns a text provider with the text strings and an accessible string.
- [- initWithText:](./initwithtext_.md)
  Creates and returns a text provider with the specified long form text.
- [- initWithText:shortText:](./initwithtext_shorttext_.md)
  Creates and returns a text provider with both long and short versions of the text.
- [- initWithText:shortText:accessibilityLabel:](./initwithtext_shorttext_accessibilitylabel_.md)
  Creates and returns a text provider with the text strings and an accessible string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/init(text:shorttext:))*