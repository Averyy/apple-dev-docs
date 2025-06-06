# init(_:_:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a regex component that matches the given component one or more times.

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
init<W, C1, C2, C3>(_ component: some RegexComponent, _ behavior: RegexRepetitionBehavior? = nil) where Output == (Substring, C1, C2, C3)
```

## Parameters

- `component`: The regex component.
- `behavior`: The repetition behavior to use when repeating    in the match. If   is  , the default   repetition behavior is used, which can be changed from    by calling   on the resulting   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/oneormore/init(_:_:)-9f4e8)*