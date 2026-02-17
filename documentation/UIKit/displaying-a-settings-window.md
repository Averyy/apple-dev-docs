# Displaying a Settings window

**Framework**: UIKit

Provide a Settings window in your Mac app built with Mac Catalyst so users can manage app settings defined in a Settings bundle.

#### Overview

Mac apps typically display app-specific settings using a Settings window accessible through the standard Settings menu item under the app menu in the menu bar.

Mac apps built with Mac Catalyst that include a `Settings.bundle` file automatically get the Settings menu item and a Settings window. When a user selects the Settings menu item, the system displays a Mac-friendly Settings window based on the options provided in your Settings bundle. To learn about Settings bundles, see [`Building a Settings bundle for your app`](https://developer.apple.com/documentation/Foundation/building-a-settings-bundle-for-your-app).

##### Add a Settings Window to Your App

To include a Settings window in your Mac app, start by adding a `Settings.bundle` file to your Xcode project:

1. Open your app project in Xcode and choose File > New > Target.
2. From the Resource group, select Settings Bundle, and then click Next.
3. Enter the name of your settings bundle.
4. Click Create.

![A screenshot of the new file dialog in Xcode, showing the selection of the iOS platform, and the selection of the Settings Bundle template.](https://docs-assets.developer.apple.com/published/6d7d50a892f4a6ebbaf652ae3a176ec9/displaying-a-settings-window-1%402x.png)

##### Add Toolbar Tabs to the Settings Window

A Settings bundle can include one or more child panes that allow you to organize your settings hierarchically (see [`Building a Settings bundle for your app`](https://developer.apple.com/documentation/Foundation/building-a-settings-bundle-for-your-app#Add-a-child-page-element)). In iOS, the Settings app displays a child pane as a settings row. When the user taps the row, the app displays a new view showing the settings defined in the child pane’s property list file.

In macOS, the Settings window displays a child pane as a tab on the window’s toolbar. When the user clicks the tab, they see the settings provided in the child pane’s property list file.

The tab for a child pane displays the pane’s title and a system-provided icon. To customize the icon, add the following key to the child pane’s property list file:

You must include the image file in the Settings bundle that contains the child pane’s property list file.

##### Confirm Changes Made with a Toggle Switch

Another element of the Settings bundle is the toggle switch element, which displays an ON/OFF switch that the user can toggle. Your Mac app can prompt the user for a confirmation when they toggle the switch by including the following keys in the toggle switch element:

Each dictionary contains the following keys that define the contents of the prompt:

For more information, see [`Building a Settings bundle for your app`](https://developer.apple.com/documentation/Foundation/building-a-settings-bundle-for-your-app#Add-a-toggle-switch-element).

##### Display Subtitles for Toggle Switches

Some iOS apps show descriptive text in a subtitle below a toggle switch using a group item with footer text. While the Settings window supports this approach, the appearance on a Mac isn’t ideal. Instead, include the following key in the toggle switch element to show a subtitle:

## See Also

- [Detecting changes in the preferences window](detecting-changes-in-the-preferences-window.md)
  Listen for and respond to a user’s preference changes in your Mac app built with Mac Catalyst using Combine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/displaying-a-settings-window)*