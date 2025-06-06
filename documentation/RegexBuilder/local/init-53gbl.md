# init(_:)

**Framework**: RegexBuilder  
**Kind**: init

Creates an atomic group with the given regex component.

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
init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)
```

## Parameters

- `componentBuilder`: A builder closure that generates a   regex component to wrap in an atomic group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/local/init(_:)-53gbl)*