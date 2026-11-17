# Testing your app in CarPlay Simulator

**Framework**: CarPlay  
**Role**: Article

Run your app in CarPlay Simulator to identify and debug potential issues.

## Overview

CarPlay Simulator is a Mac app that simulates the CarPlay environment with the help of a connected iPhone. During development, use CarPlay Simulator to test your app, widgets, and Live Activities in the CarPlay environment. The CarPlay Simulator window imitates a vehicle’s primary display, and you interact with it directly or using simulated vehicle controls. The window also provides ways to configure the CarPay environment, including options to change the size and resolution of the display, change environmental settings, and simulate relevant events.

> ❗ **Important**: CarPlay Simulator is useful as an initial validation step, but Apple recommends you also test your CarPlay app in a vehicle or aftermarket system. If you test using an aftermarket head unit, choose one that supports Wireless CarPlay so your iPhone can connect wirelessly to the head unit and via cable to your Mac for debugging in Xcode.

## Connect an iPhone to your Mac and open CarPlay Simulator

In iOS 27 and later, CarPlay development requires an iPhone connected to your Mac and the CarPlay Simulator app. To run your app in CarPlay Simulator:

1. Connect the iPhone you use to develop apps to your Mac.
2. Set the iPhone as the build destination for your iOS app.
3. Build and run your iOS app on the connected iPhone.
4. Open Device Hub.
5. Select the connected iPhone in the list of devices.
6. Choose Device > CarPlay Simulator from the menu, or right-click the device and choose CarPlay Simulator from the contextual menu.

When CarPlay Simulator launches, Device Hub creates a new window with the CarPlay interface. In this window, launch your app by tapping it directly, or use the vehicle controls to select and run it. Use the window’s controls to change the display size and resolution so you can see how your app looks in different configurations. You can also use the window controls to simulate app-specific events. For example, you can specify a destination to test your navigation app’s turn-by-turn directions.

> **Note**: If you don’t see an option to open CarPlay Simulator from Device Hub, make sure an iPhone is connected to your Mac and your iOS app offers CarPlay support. If you still don’t see an option to open CarPlay Simulator, [download the additional tools for Xcode](https://developer.apple.com/download/all/?q=additional%20tools%20for%20xcode) to get the CarPlay Simulator app and run it directly.

## Troubleshoot issues with CarPlay Simulator not showing your app

When you run CarPlay Simulator, your app appears only if it contains all the expected elements of a regular CarPlay app. Every CarPlay app requires the following elements:

- The Signing & Capabilities tab of your Xcode project contains a CarPlay capability.
- Your Xcode project has an entitlements file with the CarPlay entitlement for your app’s capability.
- Your project uses a provisioning profile that supports the requested CarPlay entitlement.
- Your app supports multiple scenes and provides a CarPlay main scene.

> **Note**: When you add a CarPlay capability to your project, Xcode automatically adds an entitlements file with the matching capability to your project.

If you’re building a new app, verify that all of these elements are present before running the app in CarPlay Simulator. If any of these elements are missing, your app might not appear in the simulator window.

For information about how to request entitlements for your app, see [Preparing your iOS app for CarPlay development](./preparing-your-ios-app-for-carplay-development.md). For information about configuring your app’s main scene, see [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/testing-your-app-in-carplay-simulator)*