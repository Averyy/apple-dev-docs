# borderless

**Framework**: SwiftUI  
**Kind**: property

A button style that doesn’t apply a border.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency static var borderless: BorderlessButtonStyle { get }
```

#### Discussion

In tvOS, when a person focuses on a borderless button, the button animates to a raised position with a Liquid Glass effect. This button style applies a Liquid Glass effect to the first image of the button’s content when the button gains focus. To apply the effect to a different subview of your button, apply the [`hoverEffect(_:)`](view/hovereffect(_:).md) modifier with a [`highlight`](hovereffect/highlight.md) effect to that subview. For more information, see [`Creating a tvOS media catalog app in SwiftUI`](creating-a-tvos-media-catalog-app-in-swiftui.md).

To apply this style to a button, or to a view that contains buttons, use the [`buttonStyle(_:)`](view/buttonstyle(_:)-66fbx.md) modifier.

## See Also

- [static var automatic: DefaultButtonStyle](primitivebuttonstyle/automatic.md)
  The default button style, based on the button’s context.
- [static var accessoryBar: AccessoryBarButtonStyle](primitivebuttonstyle/accessorybar.md)
  A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [static var accessoryBarAction: AccessoryBarActionButtonStyle](primitivebuttonstyle/accessorybaraction.md)
  A button style that you use for extra actions in an accessory toolbar.
- [static var bordered: BorderedButtonStyle](primitivebuttonstyle/bordered.md)
  A button style that applies the standard border style based on the button’s context.
- [static var borderedProminent: BorderedProminentButtonStyle](primitivebuttonstyle/borderedprominent.md)
  A button style that applies the standard bordered prominent style based on the button’s context.
- [static var card: CardButtonStyle](primitivebuttonstyle/card.md)
  A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [static var glass: GlassButtonStyle](primitivebuttonstyle/glass.md)
  A button style that applies a Liquid Glass effect based on the button’s context.
- [static var glassProminent: GlassProminentButtonStyle](primitivebuttonstyle/glassprominent.md)
  A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [static func glass(Glass) -> Self](primitivebuttonstyle/glass(_:).md)
  A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [static var link: LinkButtonStyle](primitivebuttonstyle/link.md)
  A button style for buttons that emulate links.
- [static var plain: PlainButtonStyle](primitivebuttonstyle/plain.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/borderless)*