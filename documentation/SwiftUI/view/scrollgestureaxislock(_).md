# scrollGestureAxisLock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets whether scrollable views within this view lock each scroll gesture to its predominant axis.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func scrollGestureAxisLock(_ lock: ScrollGestureAxisLock) -> some View
```

## Return Value

A view that uses the specified locking behavior.

## Discussion

Use [`disabled`](../scrollgestureaxislock/disabled.md) so that people can pan diagonally across content like a canvas or a map. Use [`directional`](../scrollgestureaxislock/directional.md) to keep scrolling aligned vertically or horizontally, as in a spreadsheet.

For example, this scroll view lets people pan a floor plan freely in any direction:

```swift
ScrollView([.horizontal, .vertical]) {
    Image("FloorPlan")
}
.scrollGestureAxisLock(.disabled)
```

The locking behavior applies to the scroll views in this view hierarchy that are configured to scroll along both axes. Scroll views configured to scroll along a single axis, such as a [`List`](../list.md), ignore the locking behavior and pass it to the scroll views they contain. A scroll view configured to scroll along both axes doesn’t pass the locking behavior to nested child scroll views.

Pass [`automatic`](../scrollgestureaxislock/automatic.md) to use the platform’s default behavior.

## Parameters

- `lock`: The locking behavior to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrollgestureaxislock(_:))*