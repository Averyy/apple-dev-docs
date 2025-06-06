# init(_:_:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a regex component that matches the given component zero or one times.

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
init<W, C1>(_ component: some RegexComponent, _ behavior: RegexRepetitionBehavior? = nil) where Output == (Substring, C1?)
```

## Parameters

- `component`: The regex component.
- `behavior`: The repetition behavior to use when repeating    in the match. If   is  , the default   repetition behavior is used, which can be changed from    by calling   on the resulting   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/optionally/init(_:_:)-9wu1h)*