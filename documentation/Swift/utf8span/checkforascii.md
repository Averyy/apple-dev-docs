# checkForASCII()

**Framework**: Swift  
**Kind**: method

Do a scan checking for whether the contents are all-ASCII.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func checkForASCII() -> Bool
```

#### Discussion

Updates the `isKnownASCII` bit if contents are all-ASCII.

> **Note**: O(n)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/checkforascii())*