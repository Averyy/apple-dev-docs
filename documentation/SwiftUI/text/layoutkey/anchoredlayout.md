# Text.LayoutKey.AnchoredLayout

**Framework**: SwiftUI  
**Kind**: struct

The layout of one text view, together with an anchor for the position of that view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct AnchoredLayout
```

#### Overview

[`Text.LayoutKey`](text/layoutkey.md) collects one of these values for every text view in the subtree you query. Read [`layout`](text/layoutkey/anchoredlayout/layout.md) to inspect the lines, runs, and glyphs the text produced, and resolve [`origin`](text/layoutkey/anchoredlayout/origin.md) in a [`GeometryProxy`](geometryproxy.md) to place something of your own next to the text:

```swift
ZStack {
    Text("Hello, world")
}
.overlayPreferenceValue(Text.LayoutKey.self) { layouts in
    GeometryReader { proxy in
        ForEach(0..<layouts.count, id: \.self) { index in
            Underline(layout: layouts[index].layout)
                .position(proxy[layouts[index].origin])
        }
    }
}
```

The anchor matters because a text view reports its layout in its own coordinate space. Resolving the anchor converts that origin into the space of the view reading the preference.

## Topics

### Instance Properties
- [var layout: Text.Layout](text/layoutkey/anchoredlayout/layout.md)
  The text layout value.
- [var origin: Anchor<CGPoint>](text/layoutkey/anchoredlayout/origin.md)
  The origin of the text layout.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layoutkey/anchoredlayout)*