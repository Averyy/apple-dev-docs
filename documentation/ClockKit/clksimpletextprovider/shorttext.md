# shortText

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A shorter version of the text.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var shortText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * shortText;
```

#### Discussion

The text provider uses this string before attempting to truncate the long version of your text. In this string, you might use abbreviations instead of full words or include only the most important word or characters.

## See Also

### Getting the Text
- [var text: String](./text.md)
  The long version of text that you want to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/shorttext)*