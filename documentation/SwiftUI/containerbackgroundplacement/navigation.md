# navigation

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A background placement inside a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- watchOS 10.0+

## Declaration

```swift
static let navigation: ContainerBackgroundPlacement
```

#### Discussion

For translucent backgrounds in a navigation split view, combine this placement with [`navigationSplitView`](./navigationsplitview.md).

```swift
NavigationSplitView {
     … sidebar …
    .containerBackground(.thinMaterial, for: .navigation)
    .containerBackground(Color.green, for: .navigationSplitView)
} detail: {
    // … detail …
    .containerBackground(.thickMaterial, for: .navigation)
}
```

## See Also

### Getting placements
- [static let tabView: ContainerBackgroundPlacement](./tabview.md)
  A background placement inside a [`TabView`](../tabview.md).
- [static let widget: ContainerBackgroundPlacement](./widget.md)
  The container background placement for a widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/containerbackgroundplacement/navigation)*