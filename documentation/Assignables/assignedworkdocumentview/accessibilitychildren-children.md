# accessibilityChildren(children:)

**Framework**: Assignables  
**Kind**: method

Replaces the existing accessibility element’s children with one or more new synthetic accessibility elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityChildren<V>(@ViewBuilder children: () -> V) -> some View where V : View
```

#### Discussion

Use this modifier to replace an existing element’s children with one or more new synthetic accessibility elements you provide. This allows for synthetic, non-visual accessibility elements to be set as children of a visual accessibility element.

SwiftUI creates an accessibility container implicitly when needed. If an accessibility element already exists, the framework converts it into an accessibility container.

In the  example below, a `Canvas` displays a graph of vertical bars that don’t have any inherent accessibility elements. You make the view accessible by adding the [`accessibilityChildren(children:)`](assignedworkdocumentview/accessibilitychildren(children:).md) modifier with views whose accessibility elements represent the values of each bar drawn in the canvas:

```None
var body: some View {
    Canvas { context, size in
        // Draw Graph
        for data in dataSet {
            let path = Path(
                roundedRect: CGRect(
                    x: (size.width / CGFloat(dataSet.count))
                    * CGFloat(data.week),
                    y: 0,
                    width: size.width / CGFloat(dataSet.count),
                    height: CGFloat(data.lines),
                cornerRadius: 5)
            context.fill(path, with: .color(.blue))
        }
        // Draw Axis and Labels
        ...
    }
    .accessibilityLabel("Lines of Code per Week")
    .accessibilityChildren {
        HStack {
            ForEach(dataSet) { data in
                RoundedRectangle(cornerRadius: 5)
                    .accessibilityLabel("Week \(data.week)")
                    .accessibilityValue("\(data.lines) lines")
            }
        }
    }
}
```

SwiftUI hides any views that you provide with the `children` parameter, then the framework uses the views to generate the accessibility elements.

## Parameters

- `children`: A   that represents the replacement   child views the framework uses to generate accessibility elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/accessibilitychildren(children:))*