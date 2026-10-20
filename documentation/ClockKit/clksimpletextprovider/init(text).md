# init(text:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a text provider with the specified long form text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(text: String)
```

```objc
+ (instancetype) textProviderWithText:(NSString *) text;
```

#### Return Value

A text provider initialized with the specified content.

## Parameters

- `text`: The text that you want to display. This value is assigned to the [`text`](./text.md) property of your text provider object.

## See Also

### Creating a Text Provider
- [convenience init(text: String, shortText: String?)](./init%28text,shorttext%29.md)
  Creates and returns a text provider with both long and short versions of the text.
- [convenience init(text: String, shortText: String?, accessibilityLabel: String?)](./init%28text,shorttext,accessibilitylabel%29.md)
  Creates and returns a text provider with the text strings and an accessible string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/init(text:))*