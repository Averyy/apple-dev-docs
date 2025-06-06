# trimmingPrefix(_:)

**Framework**: Swift  
**Kind**: method

Returns a new collection of the same type by removing the initial elements that matches the given regex.

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
func trimmingPrefix(_ regex: some RegexComponent) -> Self.SubSequence
```

#### Return Value

A collection containing the elements that does not match `regex` from the start.

## Parameters

- `regex`: The regex to remove from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/trimmingprefix(_:)-1luge)*