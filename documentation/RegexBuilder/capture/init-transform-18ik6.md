# init(_:transform:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a capture for the given component, transforming with the given closure.

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
init<W, C1, C2, C3, C4, NewCapture>(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent, transform: @escaping (W) throws -> NewCapture) where Output == (Substring, NewCapture, C1, C2, C3, C4)
```

## Parameters

- `componentBuilder`: A builder closure that generates a regex   component to capture.
- `transform`: A closure that takes the substring matched by    and returns a new value to capture. If    throws an error, matching is abandoned and the error is returned   to the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/capture/init(_:transform:)-18ik6)*