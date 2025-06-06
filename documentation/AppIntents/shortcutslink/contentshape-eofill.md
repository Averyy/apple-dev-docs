# contentShape(_:eoFill:)

**Framework**: App Intents  
**Kind**: method

Defines the content shape for hit testing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func contentShape<S>(_ shape: S, eoFill: Bool = false) -> some View where S : Shape
```

#### Return Value

A view that uses the given shape for hit testing.

## Parameters

- `shape`: The hit testing shape for the view.
- `eoFill`: A Boolean that indicates whether the shape is interpreted   with the even-odd winding number rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/contentshape(_:eofill:))*