# Performing accessibility testing for your app

**Framework**: Accessibility

Test your app with accessibility settings and assistive technologies to discover and address accessibility issues.

#### Overview

It’s always a good idea to experience your app from the perspective of the people using it. When you test your app from the user’s perspective, make sure you also test with different accessibility settings and assistive technologies like VoiceOver, Voice Control, and Switch Control so you can experience the app in the same way as people who rely on these features. Testing your app with accessibility settings reveals which tasks are possible to complete, which elements are accessible and which aren’t, and whether your navigation is clear and logical for every use case.

![None](https://docs-assets.developer.apple.com/published/54a857292994cb77dc0abc95ea382205/performing-accessibility-testing%402x.png)

##### Identify the Main Tasks in Your App

Before you begin accessibility testing, compile a list of the main tasks that a person can perform on each screen in your app. For example, a to-do list app might contain several screens with one or more possible tasks as described in the following list.

##### Create an Accessibility Testing Matrix

After you identify your app’s main tasks, choose which devices, accessibility settings, and assistive technologies to test those tasks with.

It’s recommended to test your app on each type of device your app supports (for example, iPhone, iPad, and Mac). Testing on each of those devices lets you experience the app in the same way as a person who downloads and installs it. Testing on device can also highlight subtle differences in your app’s user experience across platforms.

After you prepare your devices for testing, identify which accessibility features to test. As a starting point, it’s recommended that you test your app for the following accessibility categories, although you’re encouraged to test with additional settings and technologies if you can:

- Visual accessibility for accessibility settings related to color, text, motion, and more
- Media accessibility for accessibility settings related to captions, audio descriptions, audio transcripts, and more
- Assistive technologies such as VoiceOver, Voice Control, Switch Control, and more

The following sections describe how to test your app for visual accessibility, media accessibility, and several key assistive technologies.

##### Test with Accessibility Settings

To test with accessibility settings, turn on each of the following accessibility features in Settings > Accessibility, one at a time. Work through your testing matrix by completing the main tasks in your app while each accessibility setting is on.

##### Test with Assistive Technologies

To test with assistive technologies, set up and turn on each of the following assistive technologies, one at a time. Work through your testing matrix by completing the main tasks in your app using only that assistive technology.

##### Diagnose and Address Accessibility Issues

As you test your app’s workflows, make sure your app continues to provide a good user experience while accessibility settings and assistive technologies are on. Check that you can access every element and that the ordering of those elements is what you intend. Make note when you find it difficult to perform a task. Confirm that your UI adjusts appropriately when the system font size, color filter, or other visual settings change to something other than the default. You can use the following list as a starting point for ensuring that your app provides a good experience in various accessibility categories.

Take notes about any issues as you discover them so you can address them in your app’s design and implementation. If you encounter accessibility issues that you aren’t able to troubleshoot while testing on the device, try using [`Accessibility Inspector`](accessibility-inspector.md) to help diagnose and resolve issues. You can also automate accessibility testing by adding accessibility audits in your UI tests, as described in [`Perform accessibility audits for your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10035).

Address accessibility issues that you discover during testing so that you’re able to successfully complete all the tasks in your app when accessibility settings and assistive technologies are on.

## See Also

- [Accessibility updates](../Updates/Accessibility.md)
  Learn about important changes to Accessibility.
- [Accessibility](https://developer.apple.com/design/Human-Interface-Guidelines/accessibility)
  Accessible user interfaces empower everyone to have a great experience with your app or game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app)*