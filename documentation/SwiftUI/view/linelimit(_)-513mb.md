# lineLimit(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the maximum number of lines that text can occupy in this view.

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
func lineLimit(_ number: Int?) -> some View
```

**Other overloads**:

```swift
nonisolated
func lineLimit(_ limit: ClosedRange<Int>) -> some View
```

```swift
nonisolated
func lineLimit(_ limit: PartialRangeFrom<Int>) -> some View
```

```swift
nonisolated
func lineLimit(_ limit: PartialRangeThrough<Int>) -> some View
```

## Return Value

A view that limits the number of lines that [`Text`](../text.md) instances display.

## Discussion

Use this modifier to cap the number of lines that an individual text element can display.

The line limit applies to all [`Text`](../text.md) instances within a hierarchy. For example, an [`HStack`](../hstack.md) with multiple pieces of text longer than three lines caps each piece of text to three lines rather than capping the total number of lines across the [`HStack`](../hstack.md).

In the example below, the modifier limits the very long line in the [`Text`](../text.md) element to the 2 lines that fit within the view’s bounds:

```swift
Text("This is a long string that demonstrates the effect of SwiftUI's lineLimit(:_) operator.")
    .frame(width: 200, height: 200, alignment: .leading)
    .lineLimit(2)
```

![A screenshot showing showing the effect of the line limit operator on](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-view-lineLimit@2x.png)

## Parameters

- `number`: The line limit. If `nil`, no line limit applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/linelimit(_:)-513mb)*