# Inspecting the accessibility of the screens in your app

**Framework**: Accessibility

Focus on your app with Accessibility Inspector and investigate potential issues on each screen.

#### Overview

To investigate potential accessibility issues in your app, use Accessibility Inspector to display information about the accessibility properties of elements on screen in your app. Accessibility issues can occur on individual elements and when people navigate between elements, and you can detect both kinds of issue with the inspector.

To open Accessibility Inspector, open Xcode and choose Xcode > Open Developer Tool > Accessibility Inspector.

##### Target Your App

In Accessibility Inspector, the target menu displays a list of connected devices and apps you can inspect. By default, it displays apps running on your Mac. If you’re developing a macOS app, pick your app from the list of running apps. If you’re developing for iOS, iPadOS, watchOS, or tvOS, select the name of the device on which the app is running, then pick the app from the processes menu. For information about targeting the correct device, see [`Running your app in Simulator or on a device`](https://developer.apple.com/documentation/Xcode/running-your-app-in-simulator-or-on-a-device).

> **Note**: Accessibility Inspector targets the current foreground app by default.

Once you select your app, Accessibility Inspector displays detailed information about the accessibility properties of the current screen and focused element. The following images show the inspection of an app with the Quote element selected, and the corresponding iOS app showing the Quote element highlighted in green:

##### Inspect Individual Elements

You choose which element to inspect with the  button or by pressing Option Space to toggle inspection mode. While in inspection mode, interact with the element you want to inspect to select it. For example, in macOS, click the element to select it. Similarly, in iOS, tap the element to select it.

Accessibility Inspector displays information about the element you select in several sections:

Each screen in your app has the potential to contain accessibility issues; periodically navigate through your app during development and check for issues. If you find an inaccessible element, focus Accessibility Inspector on that element, examine its values, and trigger its actions to find the problem. For more information, see [`Performing accessibility audits for your app`](performing-accessibility-audits-for-your-app.md).

##### Navigate Elements in Accessibility Order

The navigation section of the inspector contains controls for navigating the app in the same order that accessibility features like VoiceOver use to create a linear path through the elements of the current screen. You can also use these controls to navigate to individual elements for inspection.

The play button starts an automatic sequence of navigation that loops from the current element to the end of the screen. The previous and next buttons advance the selected element one at a time in the linear navigation order. You can also press an arrow key while holding down the Control and Command keys to navigate. The speak button reads the current element aloud similar to how VoiceOver would speak the element to someone selecting this element in your app using VoiceOver.

> **Note**: By default, left and right navigation drills into elements if possible. To change this navigation behavior to strictly traverse sibling elements, choose Inspection > Disable Auto-interact Into Elements.

If any elements have missing or improper spoken descriptions, find the source of that element in your app’s source code and make corrections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/inspecting-the-accessibility-of-screens)*