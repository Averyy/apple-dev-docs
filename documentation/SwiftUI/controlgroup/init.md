# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a control group based on a style configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ configuration: ControlGroupStyleConfiguration)
```

#### Discussion

Use this initializer within the [`makeBody(configuration:)`](controlgroupstyle/makebody(configuration:).md) method of a [`ControlGroupStyle`](controlgroupstyle.md) instance to create an instance of the control group being styled. This is useful for custom control group styles that modify the current control group style.

For example, the following code creates a new, custom style that places a red border around the current control group:

```swift
struct RedBorderControlGroupStyle: ControlGroupStyle {
    func makeBody(configuration: Configuration) -> some View {
        ControlGroup(configuration)
            .border(Color.red)
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup/init(_:))*