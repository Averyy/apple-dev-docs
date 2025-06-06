# Handling squeezes from Apple Pencil

**Framework**: Apple Pencil

Detect and respond to squeezes a person makes on Apple Pencil Pro.

#### Overview

You can use Apple Pencil interactions to allow people to access functionality in your app quickly. Squeezing Apple Pencil Pro lets a person perform actions such as showing a contextual palette without moving the pencil to another location on the screen.

![An illustration showing a hand squeezing Apple Pencil near the tip.](https://docs-assets.developer.apple.com/published/7d3dbec5d663bd982e3a4b95467f91c7/apple-pencil-squeeze%402x.png)

> **Note**: Only Apple Pencil Pro supports squeeze interactions.

Only Apple Pencil Pro supports squeeze interactions.

##### Register for a Squeeze

To respond to squeezes from Apple Pencil Pro in your app, you need to register your view to receive squeeze interactions.

##### Check the Preferred Squeeze Action

A person can choose which action they prefer to perform when they squeeze Apple Pencil Pro. They choose this preference in Settings > Apple Pencil > Actions > Squeeze. In addition to drawing-specific actions like switching drawing tools, people can configure the preferred action for squeeze to perform any App Shortcut, including pre-configured shortcuts you provide for your app.

In your app, you can check the value of this preferred action for squeeze.

##### Choose the Action to Perform

When possible, perform the preferred action to provide a consistent user experience across apps that support squeezes. If the preferred action doesn’t make sense in your app, consider giving people a way to specify a custom action that’s suitable for your app. For design guidance, read Human Interface Guidelines > Apple Pencil and Scribble > [`Squeeze`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Squeeze).

The following code shows a snippet from a drawing app that provides custom drawing tools. This app allows a person to configure a custom action to quickly swap to their favorite custom drawing tool instead of using the systemwide preferred action for squeezes. This app also supports the preferred actions to ignore squeezes, switch to the previous tool, and show a custom contextual palette near the Apple Pencil Pro tip.

###### Related Articles

###### Related Reference in Swiftui

###### Related Reference in Uikit


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepencil/handling-squeezes-from-apple-pencil)*