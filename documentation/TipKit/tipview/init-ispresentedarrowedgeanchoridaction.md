# init(_:isPresented:arrowEdge:anchorID:action:)

**Framework**: TipKit  
**Kind**: init

Creates a tip view with an optional arrow.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init<AnchorID>(_ tip: (any Tip)?, isPresented: Binding<Bool>? = nil, arrowEdge: Edge? = nil, anchorID: AnchorID, action: @escaping @MainActor (Tips.Action) -> Void = { _ in }) where Content == AnyTip, AnchorID : Hashable, AnchorID : Sendable
```

#### Discussion

Use a `TipView` when you want to indicate the UI element to which the tip applies, but don’t want to directly anchor the tip view to that element. Use the [`popoverTip(_:arrowEdge:action:)`](https://developer.apple.com/documentation/SwiftUI/View/popoverTip(_:arrowEdge:action:)) to anchor your tip to an element.

## Parameters

- `tip`: The tip to display.
- `isPresented`: A binding that will automatically update to true when a tip is displayed. This value can be changed to temporarily hide or show a currently displayable tip. If this value is  , the view will automatically disappear based on the tip’s status and display rules.
- `arrowEdge`: The edge of the tip view that displays the arrow.
- `anchorID`: The identifier used to read the   of the anchoring view.
- `action`: The closure to perform when the user triggers a tip’s action.

## See Also

- [init((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void)](tipview/init(_:arrowedge:action:).md)
  Creates a tip view with an optional arrow.
- [init((any Tip)?, isPresented: Binding<Bool>?, arrowEdge: Edge?, action: (Tips.Action) -> Void)](tipview/init(_:ispresented:arrowedge:action:).md)
  Creates a tip view with an optional arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipview/init(_:ispresented:arrowedge:anchorid:action:))*