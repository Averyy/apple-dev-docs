# System experiences

**Framework**: Technology Overviews

Extend the reach of your app by supporting system experiences that make your content available in other places.

Experiences like Widgets, Live Activities, watch complications, and others help you put your app’s content in front of people in different contexts. These experiences create glanceable information on the Lock Screen or Home Screen of a device, providing important details and updates quickly. Other experiences are an extension of your app’s capabilities, and make your content available in places where people need it, like their vehicle. Support different experiences to give people options for how to interact with your content.

## Widgets

Widgets elevate a small amount of timely, personally relevant information, and display it where people can see it at a glance. Apple platforms support widgets in a variety of places:

- On iPhone and iPad, people put widgets in the Today View, on the Home Screen, and on the Lock Screen. People can also stack widgets on the Home Screen to create a Smart Stack, which shows the most contextually relevant widget in the moment.
- On Mac, people put Mac app widgets on the desktop and in Notification Center. People can also put widgets from their iOS app on the Mac desktop.
- On Apple Watch, widgets appear in the [Smart Stack](../WidgetKit/WidgetKit.md). You also create [complications](./system-experiences.md#Watch-complications) for Apple Watch as widgets.
- On Apple Vision Pro, widgets become three-dimensional objects that people pin to horizontal and vertical surfaces.
- In vehicles, people can add widgets to the CarPlay interface to see the information while driving.

Widgets come in a [variety of sizes](../WidgetKit/widgetfamily.md) and are primarily informational, displaying app-specific content with no or only a few interactive controls. Use your widget to to offer app-specific content that people might want to view from anywhere. For example, a weather app might display the latest forecast or top stories about the weather. Support as many widget sizes as possible to give people choices for how to display it. Some experiences work only with specific widget sizes: make sure to support the ones that matter for your content.

Deliver your app’s widgets using a [Widget extension](../WidgetKit/creating-a-widget-extension.md) that you include inside your app bundle. The code for each widget provides the system with SwiftUI views with the information to display and a [timeline](../WidgetKit/keeping-a-widget-up-to-date.md) for when to display them. When someone adds your widget to the Home Screen or to another system experience, the system runs your widget’s code periodically to create views and timeline entries. When your app receives new data, you can [update your widget](../WidgetKit/widgetcenter.md) programmatically to force the system to refresh your widget.

On Apple Watch, [increase the visibility of widgets](../WidgetKit/widget-suggestions-in-smart-stacks.md) in Smart Stacks by supplying contextual clues about their relevance. You can construct contextual clues based on a location, time, or other conditions. For example, you might ask the system to elevate the widget for your music player app when someone connects their headphones to the device.

## Live Activities

Live Activities display time-sensitive content prominently on someone’s device and update it regularly as the content changes. An airline app uses Live Activities to display flight information and communicate schedule changes and gate information. A food-ordering app uses Live Activities to show the current status of an ordern and its expected delivery time. A parking app might use a Live Activity to show the amount of time remaining and give someone a way to extend the amount of time they remain parked. Live Activities can appear as widgets on the Lock Screen, or in a minimal form in the Dynamic Island of a device.

Deliver your app’s Live Activities using the same [Widget extension](../WidgetKit/creating-a-widget-extension.md), you use to deliver your app’s widgets, and types from the [ActivityKit](../ActivityKit/ActivityKit.md) framework. When adding this extension to your app, enable the Include Live Activity checkbox to generate the initial code for your Live Activity. If you already have a widget extension, you can also add the [configuration object](../WidgetKit/activityconfiguration.md) for your Live Activity to your existing code. The configuration object provides the SwiftUI views and Dynamic Island content to display for your Live Activity.

Update the content in your Live Activity using the [ActivityKit](../ActivityKit/ActivityKit.md) and the [Apple Push Notification service](../UserNotifications/setting-up-a-remote-notification-server.md) (APNs). Live Activities often require frequent updates, and these technologies help you deliver updates in a timely manner.

## Controls

Controls allow people to [perform app-specific actions](../WidgetKit/creating-controls-to-perform-actions-across-the-system.md) in Control Center, the Lock Screen, and from a device’s Action button. Create a control for your app when you want to give someone a quick way to execute one of your app’s actions. A photography app might offer a control to launch the app’s capture interface to begin taking new photos. A productivity app might offer a toggle control to put the app in a specific mode. Include controls in a Widget extension inside your app bundle.

Deliver your app’s controls using the same [Widget extension](../WidgetKit/creating-a-widget-extension.md) you use to deliver your app’s widgets. When adding this extension to your app in Xcode, enable the Include Control checkbox to generate the initial code for your control. If you already have a widget extension, you can also add a [control widget](../SwiftUI/controlwidget.md) to your existing code.

Controls handle interactions with the help of the [App Intents](../AppIntents/AppIntents.md) framework. App intents define specific actions your app is able to perform. For example, a music player app might define app intents to [play audio](../AppIntents/appschema/audiointent/playaudio.md) or [add an item](../AppIntents/appschema/audiointent/addtoplaylist.md) to a playlist. You specify which app intent to call in the control’s configuration, and the system runs that app intent when someone interacts with the control.

## Watch complications

Watch complications are small elements on the Apple Watch face that display timely, relevant information. A weather app on watchOS might provide complications to display the current temperature or weather conditions, while a calendar app might show upcoming events. Tapping on a complication launches the app itself to display more detailed information.

Complications are widgets that conform to [specific sizes](../WidgetKit/widgetfamily.md), so you deliver them using a [Widget extension](../WidgetKit/creating-a-widget-extension.md). Like other widgets, your code tells the system which SwiftUI views to display and when to display them. The [timeline](../WidgetKit/keeping-a-widget-up-to-date.md) data you provide includes the time or condition at which to display a specific set of views. Update timelines programmatically from your app or app extension, or deliver updates using [push notifications](../WidgetKit/updating-widgets-with-widgetkit-push-notifications.md).

## CarPlay

CarPlay is a smarter, safer way to use iPhone in the car. If your app offers content that’s relevant in a vehicle, build a [CarPlay version](../CarPlay/CarPlay.md) of your interface. When someone connects their iPhone to a CarPlay-equipped vehicle, apps that support CarPlay appear on the in-vehicle display. After launching the app, people use your app’s CarPlay interface to navigate and interact with your content.

> **Note**: CarPlay audio and video apps also run on Apple HomeView without any modifications.

To support CarPlay, add a [CarPlay-specific scene](../CarPlay/cptemplateapplicationscene.md) to your existing iOS app. The scene provides your app’s initial interface and code to navigate to other parts of your app. Instead of views and windows, build your CarPlay interface from [templates](../CarPlay/CarPlay.md), which present the data you specify in a predefined style. CarPlay renders templates specifically for the target vehicle, handling differences between display sizes and environment settings.

Build a CarPlay version of your app if it:

- Plays [audio](../BundleResources/entitlements/com.apple.developer.carplay-audio.md) or [video](../BundleResources/entitlements/com.apple.developer.carplay-video.md) content.
- Offers [turn-by-turn navigation](../BundleResources/entitlements/com.apple.developer.carplay-maps.md).
- Offers [messaging or VoIP calling](../BundleResources/entitlements/com.apple.developer.carplay-communication.md) features.
- Provides [services](../BundleResources/entitlements/com.apple.developer.carplay-driving-task.md) that are essential to the driving experience.
- Provides information about [EV charging](../BundleResources/entitlements/com.apple.developer.carplay-charging.md), [fueling](../BundleResources/entitlements/com.apple.developer.carplay-fueling.md), or [parking](../BundleResources/entitlements/com.apple.developer.carplay-parking.md) facilities.
- Supports [public safety organizations](../BundleResources/entitlements/com.apple.developer.carplay-public-safety.md) in the performance of their duties.
- Allows people to order food from [quick service restaurants](../BundleResources/entitlements/com.apple.developer.carplay-quick-ordering.md).
- Offers a [voice-based conversational assistant](../BundleResources/entitlements/com.apple.developer.carplay-voice-based-conversation.md).

## App Clips

An App Clip is a lightweight version of your app that performs one task quickly, When someone doesn’t have your app, they can use an App Clip code, QR code, NFC reader, or other technique to access a service using your App Clip instead. For example, a scooter rental app might provide an App Clip code allowing someone to rent a scooter without requiring them to download the full version of your app. This convenience can convince people to download the full version of your app later.

[Create an App Clip](../AppClip/creating-an-app-clip-with-xcode.md) in Xcode by adding an App Clip target to your project. Use the [App Clips](../AppClip/AppClip.md) framework to implement your clip, and add any app-specific code you need to complete the intended task. Limit your App Clip to the most essential service you offer, and include the minimal set of code and resources in your App Clip bundle.

In addition to [uploading your App Clip](../AppClip/distributing-your-app-clip.md) to the App Store, [create the App Clip codes](../AppClip/creating-app-clip-codes.md) people use to access launch your App Clip. Include these codes in promotional materials or in the place where people encounter your services and need to use your App Clip.

Additional things to know when creating an App Clip include:

- You need to adopt [universal links](./convenience.md#Provide-consistent-URLs-for-app-content) for tasks you want people to perform. The processes that launch your App Clip contain the URL of the associated task.
- You can use your App Clip to [recommend your full app](../AppClip/recommending-your-app-to-app-clip-users.md) to people. A useful App Clip is good encouragement for someone to download your app.
- Your App Clip can [schedule and receive notifications](../AppClip/enabling-notifications-in-app-clips.md) for a short period of time. For example, a scooter rental App Clip might send notifications when the rental is about to expire, and give someone the option to extend the rental time.
- Your App Clip can include [Live Activities](./system-experiences.md#Live-Activities), which you might use to inform someone about the progress of a task. For example, you might display the time remaining on a scooter rental.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/system-experiences)*