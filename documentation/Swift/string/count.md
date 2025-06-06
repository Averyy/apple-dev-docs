# count

**Framework**: Swift  
**Kind**: property

The number of characters in a string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var count: Int { get }
```

#### Discussion

To check whether a string is empty, use its `isEmpty` property instead of comparing `count` to zero.

> **Note**: O(n), where n is the length of the string.

## See Also

- [var isEmpty: Bool](string/isempty.md)
  A Boolean value indicating whether a string has no characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/count)*