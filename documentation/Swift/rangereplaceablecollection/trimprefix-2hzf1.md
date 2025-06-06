# trimPrefix(_:)

**Framework**: Swift  
**Kind**: method

Removes the initial elements matching the regex from the start of this collection, if the initial elements match, using the given closure to create the regex.

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
mutating func trimPrefix(@RegexComponentBuilder _ content: () -> some RegexComponent)
```

## Parameters

- `content`: A closure that returns the regex to search for   at the start of this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/trimprefix(_:)-2hzf1)*