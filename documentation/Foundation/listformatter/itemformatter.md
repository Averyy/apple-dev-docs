# itemFormatter

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An object that formats each item in the list.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var itemFormatter: Formatter? { get set }
```

```objc
@property (copy, nullable) NSFormatter * itemFormatter;
```

#### Discussion

If this property isn’t set, the list formatter falls back to the item’s [`description(withLocale:)`](../nsarray/description%28withlocale%29.md) or [`localizedDescription`](../progress/localizeddescription.md) methods if implemented. If those methods aren’t implemented, the formatter uses [`description`](../../ObjectiveC/nsobjectprotocol/description.md) instead.

## See Also

### Configuring Formatter Options
- [var locale: Locale!](./locale.md)
  The locale to use when formatting items in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatter/itemformatter)*