# buttonStyle(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func buttonStyle<S>(_ style: S) -> some View where S : PrimitiveButtonStyle
```

#### Discussion

Use this modifier to set a specific style for button instances within a view:

```None
HStack {
    Button("Sign In", action: signIn)
    Button("Register", action: register)
}
.buttonStyle(.bordered)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/buttonstyle(_:)-87weh)*