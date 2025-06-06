# localizedStandardContains(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the string contains the given string, taking the current locale into account.

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
func localizedStandardContains<T>(_ string: T) -> Bool where T : StringProtocol
```

#### Discussion

This is the most appropriate method for doing user-level string searches, similar to how searches are done generally in the system.  The search is locale-aware, case and diacritic insensitive.  The exact list of search options applied may change over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/localizedstandardcontains(_:))*