# PrimitiveButtonStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.

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
@preconcurrency protocol PrimitiveButtonStyle
```

#### Overview

To configure the current button style for a view hierarchy, use the [`buttonStyle(_:)`](view/buttonstyle(_:).md) modifier. Specify a style that conforms to `PrimitiveButtonStyle` to create a button with custom interaction behavior. To create a button with the standard button interaction behavior defined for each platform, use [`ButtonStyle`](buttonstyle.md) instead.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Getting built-in button styles
- [static var automatic: DefaultButtonStyle](primitivebuttonstyle/automatic.md)
  The default button style, based on the button’s context.
- [static var accessoryBar: AccessoryBarButtonStyle](primitivebuttonstyle/accessorybar.md)
  A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [static var accessoryBarAction: AccessoryBarActionButtonStyle](primitivebuttonstyle/accessorybaraction.md)
  A button style that you use for extra actions in an accessory toolbar.
- [static var bordered: BorderedButtonStyle](primitivebuttonstyle/bordered.md)
  A button style that applies standard border artwork based on the button’s context.
- [static var borderedProminent: BorderedProminentButtonStyle](primitivebuttonstyle/borderedprominent.md)
  A button style that applies standard border prominent artwork based on the button’s context.
- [static var borderless: BorderlessButtonStyle](primitivebuttonstyle/borderless.md)
  A button style that doesn’t apply a border.
- [static var card: CardButtonStyle](primitivebuttonstyle/card.md)
  A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [static var link: LinkButtonStyle](primitivebuttonstyle/link.md)
  A button style for buttons that emulate links.
- [static var plain: PlainButtonStyle](primitivebuttonstyle/plain.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
### Creating custom button styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](primitivebuttonstyle/makebody(configuration:).md)
  Creates a view that represents the body of a button.
- [PrimitiveButtonStyle.Configuration](primitivebuttonstyle/configuration.md)
  The properties of a button.
- [associatedtype Body : View](primitivebuttonstyle/body.md)
  A view that represents the body of a button.
### Supporting types
- [struct DefaultButtonStyle](defaultbuttonstyle.md)
  The default button style, based on the button’s context.
- [struct AccessoryBarButtonStyle](accessorybarbuttonstyle.md)
  A button style that you use for actions in an accessory toolbar that narrow the focus of a search or other operation.
- [struct AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md)
  A button style that you use for extra actions in an accessory toolbar.
- [struct BorderedButtonStyle](borderedbuttonstyle.md)
  A button style that applies standard border artwork based on the button’s context.
- [struct BorderedProminentButtonStyle](borderedprominentbuttonstyle.md)
  A button style that applies standard border prominent artwork based on the button’s context.
- [struct BorderlessButtonStyle](borderlessbuttonstyle.md)
  A button style that doesn’t apply a border.
- [struct CardButtonStyle](cardbuttonstyle.md)
  A button style that doesn’t pad the content, and applies a motion effect when a button has focus.
- [struct LinkButtonStyle](linkbuttonstyle.md)
  A button style for buttons that emulate links.
- [struct PlainButtonStyle](plainbuttonstyle.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.
### Type Properties
- [static var glass: GlassButtonStyle](primitivebuttonstyle/glass.md)
  A button style that applies Liquid Glass based on the button’s context.

## Relationships

### Conforming Types
- [AccessoryBarActionButtonStyle](accessorybaractionbuttonstyle.md)
- [AccessoryBarButtonStyle](accessorybarbuttonstyle.md)
- [BorderedButtonStyle](borderedbuttonstyle.md)
- [BorderedProminentButtonStyle](borderedprominentbuttonstyle.md)
- [BorderlessButtonStyle](borderlessbuttonstyle.md)
- [CardButtonStyle](cardbuttonstyle.md)
- [DefaultButtonStyle](defaultbuttonstyle.md)
- [GlassButtonStyle](glassbuttonstyle.md)
- [LinkButtonStyle](linkbuttonstyle.md)
- [PlainButtonStyle](plainbuttonstyle.md)

## See Also

- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [protocol ButtonStyle](buttonstyle.md)
  A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [struct ButtonStyleConfiguration](buttonstyleconfiguration.md)
  The properties of a button.
- [struct PrimitiveButtonStyleConfiguration](primitivebuttonstyleconfiguration.md)
  The properties of a button.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyle)*