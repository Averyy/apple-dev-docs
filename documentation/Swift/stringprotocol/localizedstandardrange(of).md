# localizedStandardRange(of:)

**Framework**: Swift  
**Kind**: method

Finds and returns the range of the first occurrence of a given string, taking the current locale into account.  Returns `nil` if the string was not found.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func localizedStandardRange<T>(of string: T) -> Range<Self.Index>? where T : StringProtocol
```

#### Discussion

This is the most appropriate method for doing user-level string searches, similar to how searches are done generally in the system.  The search is locale-aware, case and diacritic insensitive.  The exact list of search options applied may change over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/localizedstandardrange(of:))*