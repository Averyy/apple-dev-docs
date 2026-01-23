---
url: https://developer.apple.com/design/human-interface-guidelines/disclosure-controls
framework: HIG
---

# Disclosure controls

**Type:** article

**Platforms:** ios, ipados, macos, visionos

Disclosure controls reveal and hide information and functionality related to specific controls or views.

![A stylized representation of collapsed and expanded disclosure buttons. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/b6a2092ec265c96415bae0602459aadd/components-disclosure-control-intro~dark%402x.png)

## Best practices
**Use a disclosure control to hide details until they’re relevant.** Place controls that people are most likely to use at the top of the disclosure hierarchy so they’re always visible, with more advanced functionality hidden by default. This organization helps people quickly find the most essential information without overwhelming them with too many detailed options.

## Disclosure triangles
A disclosure triangle shows and hides information and functionality associated with a view or a list of items. For example, Keynote uses a disclosure triangle to show advanced options when exporting a presentation, and the Finder uses disclosure triangles to progressively reveal hierarchy when navigating a folder structure in list view.
A disclosure triangle points inward from the leading edge when its content is hidden and down when its content is visible. Clicking or tapping the disclosure triangle switches between these two states, and the view expands or collapses accordingly to accommodate the content.
**Provide a descriptive label when using a disclosure triangle.** Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”
For developer guidance, see [NSButton.BezelStyle.disclosure](../AppKit/NSButton/BezelStyle-swift.enum/disclosure.md).

## Disclosure buttons
A disclosure button shows and hides functionality associated with a specific control. For example, the macOS Save sheet shows a disclosure button next to the Save As text field. When people click or tap this button, the Save dialog expands to give advanced navigation options for selecting an output location for their document.
A disclosure button points down when its content is hidden and up when its content is visible. Clicking or tapping the disclosure button switches between these two states, and the view expands or collapses accordingly to accommodate the content.
**Place a disclosure button near the content that it shows and hides.** Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.
**Use no more than one disclosure button in a single view.** Multiple disclosure buttons add complexity and can be confusing.
For developer guidance, see [NSButton.BezelStyle.pushDisclosure](../AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure.md).

## Platform considerations
*No additional considerations for macOS. Not supported in tvOS or watchOS.*

### iOS, iPadOS, visionOS
Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](../SwiftUI/DisclosureGroup.md) view.

## Resources

#### Related
[Outline views](outline-views.md)
[Lists and tables](lists-and-tables.md)
[Buttons](buttons.md)

#### Developer documentation
[DisclosureGroup](../SwiftUI/DisclosureGroup.md) — SwiftUI
[NSButton.BezelStyle.disclosure](../AppKit/NSButton/BezelStyle-swift.enum/disclosure.md) — AppKit
[NSButton.BezelStyle.pushDisclosure](../AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure.md) — AppKit

#### Videos
- [Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031) - Display detailed data in your SwiftUI apps more quickly and efficiently with improved stacks and new list and outline views. Now available on iOS and iPadOS for the first time, outlines are a new multi-platform tool for expressing hierarchical data that work alongside stacks and lists. Learn how to use new and improved tools in SwiftUI to display more content on screen when using table views, create smooth-scrolling and responsive stacks, and build out list views for content that needs more than a vStack can provide. Take your layout options even further with the new grid view, as well as disclosure groups.

To get the most out of this video, we recommend first checking out “SwiftUI App Essentials,” which provides an overview of everything new in SwiftUI for 2020. If you’re brand-new to coding with SwiftUI, we also suggest watching 2019’s “SwiftUI Essentials” talk.



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/disclosure-controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls)*
