# init(as:_:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a capture for the given component using the specified reference.

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
init<W, C1>(as reference: Reference<W>, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, W, C1)
```

## Parameters

- `reference`: The reference to use for anything captured by   .
- `componentBuilder`: A builder closure that generates a regex   component to capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/capture/init(as:_:)-4l8eh)*