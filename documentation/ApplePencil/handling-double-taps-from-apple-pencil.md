# Handling double taps from Apple Pencil

**Framework**: Apple Pencil

Detect and respond to double taps a person makes on Apple Pencil.

#### Overview

You can use Apple Pencil interactions to allow people to access functionality in your app quickly. Double-tapping Apple Pencil lets a person perform actions such as switching between drawing tools without moving the pencil to another location on the screen.

![An illustration showing a hand double-tapping Apple Pencil with the index finger.](https://docs-assets.developer.apple.com/published/796d7b73d68c0168b9105f002aa0984e/apple-pencil-double-tap%402x.png)

##### Register for a Double Tap

To respond to double taps from Apple Pencil in your app, you need to register your view to receive double-tap interactions.

##### Check the Preferred Double Tap Action

A person can choose which action they prefer to perform when they double-tap Apple Pencil. They choose this systemwide preference in Settings > Apple Pencil > Actions > Double Tap.

In your app, you can check the value of this preferred action for double tap.

##### Choose the Action to Perform

When possible, perform the preferred action to provide a consistent user experience across apps that support double taps. If the preferred action doesn’t make sense in your app, consider giving people a way to choose a custom action that’s suitable for your app. For design guidance, read Human Interface Guidelines > Apple Pencil and Scribble > [`Double tap`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Double-tap).

The following code shows a snippet from a drawing app that provides custom drawing tools. This app allows a person to configure a custom action to quickly swap to their favorite custom drawing tool instead of using the systemwide preferred action for double taps. This app also supports the preferred actions to ignore double taps, switch to the previous tool, and switch to the eraser tool.

###### Related Articles

###### Related Reference in Swiftui

###### Related Reference in Uikit


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepencil/handling-double-taps-from-apple-pencil)*