# cornerRadius(_:antialiased:)

**Framework**: FamilyControls  
**Kind**: method

Clips this view to its bounding frame, with the specified corner radius.

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
func cornerRadius(_ radius: CGFloat, antialiased: Bool = true) -> some View
```

#### Return Value

A view that clips this view to its bounding frame with the specified corner radius.

#### Discussion

By default, a view’s bounding frame only affects its layout, so any content that extends beyond the edges of the frame remains visible. Use `cornerRadius(_:antialiased:)` to hide any content that extends beyond these edges while applying a corner radius.

The following code applies a corner radius of 25 to a text view:

```swift
Text("Rounded Corners")
    .frame(width: 175, height: 75)
    .foregroundColor(Color.white)
    .background(Color.black)
    .cornerRadius(25)
```

## Parameters

- `antialiased`: A Boolean value that indicates whether the   rendering system applies smoothing to the edges of the clipping   rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/cornerradius(_:antialiased:))*