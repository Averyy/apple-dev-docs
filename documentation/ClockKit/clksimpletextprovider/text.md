# text

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The long version of text that you want to display.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var text: String { get set }
```

```objc
@property (nonatomic, copy) NSString * text;
```

#### Discussion

The long version of the text is the preferred version and is used whenever possible.

## See Also

### Getting the Text
- [var shortText: String?](./shorttext.md)
  A shorter version of the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimpletextprovider/text)*