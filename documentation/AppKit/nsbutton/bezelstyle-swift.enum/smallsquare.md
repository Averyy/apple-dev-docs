# NSButton.BezelStyle.smallSquare

**Framework**: AppKit  
**Kind**: case

A simple square bezel style that can scale to any size.

**Availability**:
- macOS ?+

## Declaration

```swift
case smallSquare
```

#### Discussion

A square style button (sometimes referred to as a “gradient button”) initiates an action related to a view, like adding or removing rows in a table.

![A screenshot of the open at login dialog. The dialog contains a title and message at the top, with a table underneath, and two square bezel style buttons in the lower left hand corner or a plus and minus sign beside each other.](https://docs-assets.developer.apple.com/published/ed7bd2e3f2f8b65aac8412180d3abf0b/media-4306762%402x.png)

These small square buttons contain symbols or interface icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear near their associated view — usually within or beneath it — so people know which view the buttons affect.

Prefer using a symbol in a gradient button. [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.

Avoid using labels to introduce gradient buttons. Because gradient buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.

For design guidance, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/smallsquare)*