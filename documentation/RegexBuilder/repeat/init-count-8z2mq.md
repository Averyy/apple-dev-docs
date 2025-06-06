# init(count:_:)

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
init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(count: Int, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?, C8?, C9?, C10?)
```

## Parameters

- `count`: The number of times to repeat  .   must   be greater than or equal to zero.
- `componentBuilder`: A builder closure that creates the regex   component to repeat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/repeat/init(count:_:)-8z2mq)*