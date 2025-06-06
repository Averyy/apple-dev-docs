# ButtonStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of a button.

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
struct ButtonStyleConfiguration
```

## Topics

### Configuring a button’s label
- [let label: ButtonStyleConfiguration.Label](buttonstyleconfiguration/label-swift.property.md)
  A view that describes the effect of pressing the button.
- [ButtonStyleConfiguration.Label](buttonstyleconfiguration/label-swift.struct.md)
  A type-erased label of a button.
### Configuring a button’s interaction state
- [let isPressed: Bool](buttonstyleconfiguration/ispressed.md)
  A Boolean that indicates whether the user is currently pressing the button.
### Defining the button’s purpose
- [let role: ButtonRole?](buttonstyleconfiguration/role.md)
  An optional semantic role that describes the button’s purpose.

## See Also

- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [protocol ButtonStyle](buttonstyle.md)
  A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [protocol PrimitiveButtonStyle](primitivebuttonstyle.md)
  A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [struct PrimitiveButtonStyleConfiguration](primitivebuttonstyleconfiguration.md)
  The properties of a button.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonstyleconfiguration)*