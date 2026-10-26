# init(line1TextProvider:line2TextProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template that has two small rows of text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

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

## See Also

### Creating the Template
- [+ templateWithLine1TextProvider:line2TextProvider:](./templatewithline1textprovider_line2textprovider_.md)
  Returns a new template that has two small rows of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularstacktext/init(line1textprovider:line2textprovider:))*