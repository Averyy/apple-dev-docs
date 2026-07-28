---
url: https://developer.apple.com/design/human-interface-guidelines/tab-views
framework: HIG
---

# Tab views

**Type:** article

**Platforms:** macos, watchos

> **Updated 2023-06-05:** Added guidance for using tab views in watchOS.

A tab view presents multiple mutually exclusive panes of content in the same area, which people can switch between using a tabbed control.

![A stylized representation of a view with three labeled tabs, the first of which is selected. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/91f9c53bf4c655720f8cf837508fa019/components-tab-view-intro~dark%402x.png)

## Best practices
**Use a tab view to present closely related areas of content.** The appearance of a tab view provides a strong visual indication of enclosure. People expect each tab to display content that is in some way similar or related to the content in the other tabs.
**Make sure the controls within a pane affect content only in the same pane.** Panes are mutually exclusive, so ensure they’re fully self-contained.
**Provide a label for each tab that describes the contents of its pane.** A good label helps people predict the contents of a pane before clicking or tapping its tab. In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts. Use title-style capitalization for tab labels.
**Avoid using a pop-up button to switch between tabs.** A tabbed control is efficient because it requires a single click or tap to make a selection, whereas a pop-up button requires two. A tabbed control also presents all choices onscreen at the same time, whereas people must click a pop-up button to see its choices. Note that a pop-up button can be a reasonable alternative in cases where there are too many panes of content to reasonably display with tabs.
**Avoid providing more than six tabs in a tab view.** Having more than six tabs can be overwhelming and create layout issues. If you need to present six or more tabs, consider another way to implement the interface. For example, you could instead present each tab as a view option in a pop-up button menu.
For developer guidance, see [NSTabView](../AppKit/NSTabView.md).

## Anatomy
The tabbed control appears on the top edge of the content area. You can choose to hide the control, which is appropriate for an app that switches between panes programmatically.
![An illustration of a window in which a three-tab tabbed control is centered on the top edge of the content view.](https://docs-assets.developer.apple.com/published/f00bd8dd11acf7cc5f8520b4b5270956/tab-views-top~dark%402x.png)
When you hide the tabbed control, the content area can be borderless, bezeled, or bordered with a line. A borderless view can be solid or transparent.
**In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view.** This layout looks clean and leaves room for additional controls that aren’t directly related to the contents of the tab view. You can extend a tab view to meet the window edges, but this layout is unusual.

## Platform considerations
*Not supported in iOS, iPadOS, tvOS, or visionOS.*

### iOS, iPadOS
For similar functionality, consider using a [segmented control](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) instead.

### watchOS
watchOS displays tab views using [page controls](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls). For developer guidance, see [TabView](../SwiftUI/TabView.md).
![An illustration showing the page control next to the Digital Crown on Apple Watch. The current dot is enlarged, indicating that people can scroll through the current content, as well as scroll between pages.](https://docs-assets.developer.apple.com/published/c65574d8caec7a02132f9beeee66b84f/tab-view-watch-vertical%402x.png)

## Resources

#### Related
[Tab bars](tab-bars.md)
[Segmented controls](segmented-controls.md)

#### Developer documentation
[TabView](../SwiftUI/TabView.md) — SwiftUI
[NSTabView](../AppKit/NSTabView.md) — AppKit

## Change log
| Date | Changes |
| --- | --- |
| June 5, 2023 | Added guidance for using tab views in watchOS. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/tab-views](https://developer.apple.com/design/human-interface-guidelines/tab-views)*
