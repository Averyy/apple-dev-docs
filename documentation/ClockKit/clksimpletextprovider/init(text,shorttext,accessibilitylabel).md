# init(text:shortText:accessibilityLabel:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a text provider with the text strings and an accessible string.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(text: String, shortText: String?, accessibilityLabel: String?)
```

```objc
+ (instancetype) textProviderWithText:(NSString *) text shortText:(NSString *) shortText accessibilityLabel:(NSString *) accessibilityLabel;
```

#### Return Value

A text provider initialized with the specified content.

## Parameters

- `text`: The text that you want to display.
- `shortText`: A shorter version of the value in the `text` parameter that conveys the same information.
- `accessibilityLabel`: A succinct string that identifies the purpose of the text.

## See Also

### Creating a Text Provider
- [convenience init(text: String)](./init%28text%29.md)
  Creates and returns a text provider with the specified long form text.
- [convenience init(text: String, shortText: String?)](./init%28text,shorttext%29.md)
  Creates and returns a text provider with both long and short versions of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/init(text:shorttext:accessibilitylabel:))*