# itemFormatter

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

If this property isn’t set, the list formatter falls back to the item’s [`description(withLocale:)`](nsarray/description(withlocale:).md) or [`localizedDescription`](progress/localizeddescription.md) methods if implemented. If those methods aren’t implemented, the formatter uses [`description`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/description) instead.

## See Also

- [var locale: Locale!](listformatter/locale.md)
  The locale to use when formatting items in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatter/itemformatter)*