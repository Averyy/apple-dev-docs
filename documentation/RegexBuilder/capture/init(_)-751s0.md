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
init<W>(_ component: some RegexComponent) where Output == (Substring, W)
```

## Parameters

- `component`: The regex component to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/capture/init(_:)-751s0)*