# Writing Tools

**Framework**: AppKit

Add support for Writing Tools to your app’s text views.

#### Overview

Writing Tools provides a simple way for people to improve what they write using your app. Text views that support Writing Tools gain the ability to proofread, rewrite, summarize, or compose content with the help of system-provided large language models (LLMs) and Apple Intelligence.

Writing Tools supports both the standard system views and custom text views you create. The [`NSTextView`](nstextview.md) and [`NSTextField`](nstextfield.md) classes automatically support Writing Tools, but you can customize that support to suit your app’s requirements. You can also add Writing Tools support to any [`NSView`](nsview.md) in your app that contains text.

## Topics

### Configuration
- [Customizing Writing Tools behavior for AppKit views](customizing-writing-tools-behavior-for-system-views.md)
  Modify the behavior of Writing Tools in standard macOS text views, and adjust your app’s behavior while the feature is active.
- [enum NSWritingToolsBehavior](nswritingtoolsbehavior.md)
  Constants that specify the Writing Tools experience for the underlying view.
- [struct NSWritingToolsResultOptions](nswritingtoolsresultoptions.md)
  Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.
### Writing Tools for custom views
- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)
  Adopt a simplified version of the Writing Tools experience in a custom view using the pasteboard and macOS services.
- [Adding Writing Tools support to a custom AppKit view](adding-writing-tools-support-to-a-custom-nsview.md)
  Integrate Writing Tools support, including support for inline replacement animations, to your custom text views on macOS.
- [class NSWritingToolsCoordinator](nswritingtoolscoordinator.md)
  An object that manages interactions between Writing Tools and your custom text view.
- [NSWritingToolsCoordinator.Delegate](nswritingtoolscoordinator/delegate-swift.protocol.md)
  An interface that you use to manage interactions between Writing Tools and your custom text view.
- [NSWritingToolsCoordinator.Context](nswritingtoolscoordinator/context.md)
  A data object that you use to share your custom view’s text with Writing Tools.
- [NSWritingToolsCoordinator.AnimationParameters](nswritingtoolscoordinator/animationparameters.md)
  An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.
### Text previews
- [class NSTextPreview](nstextpreview.md)
  A snapshot of the text in your view, which the system uses to create user-visible effects.

## See Also

- [Text Display](text-display.md)
  Display text and check spelling.
- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Fonts](fonts.md)
  Manage the fonts used to display text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/writing-tools)*