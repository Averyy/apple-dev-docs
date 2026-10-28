# initWithText:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a text provider with the specified long form text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithText:(NSString *) text;
```

## Return Value

A text provider initialized with the specified content.

## Parameters

- `text`: The text that you want to display. This value is assigned to the [`text`](./text.md) property of your text provider object.

## See Also

### Creating a Text Provider
- [convenience init(text: String)](./init%28text%29.md)
  Creates and returns a text provider with the specified long form text.
- [convenience init(text: String, shortText: String?)](./init%28text,shorttext%29.md)
  Creates and returns a text provider with both long and short versions of the text.
- [- initWithText:shortText:](./initwithtext_shorttext_.md)
  Creates and returns a text provider with both long and short versions of the text.
- [convenience init(text: String, shortText: String?, accessibilityLabel: String?)](./init%28text,shorttext,accessibilitylabel%29.md)
  Creates and returns a text provider with the text strings and an accessible string.
- [- initWithText:shortText:accessibilityLabel:](./initwithtext_shorttext_accessibilitylabel_.md)
  Creates and returns a text provider with the text strings and an accessible string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/initwithtext:)*