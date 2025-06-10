# modifier(_:)

**Framework**: PermissionKit  
**Kind**: method

Applies a modifier to a view and returns a new view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 26.0+ (Beta)
- watchOS 6.0+

## Declaration

```swift
nonisolated
func modifier<T>(_ modifier: T) -> ModifiedContent<Self, T>
```

#### Discussion

Use this modifier to combine a `View` and a `ViewModifier`, to create a new view. For example, if you create a view modifier for a new kind of caption with blue text surrounded by a rounded rectangle:

```None
struct BorderedCaption: ViewModifier {
    func body(content: Content) -> some View {
        content
            .font(.caption2)
            .padding(10)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 1)
            )
            .foregroundColor(Color.blue)
    }
}
```

You can use [`modifier(_:)`](communicationlimitsbutton/modifier(_:).md) to extend `View` to create new modifier for applying the `BorderedCaption` defined above:

```None
extension View {
    func borderedCaption() -> some View {
        modifier(BorderedCaption())
    }
}
```

Then you can apply the bordered caption to any view:

```None
Image(systemName: "bus")
    .resizable()
    .frame(width:50, height:50)
Text("Downtown Bus")
    .borderedCaption()
```

## Parameters

- `modifier`: The modifier to apply to this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/modifier(_:))*