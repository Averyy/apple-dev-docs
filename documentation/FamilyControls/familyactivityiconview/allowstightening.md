# allowsTightening(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets whether text in this view can compress the space between characters when necessary to fit text in a line.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func allowsTightening(_ flag: Bool) -> some View
```

#### Return Value

A view that can compress the space between characters when necessary to fit text in a line.

#### Discussion

Use `allowsTightening(_:)` to enable the compression of inter-character spacing of text in a view to try to fit the text in the view’s bounds.

In the example below, two identically configured text views show the effects of `allowsTightening(_:)` on the compression of the spacing between characters:

```swift
VStack {
    Text("This is a wide text element")
        .font(.body)
        .frame(width: 200, height: 50, alignment: .leading)
        .lineLimit(1)
        .allowsTightening(true)

    Text("This is a wide text element")
        .font(.body)
        .frame(width: 200, height: 50, alignment: .leading)
        .lineLimit(1)
        .allowsTightening(false)
}
```

## Parameters

- `flag`: A Boolean value that indicates whether the space   between characters compresses when necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/allowstightening(_:))*