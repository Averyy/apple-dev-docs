# TipViewStyle

**Framework**: TipKit  
**Kind**: protocol

A type that applies custom appearance to all tips within a view hierarchy.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol TipViewStyle
```

#### Overview

To configure the current style for tips in a view hierarchy, use the [`tipViewStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tipViewStyle(_:)) modifier and specify a type that conforms to `TipViewStyle`.

![An image of a tip view with a custom style.](https://docs-assets.developer.apple.com/published/1d23e6a05e6d5bd02044a8ae7f981218/tipviewstyle_headline-style%402x.png)

Customize the layout and style of your tips by creating a custom `TipViewStyle`:

```swift
struct HeadlineTipViewStyle: TipViewStyle {
    func makeBody(configuration: TipViewStyle.Configuration) -> some View {
        VStack(alignment: .leading) {
            HStack {
                Text("TIP").font(.system(.headline).smallCaps())
                Spacer()
                Button(action: { configuration.tip.invalidate(reason: .tipClosed) }) {
                    Image(systemName: "xmark").scaledToFit()
                }
            }

            Divider().frame(height: 1.0)

            HStack(alignment: .top) {
                configuration.image?
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 48.0, height: 48.0)

                VStack(alignment: .leading, spacing: 8.0) {
                    configuration.title?.font(.headline)
                    configuration.message?.font(.subheadline)

                    ForEach(configuration.actions) { action in
                        Button(action: action.handler) {
                            action.label().foregroundStyle(.blue)
                        }
                    }
                }
            }
        }
    }
}
```

Use the [`tipViewStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/tipViewStyle(_:)) modifier to apply your style to all tips within a view hierarchy:

```swift
struct AddWorkoutView: View {
    var body: some View {
        VStack {
            TipView(AddWorkoutTip())
                .tipViewStyle(HeadlineTipViewStyle())

            Text("Workout Samples")
            WorkoutSampleList()
        }
    }
}
```

For UIKit and AppKit apps, the `viewStyle` property can be used for specifying a custom `TipViewStyle`:

```swift
let addWorkoutTipView = TipUIView(AddWorkoutTip())
addWorkoutTipView.viewStyle = HeadlineTipViewStyle()
addSubview(addWorkoutTipView)
```

## Topics

### Associated Types
- [associatedtype Body : View](tipviewstyle/body.md)
  The user interface element of the tip.
### Instance Methods
- [func makeBody(configuration: Self.Configuration) -> Self.Body](tipviewstyle/makebody(configuration:).md)
  A builder that makes the body of the tip view based on a style configuration.
### Type Aliases
- [TipViewStyle.Configuration](tipviewstyle/configuration.md)
  The tip style’s configuration.
### Type Properties
- [static var miniTip: MiniTipViewStyle](tipviewstyle/minitip.md)
  The default style for a tip view.

## Relationships

### Conforming Types
- [MiniTipViewStyle](minitipviewstyle.md)

## See Also

- [func tipViewStyle(some TipViewStyle) -> some View](../SwiftUI/View/tipViewStyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [struct TipViewStyleConfiguration](tipviewstyleconfiguration.md)
  The container type that holds a tip’s configuration.
- [struct MiniTipViewStyle](minitipviewstyle.md)
  The default style for a TipView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipviewstyle)*