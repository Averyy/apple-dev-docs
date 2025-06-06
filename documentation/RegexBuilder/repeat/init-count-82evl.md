# init(_:count:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a regex component that matches the given component repeated the specified number of times.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(_ component: some RegexComponent, count: Int) where Output == Substring
```

## Parameters

- `component`: The regex component to repeat.
- `count`: The number of times to repeat  .   must   be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/repeat/init(_:count:)-82evl)*