# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a group box based on a style configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ configuration: GroupBoxStyleConfiguration)
```

#### Discussion

Use this initializer within the [`makeBody(configuration:)`](groupboxstyle/makebody(configuration:).md) method of a [`GroupBoxStyle`](groupboxstyle.md) instance to create a styled group box, with customizations, while preserving its existing style.

The following example adds a pink border around the group box, without overriding its current style:

```swift
struct PinkBorderGroupBoxStyle: GroupBoxStyle {
    func makeBody(configuration: Configuration) -> some View {
        GroupBox(configuration)
            .border(Color.pink)
    }
}
```

## Parameters

- `configuration`: The properties of the group box instance being created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox/init(_:))*