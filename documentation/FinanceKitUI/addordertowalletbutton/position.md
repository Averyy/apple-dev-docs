# position(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Positions the center of this view at the specified point in its parent’s coordinate space.

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
func position(_ position: CGPoint) -> some View
```

#### Return Value

A view that fixes the center of this view at `position`.

#### Discussion

Use the `position(_:)` modifier to place the center of a view at a specific coordinate in the parent view using a [`CGPoint`](https://developer.apple.com/documentation/CoreFoundation/CGPoint) to specify the `x` and `y` offset.

```None
Text("Position by passing a CGPoint()")
    .position(CGPoint(x: 175, y: 100))
    .border(Color.gray)
```

## Parameters

- `position`: The point at which to place the center of this   view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/position(_:))*