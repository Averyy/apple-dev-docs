# offset(x:y:)

**Framework**: DeviceActivity  
**Kind**: method

Offset this view by the specified horizontal and vertical distances.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func offset(x: CGFloat = 0, y: CGFloat = 0) -> some View
```

#### Return Value

A view that offsets this view by `x` and `y`.

#### Discussion

Use `offset(x:y:)` to shift the displayed contents by the amount specified in the `x` and `y` parameters.

The original dimensions of the view aren’t changed by offsetting the contents; in the example below the gray border drawn by this view surrounds the original position of the text:

```swift
Text("Offset by passing horizontal & vertical distance")
    .border(Color.green)
    .offset(x: 20, y: 50)
    .border(Color.gray)
```

## Parameters

- `x`: The horizontal distance to offset this view.
- `y`: The vertical distance to offset this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/offset(x:y:))*