# Creating visual effects with SwiftUI

**Framework**: SwiftUI  
**Role**: Sample Code  
**Download**: [CreatingVisualEffectsWithSwiftUI.zip](https://docs-assets.developer.apple.com/published/9a15b1cc1a22/CreatingVisualEffectsWithSwiftUI.zip)

Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- Xcode 16.0+

## Overview

> **Note**: This sample code project is associated with WWDC24 session 10151: [Create custom visual effects in SwiftUI](https://developer.apple.com/wwdc24/10151/).

## See Also

### Rendering text
- [protocol TextAttribute](./textattribute.md)
  A value that you can attach to text views and that text renderers can query.
- [func textRenderer<T>(T) -> some View](./view/textrenderer%28_%29.md)
  Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [protocol TextRenderer](./textrenderer.md)
  A value that can replace the default text view rendering behavior.
- [struct TextProxy](./textproxy.md)
  A proxy for a text view that custom text renderers use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/creating-visual-effects-with-swiftui)*