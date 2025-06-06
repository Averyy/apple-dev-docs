# formatted(_:)

**Framework**: Swift  
**Kind**: method

Formats the date range using the specified style.

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
func formatted<S>(_ style: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Range<Date>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/range/formatted(_:))*