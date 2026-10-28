# aspectRatio(_:contentMode:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Constrains this view’s dimensions to the aspect ratio of the given size.

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
func aspectRatio(_ aspectRatio: CGSize, contentMode: ContentMode) -> some View
```

**Other overloads**:

```swift
nonisolated
func aspectRatio(_ aspectRatio: CGFloat? = nil, contentMode: ContentMode) -> some View
```

## Return Value

A view that constrains this view’s dimensions to `aspectRatio`, using `contentMode` as its scaling algorithm.

## Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an aspect ratio specified by a [`CGSize`](../../CoreFoundation/cgsize.md).

If this view is resizable, the resulting view uses `aspectRatio` as its own aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height ratio, and scales to fill its frame:

```swift
Ellipse()
    .fill(Color.purple)
    .aspectRatio(CGSize(width: 3, height: 4), contentMode: .fill)
    .frame(width: 200, height: 200)
    .border(Color(white: 0.75))
```

![A view showing a purple ellipse that has a 3:4 width-to-height ratio,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-aspectRatio@2x.png)

## Parameters

- `aspectRatio`: A size that specifies the ratio of width to height to use for the resulting view.
- `contentMode`: A flag indicating whether this view should fit or fill the parent context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/aspectratio(_:contentmode:)-771ow)*