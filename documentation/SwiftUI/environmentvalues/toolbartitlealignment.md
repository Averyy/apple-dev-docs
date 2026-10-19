# toolbarTitleAlignment

**Framework**: SwiftUI  
**Kind**: property

The alignment the navigation bar resolved for its title.

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- tvOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
var toolbarTitleAlignment: ToolbarTitleAlignment { get set }
```

#### Discussion

Read this from a custom title view (like a `ToolbarItem` using the [`title`](toolbaritemplacement/title.md) placement) to lay out its content to match the alignment the system chose.

When the system has resolved an alignment for the title, this reports that concrete alignment, [`leading`](toolbartitlealignment/leading.md) or [`center`](toolbartitlealignment/center.md), even when you have not set a preference with [`toolbarTitleAlignment(_:)`](view/toolbartitlealignment(_:).md). Otherwise it is [`automatic`](toolbartitlealignment/automatic.md).

```swift
struct AlbumTitle: View {
    @Environment(\.toolbarTitleAlignment) private var alignment

    var body: some View {
        VStack(alignment: alignment == .leading ? .leading : .center) {
            Text("Library")
            Text("42 Albums").font(.caption)
        }
    }
}
```

Use this to align content within the size your view already reported, not to decide that size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/toolbartitlealignment)*