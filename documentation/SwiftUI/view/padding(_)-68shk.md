# padding(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a specific padding amount to each edge of this view.

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
func padding(_ length: CGFloat) -> some View
```

**Other overloads**:

```swift
nonisolated
func padding(_ insets: EdgeInsets) -> some View
```

## Return Value

A view that’s padded by the amount you specify.

## Discussion

Use this modifier to add padding all the way around a view.

```swift
VStack {
    Text("Text padded by 10 points on each edge.")
        .padding(10)
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

The order in which you apply modifiers matters. The example above applies the padding before applying the border to ensure that the border encompasses the padded region:

![A screenshot of two text strings arranged vertically, each surrounded](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-padding-1-iOS@2x.png)

To independently control the amount of padding for each edge, use [`padding(_:)`](./padding%28_%29-6pgqq.md). To pad a select set of edges by the same amount, use [`padding(_:_:)`](./padding%28_,_%29.md).

## Parameters

- `length`: The amount, given in points, to pad this view on all edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/padding(_:)-68shk)*