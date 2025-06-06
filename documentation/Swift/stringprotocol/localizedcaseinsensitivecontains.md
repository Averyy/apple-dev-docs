# localizedCaseInsensitiveContains(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the given string is non-empty and contained within this string by case-insensitive, non-literal search, taking into account the current locale.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func localizedCaseInsensitiveContains<T>(_ other: T) -> Bool where T : StringProtocol
```

#### Discussion

Locale-independent case-insensitive operation, and other needs, can be achieved by calling `range(of:options:range:locale:)`.

Equivalent to:

```swift
range(of: other, options: .caseInsensitiveSearch,
      locale: Locale.current) != nil
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/localizedcaseinsensitivecontains(_:))*