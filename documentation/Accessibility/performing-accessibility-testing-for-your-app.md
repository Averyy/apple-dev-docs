# Performing accessibility testing for your app

**Framework**: Accessibility

Test your app with accessibility settings and assistive technologies to discover and address accessibility issues.

#### Overview

It’s always a good idea to experience your app from the perspective of the people using it. When you test your app from the user’s perspective, make sure you also test with different accessibility settings and assistive technologies like VoiceOver, Voice Control, and Switch Control so you can experience the app in the same way as people who rely on these features. Testing your app with accessibility settings reveals which tasks are possible to complete, which elements are accessible and which aren’t, and whether your navigation is clear and logical for every use case.

![None](/images/com.apple.Accessibility/performing-accessibility-testing@2x.png)

##### Identify the Main Tasks in Your App

Before you begin accessibility testing, compile a list of the main tasks that a person can perform on each screen in your app. For example, a to-do list app might contain several screens with one or more possible tasks as described in the following list.

- **First launch experience**: The user may need to complete or opt out of an onboarding flow.
- **Login screen**: The user may need to choose a login service, enter a username and password, interact with a login button, request a password reset, or enter information to create a new account.
- **Empty to-do list**: The user may need to create a new task, or open app settings.
- **To-do list with tasks**: The user may need to mark a task as complete, undo marking a task as complete, or create a new task.
- **New task screen**: The user may need to enter information about the task, save the task to the list, or exit the screen without saving the task.
- **Settings screen**: The user may need to adjust app settings, or exit the screen without changing anything.

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

**Visual accessibility**:

- Display & Text Size > Bold Text
- Display & Text Size > Larger Text > Larger Accessibility Sizes
- Display & Text Size > Button Shapes
- Display & Text Size > On/Off Labels
- Display & Text Size > Reduce Transparency
- Display & Text Size > Increase Contrast
- Display & Text Size > Differentiate Without Color
- Display & Text Size > Color Filters > Red/Green Filter, Green/Red Filter, Blue/Yellow Filter
- Motion > Reduce Motion
- Motion > Dim Flashing Lights

**Media accessibility**:

- Audio Descriptions
- Subtitles & Captioning > Closed Captions + SDH
- Subtitles & Captioning > Show Audio Transcriptions

##### Test with Assistive Technologies

To test with assistive technologies, set up and turn on each of the following assistive technologies, one at a time. Work through your testing matrix by completing the main tasks in your app using only that assistive technology.

**VoiceOver**:

