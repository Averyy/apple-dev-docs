---
url: https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos
framework: HIG
---

# Designing for watchOS

**Type:** article

> **Updated 2023-06-05:** Enhanced guidance for providing a glanceable, focused app experience, and emphasized the importance of the Digital Crown in navigation.

When people glance at their Apple Watch, they know they can access essential information and perform simple, timely tasks whether they’re stationary or in motion.

![A stylized representation of an Apple Watch frame shown on top of a grid. The image is overlaid with rectangular and circular grid lines and is tinted green to subtly reflect the green in the original six-color Apple logo.](/images/com.apple.HIG/platforms-watchOS-intro~dark@2x.png)
As you begin designing your app for Apple Watch, start by understanding the following fundamental device characteristics and patterns that distinguish the watchOS experience. Using these characteristics and patterns to inform your design decisions can help you provide an app that Apple Watch users appreciate.
**Display.** The small Apple Watch display fits on the wrist while delivering an easy-to-read, high-resolution experience.
**Ergonomics.** Because people wear Apple Watch, they’re usually no more than a foot away from the display as they raise their wrist to view it and use their opposite hand to interact with the device. In addition, the Always On display lets people view information on the watch face when they drop their wrist.
**Inputs.** People can navigate vertically or inspect data by turning the [Digital Crown](digital-crown.md), which offers consistent control on the watch face, the Home Screen, and within apps. They can provide input even while they’re in motion with standard [gestures](gestures.md) like tap, swipe, and drag. Pressing the [Action button](action-button.md) initiates an essential action without looking at the screen, and using [shortcuts](siri.md#Shortcuts-and-suggestions) helps people perform their routine tasks quickly and easily. People can also take advantage of data that device features provide, such as GPS, sensors for blood oxygen and heart function, and the altimeter, accelerometer, and gyroscope.
**App interactions.** People glance at the Always On display many times throughout the day, performing concise app interactions that can last for less than a minute each. People frequently use a watchOS app’s related experiences — like complications, notifications, and Siri interactions — more than they use the app itself.
**System features.** watchOS provides several features that help people interact with the system and their apps in familiar, consistent ways.
- [Complications](complications.md)
- [Notifications](notifications.md)
- [Always On](always-on.md)
- [Watch faces](watch-faces.md)

## Best practices
Great Apple Watch experiences are streamlined and specialized, and integrate the platform and device capabilities that people value most. To help your experience feel at home in watchOS, prioritize the following ways to incorporate these features and capabilities.
- Support quick, glanceable, single-screen interactions that deliver critical information succinctly and help people perform targeted actions with a simple gesture or two.
- Minimize the depth of hierarchy in your app’s navigation, and use the [Digital Crown](digital-crown.md) to provide vertical navigation for scrolling or switching between screens.
- Personalize the experience by proactively anticipating people’s needs and using on-device data to provide actionable content that’s relevant in the moment or very soon.
- Use [complications](complications.md) to provide relevant, potentially dynamic data and graphics right on the watch face where people can view them on every wrist raise and tap them to dive straight into your app.
- Use [notifications](notifications.md) to deliver timely, high-value information and let people perform important actions without opening your app.
- Use background content such as [color](color.md) to convey useful supporting information, and use  [materials](materials.md) to illustrate hierarchy and a sense of place.
- Design your app to function independently, complementing your notifications and complications by providing additional details and functionality.

## Resources

#### Related
[Apple Design Resources](https://developer.apple.com/design/resources/#watchos-apps)

#### Developer documentation
[watchOS Pathway](https://developer.apple.com/watchos/get-started/)

#### Videos
- [What’s new in watchOS 26](https://developer.apple.com/videos/play/wwdc2025/334) - Discover the new features in watchOS 26 and learn how to integrate them into your watchOS and iOS apps. Explore the ARM64 architecture, and dive into the new design system. We’ll also share updates for widgets and insights on how to bring controls to Apple Watch.

## Change log
| Date | Changes |
| --- | --- |
| June 5, 2023 | Enhanced guidance for providing a glanceable, focused app experience, and emphasized the importance of the Digital Crown in navigation. |




---
*Source: [https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)*
