# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a toggle based on a toggle style configuration.

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
init(_ configuration: ToggleStyleConfiguration)
```

#### Discussion

You can use this initializer within the [`makeBody(configuration:)`](togglestyle/makebody(configuration:).md) method of a [`ToggleStyle`](togglestyle.md) to create an instance of the styled toggle. This is useful for custom toggle styles that only modify the current toggle style, as opposed to implementing a brand new style.

For example, the following style adds a red border around the toggle, but otherwise preserves the toggle’s current style:

```swift
struct RedBorderToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Toggle(configuration)
            .padding()
            .border(.red)
    }
}
```

## Parameters

- `configuration`: The properties of the toggle, including a   label and a binding to the toggle’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toggle/init(_:))*