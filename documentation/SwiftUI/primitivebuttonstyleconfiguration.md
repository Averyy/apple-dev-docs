# PrimitiveButtonStyleConfiguration

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
struct PrimitiveButtonStyleConfiguration
```

## Topics

### Configuring a button’s label
- [let label: PrimitiveButtonStyleConfiguration.Label](primitivebuttonstyleconfiguration/label-swift.property.md)
  A view that describes the effect of calling the button’s action.
- [PrimitiveButtonStyleConfiguration.Label](primitivebuttonstyleconfiguration/label-swift.struct.md)
  A type-erased label of a button.
### Initiating a button’s action
- [func trigger()](primitivebuttonstyleconfiguration/trigger.md)
  Performs the button’s action.
### Defining the button’s purpose
- [let role: ButtonRole?](primitivebuttonstyleconfiguration/role.md)
  An optional semantic role describing the button’s purpose.

## See Also

- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [protocol ButtonStyle](buttonstyle.md)
  A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [struct ButtonStyleConfiguration](buttonstyleconfiguration.md)
  The properties of a button.
- [protocol PrimitiveButtonStyle](primitivebuttonstyle.md)
  A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyleconfiguration)*