# init(options:locale:order:)

**Framework**: Swift  
**Kind**: init

Creates a `String.Comparator` with the given `CompareOptions` and `Locale`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(options: String.CompareOptions, locale: Locale? = Locale.current, order: SortOrder = .forward)
```

## Parameters

- `options`: The options to use for comparison.
- `locale`: The locale to use for comparison. If  , the   comparison is unlocalized.
- `order`: The initial order to use for ordered comparison.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/comparator/init(options:locale:order:))*