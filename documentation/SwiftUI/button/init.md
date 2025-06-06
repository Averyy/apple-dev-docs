# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button based on a configuration for a style with a custom appearance and custom interaction behavior.

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
init(_ configuration: PrimitiveButtonStyleConfiguration)
```

#### Discussion

Use this initializer within the [`makeBody(configuration:)`](primitivebuttonstyle/makebody(configuration:).md) method of a [`PrimitiveButtonStyle`](primitivebuttonstyle.md) to create an instance of the button that you want to style. This is useful for custom button styles that modify the current button style, rather than implementing a brand new style.

For example, the following style adds a red border around the button, but otherwise preserves the button’s current style:

```swift
struct RedBorderedButtonStyle: PrimitiveButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        Button(configuration)
            .border(Color.red)
    }
}
```

## Parameters

- `configuration`: A configuration for a style with a custom   appearance and custom interaction behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(_:))*