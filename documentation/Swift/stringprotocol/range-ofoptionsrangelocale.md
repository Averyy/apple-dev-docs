# range(of:options:range:locale:)

**Framework**: Swift  
**Kind**: method

Finds and returns the range of the first occurrence of a given string within a given range of the `String`, subject to given options, using the specified locale, if any.

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
func range<T>(of aString: T, options mask: String.CompareOptions = [], range searchRange: Range<Self.Index>? = nil, locale: Locale? = nil) -> Range<Self.Index>? where T : StringProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/range(of:options:range:locale:))*