# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Available when `Label` conforms to `View` and `CurrentValueLabel` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource) where Label == Text
```

```swift
nonisolated
init(_ progress: Progress) where Label == EmptyView, CurrentValueLabel == EmptyView
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey) where Label == Text
```

```swift
nonisolated
init<S>(_ title: S) where Label == Text, S : StringProtocol
```

## Discussion

You can use this initializer within the [`makeBody(configuration:)`](../progressviewstyle/makebody%28configuration%29.md) method of a [`ProgressViewStyle`](../progressviewstyle.md) to create an instance of the styled progress view. This is useful for custom progress view styles that only modify the current progress view style, as opposed to implementing a brand new style. Because this modifier style can’t know how the current style represents progress, avoid making assumptions about the view’s contents, such as whether it uses bars or other shapes.

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

![Two horizontal progress views, one at 25 percent complete and the](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/ProgressView-4-macOS@2x.png)

> **Note**: Progress views in widgets don’t apply custom styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:)-9dmp3)*