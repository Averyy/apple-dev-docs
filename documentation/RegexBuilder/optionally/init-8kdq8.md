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
init(_ behavior: RegexRepetitionBehavior? = nil, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == Substring
```

## Parameters

- `behavior`: The repetition behavior to use when repeating    in the match. If   is  , the default   repetition behavior is used, which can be changed from    by calling   on the resulting   .
- `componentBuilder`: A builder closure that generates a regex   component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/optionally/init(_:_:)-8kdq8)*