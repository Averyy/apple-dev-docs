# firstRange(of:)

**Framework**: Swift  
**Kind**: method

Finds and returns the range of the first occurrence of a given regex within the collection.

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
func firstRange(of regex: some RegexComponent) -> Range<Self.Index>?
```

#### Return Value

A range in the collection of the first occurrence of `regex`. Returns `nil` if `regex` is not found.

## Parameters

- `regex`: The regex to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/firstrange(of:)-1di7b)*