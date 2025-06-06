# contains(_:)

**Framework**: Swift  
**Kind**: method

Returns `true` if `other` is non-empty and contained within `self` by case-sensitive, non-literal search. Otherwise, returns `false`.

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
func contains<T>(_ other: T) -> Bool where T : StringProtocol
```

#### Discussion

Equivalent to `self.range(of: other) != nil`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/contains(_:)-40kbf)*