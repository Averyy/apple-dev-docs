# role

**Framework**: SwiftUI  
**Kind**: property

An optional semantic role describing the button’s purpose.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let role: ButtonRole?
```

#### Discussion

A value of `nil` means that the Button has no assigned role. If the button does have a role, use it to make adjustments to the button’s appearance. The following example shows a custom style that uses bold text when the role is [`cancel`](buttonrole/cancel.md), [`red`](shapestyle/red.md) text when the role is [`destructive`](buttonrole/destructive.md), and adds no special styling otherwise:

```swift
struct MyButtonStyle: PrimitiveButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .onTapGesture {
                configuration.trigger()
            }
            .font(
                configuration.role == .cancel ? .title2.bold() : .title2)
            .foregroundColor(
                configuration.role == .destructive ? Color.red : nil)
    }
}
```

You can create one of each button using this style to see the effect:

```swift
VStack(spacing: 20) {
    Button("Cancel", role: .cancel) {}
    Button("Delete", role: .destructive) {}
    Button("Continue") {}
}
.buttonStyle(MyButtonStyle())
```

![A screenshot of three buttons stacked vertically. The first says](https://docs-assets.developer.apple.com/published/fc5f574e801c90d4bf376b38c19a601d/PrimitiveButtonStyleConfiguration-role-1%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyleconfiguration/role)*