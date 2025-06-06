# init(_:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a capture for the given component.

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
init<W, C1, C2, C3, C4, C5, C6, C7>(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, W, C1, C2, C3, C4, C5, C6, C7)
```

## Parameters

- `componentBuilder`: A builder closure that generates a   regex component to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/capture/init(_:)-8hde2)*