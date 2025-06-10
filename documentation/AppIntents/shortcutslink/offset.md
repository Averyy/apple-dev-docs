# offset(_:)

**Framework**: App Intents  
**Kind**: method

Offset this view by the horizontal and vertical amount specified in the offset parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func offset(_ offset: CGSize) -> some View
```

#### Return Value

A view that offsets this view by `offset`.

#### Discussion

Use `offset(_:)` to shift the displayed contents by the amount specified in the `offset` parameter.

The original dimensions of the view aren’t changed by offsetting the contents; in the example below the gray border drawn by this view surrounds the original position of the text:

```swift
Text("Offset by passing CGSize()")
    .border(Color.green)
    .offset(CGSize(width: 20, height: 25))
    .border(Color.gray)
```

## Parameters

- `offset`: The distance to offset this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/offset(_:))*