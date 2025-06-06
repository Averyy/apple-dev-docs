# Handwriting recognition

**Framework**: UIKit

Configure text fields and custom views that accept text to handle input from Apple Pencil.

## Topics

### Essentials
- [Customizing Scribble with Interactions](../PencilKit/customizing-scribble-with-interactions.md)
  Enable writing on a non-text-input view by adding interactions.
### Text fields
- [class UIScribbleInteraction](uiscribbleinteraction.md)
  An interaction for customizing the behavior of Scribble on text input views, or for suppressing it entirely in specific cases.
- [protocol UIScribbleInteractionDelegate](uiscribbleinteractiondelegate.md)
  Methods for customizing or suppressing Scribble behavior within text input views.
### Custom views
- [class UIIndirectScribbleInteraction](uiindirectscribbleinteraction-1nfjm.md)
  An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.
- [protocol UIIndirectScribbleInteractionDelegate](uiindirectscribbleinteractiondelegate-hdh.md)
  Methods that customize behavior on views that aren’t formally text input views.
- [associatedtype ElementIdentifier : Hashable = String](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md)
  A unique identifier for a control that isn’t a text field in a Scribble interaction.

## See Also

- [Text display and fonts](text-display-and-fonts.md)
  Display text, manage fonts, and check spelling.
- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Keyboards and input](keyboards-and-input.md)
  Configure the system keyboard, create your own keyboards to handle input, or detect key presses on a physical keyboard.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/handwriting-recognition)*