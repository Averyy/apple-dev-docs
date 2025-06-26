# lineLimit(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the maximum number of lines that text can occupy in this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func lineLimit(_ number: Int?) -> some View
```

#### Return Value

A view that limits the number of lines that `Text` instances display.

#### Discussion

Use this modifier to cap the number of lines that an individual text element can display.

The line limit applies to all `Text` instances within a hierarchy. For example, an `HStack` with multiple pieces of text longer than three lines caps each piece of text to three lines rather than capping the total number of lines across the `HStack`.

In the example below, the modifier limits the very long line in the `Text` element to the 2 lines that fit within the view’s bounds:

```swift
Text("This is a long string that demonstrates the effect of SwiftUI's lineLimit(:_) operator.")
    .frame(width: 200, height: 200, alignment: .leading)
    .lineLimit(2)
```

## Parameters

- `number`: The line limit. If  , no line limit applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/linelimit(_:)-4uo7l)*