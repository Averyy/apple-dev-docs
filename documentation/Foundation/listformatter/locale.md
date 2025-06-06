# locale

**Framework**: Foundation  
**Kind**: property

The locale to use when formatting items in the list.

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
var locale: Locale! { get set }
```

#### Discussion

The default value is [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md).

## See Also

- [var itemFormatter: Formatter?](listformatter/itemformatter.md)
  An object that formats each item in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatter/locale)*