- Install your app on a physical device, since VoiceOver isn’t available on Simulator.
- Learn how to turn VoiceOver off so you can exit it after testing. For example, in iOS, you can set up [`Accessibility Shortcut`](https://developer.apple.comhttps://support.apple.com/guide/iphone/open-features-with-accessibility-shortcut-iph3e2e31a5/ios) to turn VoiceOver on and off. In macOS, you can press Command-F5.
- Adjust your device volume to an appropriate level.
- Navigate to Settings > Accessibility > VoiceOver, and turn on VoiceOver.
- Adjust the Speaking Rate slider to an appropriate speaking pace.
- If you provide hints for any accessible elements in your app, make sure the Verbosity > Speak Hints setting is on.

With VoiceOver on, use VoiceOver gestures to navigate your app. Although you don’t need to become an expert VoiceOver user to test your app with it, you do need to know several key gestures, which have slight variations across platforms. For example, the following gestures apply to devices with touchscreen and trackpad input.

| Gesture | Action |
| --- | --- |
| Tap | Select and speak an item. |
| Swipe right or left | Select the next or previous item. |
| Double tap | Select and speak an item. |
| Two-finger tap | Pause or continue speaking. |
| Two-finger swipe up | Speak the entire screen from the top. |
| Three-finger triple tap | Turn the screen curtain on or off. |

To begin testing, turn on the *screen curtain* to replicate the experience of someone who is solely relying on VoiceOver. When the screen curtain is on, the screen contents are active even though the display is black and appears to be turned off.

> 💡 **Tip**: A great place to practice VoiceOver gestures is in the VoiceOver Practice area in Settings > Accessibility > VoiceOver. VoiceOver needs to be on for the VoiceOver Practice button to appear.

To learn more about VoiceOver gestures, read the platform-specific user guides listed in [`VoiceOver`](voiceover.md).

**Voice Control**:

- Install your app on a physical device, since Voice Control isn’t available on Simulator.
- Learn how to turn Voice Control off. For example, in iOS, you can set up [`Accessibility Shortcut`](https://developer.apple.comhttps://support.apple.com/guide/iphone/open-features-with-accessibility-shortcut-iph3e2e31a5/ios) to turn Voice Control on and off. In macOS, you can press Command-F5.
- Make sure you’re in an environment where you can speak clearly and audibly. For example, being in a public space like a coffee shop with a lot of cross-talk and background noise may make Voice Control testing challenging.
- Navigate to Settings > Accessibility > Voice Control, and turn on Voice Control.

With Voice Control on, use voice commands to navigate your app. Although you don’t need to become an expert Voice Control user to test your app with it, you do need to know several key commands, which have slight variations across platforms.

| Command | Action |
| --- | --- |
| “Open *app name*” | Open a specific app. |
| “Show names” or “Show numbers” | Display a screen overlay that shows item names or numbers. |
| “Tap *item name or number*” | Interact with an item. |
| “Scroll down” or “Scroll up” | Perform a scroll. |
| “Stop listening” and “Start listening” | Pause or continue Voice Control. |
| “Show commands” | Learn more about Voice Control commands. |

> 💡 **Tip**: A great place to practice Voice Control commands is in the Voice Control guide in Settings > Accessibility > Voice Control. Open the guide for a tutorial of different kinds of commands Voice Control supports.

To learn more about Voice Control commands, read the platform-specific user guides listed in [`Voice Control`](voice-control.md).

**Switch Control**:

- Install your app on a physical device, since Switch Control isn’t available on Simulator.
- Learn how to turn Switch Control off. For example, in iOS, you can set up [`Accessibility Shortcut`](https://developer.apple.comhttps://support.apple.com/guide/iphone/open-features-with-accessibility-shortcut-iph3e2e31a5/17.0/ios/17.0) to turn Switch Control on and off. In macOS, you can press Command-F5.
- Navigate to Settings > Accessibility > Switch Control > Switches. Select Add New Switch, select a type of switch, then select an action for the switch. Alternatively, you can choose Bluetooth Devices, select a device to use as a switch, and select an action for that switch.
- When you’re ready to start testing, turn on Switch Control.

With Switch Control on, use Switch Control actions to navigate your app. Although you don’t need to become an expert Switch Control user to test your app with it, you do need to know several key actions. To learn more about Switch Control actions, read the platform-specific user guides listed in [`Switch Control`](switch-control.md).

**Assistive Access**:

- Install your app on a physical device, since Assistive Access isn’t available on Simulator.
- Learn how to turn Assistive Access off so you can exit it after testing. For example, triple-click the Home button or the Side button on certain devices at any time to exit Assistive Access. For more information, read [`Enter and exit Assistive Access on iPhone`](https://developer.apple.comhttps://support.apple.com/guide/assistive-access-iphone/enter-and-exit-assistive-access-devdedddc678/ios).
- Navigate to Settings > Accessibility > Assistive Access, and set up Assistive Access.
- Add your app to the list of available apps.
- When you’re ready to start testing, tap Start Assistive Access and enter the Assistive Access passcode.

With Assistive Access on, use standard system gestures to navigate your app. Assistive Access turns off the system edge swipe gesture, so you need to perform several key interactions in different ways:

- To unlock the device, tap the Open system button at the bottom of the screen.
- To navigate to the Home Screen, tap the Back system button at the bottom of the screen.
- For any interactions in your app that rely on edge swiping, like showing a sidebar or navigating a navigation stack, use buttons instead of swipes.

To learn more about using Assistive Access, read [`Assistive Access User Guide`](https://developer.apple.comhttps://support.apple.com/guide/assistive-access-iphone/welcome/ios).

##### Diagnose and Address Accessibility Issues

As you test your app’s workflows, make sure your app continues to provide a good user experience while accessibility settings and assistive technologies are on. Check that you can access every element and that the ordering of those elements is what you intend. Make note when you find it difficult to perform a task. Confirm that your UI adjusts appropriately when the system font size, color filter, or other visual settings change to something other than the default. You can use the following list as a starting point for ensuring that your app provides a good experience in various accessibility categories.

**Visual accessibility**:

- A user with low vision can perceive all UI elements, images, and text in your app.
- Your app doesn’t use color alone to convey information.
- Your app uses sufficient contrast for important UI elements.
- Your app responds to Dynamic Type accessibility text sizes by reflowing its layout, avoiding text truncation, and making sure UI elements don’t overlap for larger sizes.
- Your app responds to the Increase Contrast accessibility setting by increasing color contrast between background and foreground elements.
- Your app responds to the Button Shapes accessibility setting to indicate where button controls exist.
- Your app responds to the Reduce Motion accessibility setting by reducing excessive motion where appropriate.
- Your app responds to the Dim Flashing Lights accessibility setting by reducing flickering in the UI or videos.

**Media accessibility**:

- A user with limited hearing can make use of all media in your app.
- Your app contains audio descriptions for all video.
- Your app contains captions for all video.
- Your app contains transcripts for all video.

**VoiceOver**:

- A user can perform all tasks within your app using only VoiceOver.
- VoiceOver can output all information in the app.
- For each item in the UI, VoiceOver reports the UI element name and status correctly.

**Voice Control**:

- A user can perform all tasks within your app using only Voice Control.
- Voice Control can output all information in the app.
- For each item in the UI, Voice Control reports the UI element name and status correctly.

**Switch Control**:

- A user can perform all tasks within your app using only Switch Control.
- Switch Control can output all information in the app.
- For each item in the UI, Switch Control reports the UI element name and status correctly.

Take notes about any issues as you discover them so you can address them in your app’s design and implementation. If you encounter accessibility issues that you aren’t able to troubleshoot while testing on the device, try using [`Accessibility Inspector`](accessibility-inspector.md) to help diagnose and resolve issues. You can also automate accessibility testing by adding accessibility audits in your UI tests, as described in [`Perform accessibility audits for your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10035).

Address accessibility issues that you discover during testing so that you’re able to successfully complete all the tasks in your app when accessibility settings and assistive technologies are on.

## See Also

- [Accessibility updates](../updates/accessibility.md)
  Learn about important changes to Accessibility.
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
  Accessible user interfaces empower everyone to have a great experience with your app or game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app)*