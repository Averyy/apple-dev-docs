# sizeThatFits(_:nsView:context:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Given a proposed size, returns the preferred size of the composite view.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency func sizeThatFits(_ proposal: ProposedViewSize, nsView: Self.NSViewType, context: Self.Context) -> CGSize?
```

#### Return Value

The composite size of the represented view controller. Returning a value of `nil` indicates that the system should use the default sizing algorithm.

#### Discussion

This method may be called more than once with different proposed sizes during the same layout pass. SwiftUI views choose their own size, so one of the values returned from this function will always be used as the actual size of the composite view.

## Parameters

- `proposal`: The proposed size for the view.
- `nsView`: Your custom view object.
- `context`: A context structure containing information about the   current state of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentable/sizethatfits(_:nsview:context:))*