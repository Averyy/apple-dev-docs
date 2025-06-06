# commonPrefix(with:options:)

**Framework**: Swift  
**Kind**: method

Returns a string containing characters this string and the given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.

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
func commonPrefix<T>(with aString: T, options: String.CompareOptions = []) -> String where T : StringProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/commonprefix(with:options:))*