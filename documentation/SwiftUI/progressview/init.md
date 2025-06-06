# init(_:)

**Framework**: Swiftui  
**Kind**: init

Creates a progress view based on a style configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(_ configuration: ProgressViewStyleConfiguration) where Label == ProgressViewStyleConfiguration.Label, CurrentValueLabel == ProgressViewStyleConfiguration.CurrentValueLabel
```

#### Discussion

You can use this initializer within the [`makeBody(configuration:)`](progressviewstyle/makebody(configuration:).md) method of a [`ProgressViewStyle`](progressviewstyle.md) to create an instance of the styled progress view. This is useful for custom progress view styles that only modify the current progress view style, as opposed to implementing a brand new style. Because this modifier style can’t know how the current style represents progress, avoid making assumptions about the view’s contents, such as whether it uses bars or other shapes.

The following example shows a style that adds a rounded pink border to a progress view, but otherwise preserves the progress view’s current style:

```swift
struct PinkBorderedProgressViewStyle: ProgressViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        ProgressView(configuration)
            .padding(4)
            .border(.pink, width: 3)
            .cornerRadius(4)
    }
}
```

![Two horizontal progress views, one at 25 percent complete and the](https://docs-assets.developer.apple.com/published/dc98a460b4d5e6b5babf527056cf7298/ProgressView-4-macOS%402x.png)

> **Note**: Progress views in widgets don’t apply custom styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:))*