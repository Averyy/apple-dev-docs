# firstMatch(of:)

**Framework**: Swift  
**Kind**: method

Returns the first match of the specified regex within the collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func firstMatch<Output>(of r: some RegexComponent) -> Regex<Output>.Match?
```

#### Return Value

The first match of `regex` in the collection, or `nil` if there isn’t a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/firstmatch(of:)-7m8f4)*