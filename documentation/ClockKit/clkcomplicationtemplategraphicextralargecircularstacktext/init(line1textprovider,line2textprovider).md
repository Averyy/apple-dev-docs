# init(line1TextProvider:line2TextProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template with two rows of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
init(line1TextProvider: CLKTextProvider, line2TextProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithLine1TextProvider:(CLKTextProvider *) line1TextProvider line2TextProvider:(CLKTextProvider *) line2TextProvider;
```

## Parameters

- `line1TextProvider`: The text provider for the top row of text. The template supports multicolored text from this text provider.
- `line2TextProvider`: The text provider for the bottom row of text. The template supports multicolored text from this text provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularstacktext/init(line1textprovider:line2textprovider:))*