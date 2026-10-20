# borderless

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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
@export(implementation)
nonisolated static var borderless: BorderlessButtonStyle { get }
```

Available when `Self` is `BorderlessButtonStyle`.

#### Discussion

In tvOS, when a person focuses on a borderless button, the button animates to a raised position with a Liquid Glass effect. This button style applies a Liquid Glass effect to the first image of the button’s content when the button gains focus. To apply the effect to a different subview of your button, apply the [`hoverEffect(_:)`](../view/hovereffect%28_%29.md) modifier with a [`highlight`](../hovereffect/highlight.md) effect to that subview. For more information, see [Creating a tvOS media catalog app in SwiftUI](../creating-a-tvos-media-catalog-app-in-swiftui.md).

To apply this style to a button, or to a view that contains buttons, use the [`buttonStyle(_:)`](../view/buttonstyle%28_%29-66fbx.md) modifier.

## See Also

### Getting built-in button styles
- [static var automatic: DefaultButtonStyle](./automatic.md)
  The default button style, based on the button’s context.
- [static var accessoryBar: AccessoryBarButtonStyle](./accessorybar.md)
  A button style that is typically used in the context of an accessory toolbar (sometimes refererred to as a “scope bar”), for buttons that narrow the focus of a search or other operation.
- [static var accessoryBarAction: AccessoryBarActionButtonStyle](./accessorybaraction.md)
  A button style that you use for extra actions in an accessory toolbar.
- [static var bordered: BorderedButtonStyle](./bordered.md)
  A button style that applies the standard border style based on the button’s context.
- [static var borderedProminent: BorderedProminentButtonStyle](./borderedprominent.md)
  A button style that applies the standard bordered prominent style based on the button’s context.
- [static var card: CardButtonStyle](./card.md)
  A button style that doesn’t pad the content, and applies a Liquid Glass effect when the button has focus.
- [static var glass: GlassButtonStyle](./glass.md)
  A button style that applies a Liquid Glass effect based on the button’s context.
- [static var glassProminent: GlassProminentButtonStyle](./glassprominent.md)
  A button style that applies a prominent Liquid Glass effect based on the button’s context.
- [static func glass(Glass) -> Self](./glass%28_%29.md)
  A button style that applies a configurable Liquid Glass effect based on the button’s context.
- [static var link: LinkButtonStyle](./link.md)
  A button style for buttons that emulate links.
- [static var plain: PlainButtonStyle](./plain.md)
  A button style that doesn’t style or decorate its content while idle, but may apply a visual effect to indicate the pressed, focused, or enabled state of the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/borderless)*