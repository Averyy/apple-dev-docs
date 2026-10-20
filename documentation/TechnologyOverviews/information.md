# Information

**Framework**: Technology Overviews

Include helpful information in your interface and make it easy for people to find your app’s content.

Making information intuitive and accessible keeps people engaged with your app. Consider how you present content in your interface, and find ways to make using that content easier for people. For example, show a map with a street address or geographic landmark instead of a text description. Make the content you include easy to find by adopting search, and make content available in other parts of the system so people can access it multiple ways.

---

#### Make your app’s content searchable

Adding search capabilities to your app helps people find your content quickly. Even if your app doesn’t offer a [search interface](../CoreSpotlight/building-a-search-interface-for-your-app.md), [indexing your app’s content](../CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes.md) makes it visible to Spotlight – the system-wide search tool. On Apple platforms, you create search interfaces and manage your app’s indexed content using [Core Spotlight](../CoreSpotlight/CoreSpotlight.md). Adopting Core Spotlight for search has some other advantages:

- People can find your content from the system’s Spotlight search interface.
- Siri can use content from your app’s indexes when responding to spoken requests.
- Apple Intelligence automatically performs a semantic analysis of your indexed content, allowing people to find your content based on semantic matches, in addition to lexical matches.

If your app creates [`NSUserActivity`](../Foundation/nsuseractivity.md) objects for relevant actions, add those objects to your app’s search indexes, too. For example, if a person views information about a particular restaurant in your app, create an activity object and set its [`isEligibleForSearch`](../Foundation/nsuseractivity/iseligibleforsearch.md) property to `true`. If someone searches for restaurants later using Spotlight, the system can include the restaurant from your activity object in the results.

> **Note**: Core Spotlight stores app-specific indexes locally on the device and doesn’t share them with Apple or a person’s other devices.

---

#### Extend the reach of your content

Apps are one way to access content, but making your content available in other parts of the system helps people stay engaged with that content.

- **Widgets** elevate a small amount of timely, personally relevant information, and display it where people can see it at a glance. On iPhone and iPad, people put widgets in Today View, on the Home Screen, and on the Lock Screen. On the Mac, people put widgets on the desktop and in Notification Center. On Apple Watch, widgets appear in the [Smart Stack](../WidgetKit/WidgetKit.md).
- **Watch complications** are small elements on the Apple Watch face that display timely, relevant information. Complications might display the current weather conditions, or provide quick access to apps.
- **Live Activities** display up-to-date content from your app. For example, they display event and task information on the Lock Screen or in the Dynamic Island. Live Activities use [ActivityKit](../ActivityKit/ActivityKit.md) and the [Apple Push Notification service](../UserNotifications/setting-up-a-remote-notification-server.md) (APNs) to deliver timely information.
- **Controls** allow people to [perform app-specific actions](../WidgetKit/creating-controls-to-perform-actions-across-the-system.md) in Control Center, the Lock Screen, and from a device’s Action button.

To support any of these features, create an [app extension](./app-extensions.md) using the [WidgetKit](../WidgetKit/WidgetKit.md) framework. Your app extension runs separately from your app and works with the system to display your content. Whenever possible, build your app extensions to run independently from your app. For example, design your app extension to fetch data over the network instead of sharing data with your app. However, you can share data between an app and app extension using a [shared group container](./shared-data.md#Share-content-on-the-same-device) if needed.

On Apple Watch, [increase the visibility of widgets](../WidgetKit/widget-suggestions-in-smart-stacks.md) in Smart Stacks by supplying contextual clues about their relevance. You can construct contextual clues based on a location, time, or other conditions. For example, you might ask the system to elevate the widget for your music player app when someone connects their headphones to the device.

---

#### Provide helpful information from your app

Incorporate contextual information to make your app’s content more useful and relevant. For example, a map with a restaurant’s location makes it easier to understand how close that restaurant is to the person’s current location than the address alone. Incorporate other types of contextual information that make sense for your app, including:

- **Maps.** Embed Apple Maps content in your app’s interface using [MapKit](../MapKit/MapKit.md). Annotate the maps in your interface with points of interest and other custom information. You can also configure turn-by-turn navigation to specific addresses. Specify rich placename information using the [GeoToolbox](../GeoToolbox/GeoToolbox.md) framework.
- **Weather.** Obtain weather forecasts and data related to weather events for a particular location using [WeatherKit](../WeatherKit/WeatherKit.md). Display the weather information on its own or use it to make people aware of adverse weather conditions.
- **Tips.** Help people discover your app’s new, interesting, or unused features using [TipKit](../TipKit/TipKit.md). The framework helps point out features people might otherwise miss, and isn’t a subsitute for general help information.
- **Rich-content links.** Display URLs in a content-rich and consistent way using [Link Presentation](../LinkPresentation/LinkPresentation.md). This framework fetches metadata such as page titles, images, video, and audio from the destination of a URL. Display that metadata yourself or present it using a [provided view](../LinkPresentation/lplinkview.md). You can also pass that metadata to the [Share Sheet](https://developer.apple.com/design/human-interface-guidelines/activity-views) and other system experiences.
- **Data detection.** Detect common types of data in text using [DataDetection](../DataDetection/DataDetection.md). This framework identifies dates, email addresses, flight numbers, web links, phone numbers, shipment tracking numbers, and other types of well-known data in text strings. It then provides that data in a more program-friendly format. For example, it provides a [`Date`](../Foundation/date.md) type for date and time information in the text. You might use the provided date type to suggest an addition to the person’s calendar.
- **Energy information.** Help people manage their energy usage using [EnergyKit](../EnergyKit/EnergyKit.md). This framework provides a forecast of grid power at the person’s location to help them determine the best time to use electricity. Incorporate it into apps that manage appliance usage, EV charging, home thermostats, and other home devices.

---

#### Help people manage their device usage

People sometimes need help managing the time they or their children spend on their devices. The [Screen Time](../ScreenTime/ScreenTime.md) framework gives you a way to help parents and guardians supervise their child’s web usage and take action against prohibited URLs. The [Family Controls](../FamilyControls/FamilyControls.md) framework prevents a child from circumventing the parental controls on their device.

If your app offers content suitable for specific age ranges, the [Declared Age Range](../DeclaredAgeRange/DeclaredAgeRange.md) framework offers a way to validate someone’s age in a privacy-friendly way. For actions that require parental approval, the [PermissionKit](../PermissionKit/PermissionKit.md) framework gives children a way to request permission before performing the action. For example, a parent might require their child to obtain permission before messaging unknown persons online.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/information)*