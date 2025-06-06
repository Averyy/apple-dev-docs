# init(_:transform:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a capture for the given component, attempting to transform with the given closure.

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
init<W, NewCapture>(_ component: some RegexComponent, transform: @escaping (W) throws -> NewCapture?) where Output == (Substring, NewCapture)
```

## Parameters

- `component`: The regex component to capture.
- `transform`: A closure that takes the substring matched by    and returns a new value to capture, or   if   matching should proceed, backtracking if allowed. If    throws an error, matching is abandoned and the error is returned   to the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/trycapture/init(_:transform:)-4ctec)*