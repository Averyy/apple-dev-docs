# Displaying a Preferences window

**Framework**: UIKit

Provide a Preferences window in your Mac app built with Mac Catalyst so users can manage app preferences defined in a Settings bundle.

#### Overview

Mac apps typically display app-specific preferences using a Preferences window accessible through the standard Preferences menu item under the app menu in the menu bar.

Mac apps built with Mac Catalyst that include a `Settings.bundle` file automatically get the Preferences menu item and a Preferences window. When a user selects the Preferences menu item, the system displays a Mac-friendly Preferences window based on the options provided in your Settings bundle. To learn about Settings bundles, see [`Implementing an iOS Settings Bundle`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/Preferences/Preferences.html#//apple_ref/doc/uid/10000059i-CH6).

##### Add a Preferences Window to Your App

To include a Preferences window in your Mac app, add a `Settings.bundle` file to your Xcode project by pressing Command-N and selecting the Settings Bundle template from the Resources section under iOS. Then click Next to save the file to your project.

![A screenshot of Xcode showing the selection of the iOS platform, selection of the Setting Bundles template, and the Next button that you click to save the Settings bundle.](https://docs-assets.developer.apple.com/published/9d467cbcb45c9d6f260c7f5cc25a7eac/media-3402483%402x.png)

##### Add Toolbar Tabs to the Preferences Window

A Settings bundle can include one or more child panes that allow you to organize your preferences hierarchically (see [`Hierarchical Preferences`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/Preferences/Preferences.html#//apple_ref/doc/uid/10000059i-CH6-SW4)). In iOS, the Settings app displays a child pane as a preference row. When the user taps the row, the app displays a new view showing the preferences defined in the child pane’s property list file.

In macOS, the Preferences window displays a child pane as a tab on the window’s toolbar. When the user clicks the tab, they see the preferences provided in the child pane’s property list file.

The tab for a child pane displays the pane’s title and a system-provided icon. To customize the icon, add the following key to the child pane’s property list file:

You must include the image file in the Settings bundle that contains the child pane’s property list file.

##### Confirm Changes Made with a Toggle Switch

Another element of the Settings bundle is the [`Toggle Switch Element`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/PreferenceSettings/Conceptual/SettingsApplicationSchemaReference/Articles/PSToggleSwitchSpecifier.html#//apple_ref/doc/uid/TP40007012), which displays an ON/OFF switch that the user can toggle. Your Mac app can prompt the user for a confirmation when they toggle the switch by including the following keys in the toggle switch element:

Each dictionary contains the following keys that define the contents of the prompt:

##### Display Subtitles for Toggle Switches

Some iOS apps show descriptive text in a subtitle below a toggle switch using a group item with footer text. While the Preferences window supports this approach, the appearance on a Mac isn’t ideal. Instead, include the following key in the toggle switch element to show a subtitle:

## See Also

- [Detecting changes in the preferences window](detecting-changes-in-the-preferences-window.md)
  Listen for and respond to a user’s preference changes in your Mac app built with Mac Catalyst using Combine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/displaying-a-preferences-window)*