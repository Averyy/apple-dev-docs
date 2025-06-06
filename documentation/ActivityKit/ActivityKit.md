# ActivityKit

**Framework**: Activitykit  
**Kind**: module

Share live updates from your app as Live Activities in the Dynamic Island, on the Lock Screen, and on the Smart Stack in watchOS.

**Availability**:
- iOS 16.1+
- iPadOS 17.0+
- Mac Catalyst 16.1+
- watchOS 11.0+

#### Overview

With the ActivityKit framework, you can start a Live Activity to share live updates from your app in the Dynamic Island and on the Lock Screen. Especially for apps that push the limit of notifications to provide updated information, Live Activities can offer a richer, interactive and highly glanceable way for people to keep track of an event or activity over a couple of hours. For example, a sports app might start a Live Activity that makes live information available at a glance for the duration of a game.

A Live Activity appears in highly visible contexts:

- On the Lock Screen of iPhone and iPad, it appears at the top of the list alongside notifications.
- On devices that support it, the Live Activity appears in the Dynamic Island.
- On iPhone in StandBy, it appears using a minimal presentation at the top of the screen or scaled to fill the display.
- On the Home Screen and when other apps are in use, updates appear as a banner at the top of the screen of devices that don’t support the Dynamic Island if the update includes an alert configuration.
- In the Smart Stack in watchOS, the leading and trailing view for the Dynamic Island appear together to form the Live Activity.

> **Note**: [`Session 10184: Meet ActivityKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10184), [`Session 10185: Update Live Activities with push notifications`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10185), and [`Session 10194: Design dynamic Live Activities`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10194)

In addition to viewing real-time information, people tap a Live Activity to launch your app and interact with its buttons or toggles to perform essential functionality without launching your app. In the Dynamic Island, people touch and hold the compact and minimal presentations to show an expanded presentation with more content that feels like a peek into your app.

![Three screenshots of iPhone that show a Live Activity for a delivery app. They show the Live Activity on the Lock Screen, in the leading and trailing presentations in the Dynamic Island, and in the expanded presentation.](https://docs-assets.developer.apple.com/published/a81e13e284bbdea7bed42f642b5d9ee5/live-activity-dynamic-island%402x.png)

In your app, use ActivityKit to configure, start, update, and end the Live Activity, and create the user interface of your Live Activities with a widget extension, [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI), and [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit). As a result of using SwiftUI and WidgetKit, you can share code between widgets and Live Activities or develop them in tandem.

However, Live Activities use a different mechanism to receive updates compared to widgets. Instead of using a timeline mechanism, Live Activities receive updated data from your app with ActivityKit and remotely with ActivityKit push notifications. Starting with iOS 17.2 and iPadOS 17.2, you can also start Live Activities with ActivityKit push notifications.

> **Note**: visionOS doesn’t load WidgetKit extensions found in compatible iPad and iPhone apps. As a result, it doesn’t support Live Activities.

## Topics

### Essentials
- [Developing a WidgetKit strategy](../WidgetKit/Developing-a-WidgetKit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, watch complications, and Live Activities.
- [ActivityKit updates](../Updates/ActivityKit.md)
  Learn about important changes in ActivityKit.
### Live Activity implementation
- [Displaying live data with Live Activities](displaying-live-data-with-live-activities.md)
  Display your app’s data in the Dynamic Island and on the Lock Screen and offer quick interactions.
- [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md)
  Use ActivityKit to receive push tokens and to remotely start, update, and end your Live Activity with ActivityKit notifications.
- [Adding accessible descriptions to widgets and Live Activities](adding-accessible-descriptions-to-widgets-and-live-activities.md)
  Describe the interface elements of your widgets and Live Activities to help people understand what they represent.
- [class Activity](activity.md)
  The object you use to start, update, and end a Live Activity.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](../WidgetKit/emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [NSSupportsLiveActivities](../BundleResources/Information-Property-List/NSSupportsLiveActivities.md)
  A Boolean value that indicates whether an app supports Live Activities.
- [NSSupportsLiveActivitiesFrequentUpdates](../BundleResources/Information-Property-List/NSSupportsLiveActivitiesFrequentUpdates.md)
  A Boolean value that indicates whether an app can update its Live Activities frequently.
### Widget extensions
- [WidgetKit](../WidgetKit/WidgetKit.md)
  Extend the reach of your app by creating widgets, watch complications, Live Activities, and controls.
- [Creating a widget extension](../WidgetKit/Creating-a-Widget-Extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Animating data updates in widgets and Live Activities](../WidgetKit/Animating-data-updates-in-widgets-and-live-activities.md)
  Use SwiftUI animations to indicate data updates in your widgets and Live Activities.
### User interface
- [Creating views for widgets, Live Activities, and watch complications](../WidgetKit/Creating-views-for-widgets-Live-Activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [Linking to specific app scenes from your widget or Live Activity](../WidgetKit/Linking-to-specific-app-scenes-from-your-widget-or-Live-Activity.md)
  Add deep links to your widgets and Live Activities that enable people to open a specific scene in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ActivityKit)*