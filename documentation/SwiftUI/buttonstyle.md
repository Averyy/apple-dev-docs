# ButtonStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.

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
@MainActor
@preconcurrency protocol ButtonStyle
```

#### Overview

To configure the current button style for a view hierarchy, use the [`buttonStyle(_:)`](view/buttonstyle(_:).md) modifier. Specify a style that conforms to `ButtonStyle` when creating a button that uses the standard button interaction behavior defined for each platform. To create a button with custom interaction behavior, use [`PrimitiveButtonStyle`](primitivebuttonstyle.md) instead.

## Topics

### Custom button styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](buttonstyle/makebody(configuration:).md)
  Creates a view that represents the body of a button.
- [ButtonStyle.Configuration](buttonstyle/configuration.md)
  The properties of a button.
- [associatedtype Body : View](buttonstyle/body.md)
  A view that represents the body of a button.

## See Also

- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [struct ButtonStyleConfiguration](buttonstyleconfiguration.md)
  The properties of a button.
- [protocol PrimitiveButtonStyle](primitivebuttonstyle.md)
  A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [struct PrimitiveButtonStyleConfiguration](primitivebuttonstyleconfiguration.md)
  The properties of a button.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonstyle)*