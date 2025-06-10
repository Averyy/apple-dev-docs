# Information

**Framework**: Technology Overviews

Include helpful information in your interface and make it easy for people to find your app’s content.

Making information intuitive and accessible keeps people engaged with your app. Consider how you present content in your interface, and find ways to make using that content easier for people. For example, show a map with a street address or geographic landmark instead of a text description. Make the content you include easy to find by adopting search, and make content available in other parts of the system so people can access it multiple ways.

#### Make Content Easier to Find

Adding search capabilities to your app helps people find your content quickly. Even if your app doesn’t offer a [`Building a search interface for your app`](https://developer.apple.com/documentation/CoreSpotlight/building-a-search-interface-for-your-app), [`Adding your app’s content to Spotlight indexes`](https://developer.apple.com/documentation/CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes) makes it visible to Spotlight – the system-wide search tool. On Apple platforms, you create search interfaces and manage your app’s indexed content using [`Core Spotlight`](https://developer.apple.com/documentation/CoreSpotlight). Adopting Core Spotlight for search has some other advantages:

- People can find your content from the system’s Spotlight search interface.
- Siri can use content from your app’s indexes when responding to spoken requests.
- Apple Intelligence automatically performs a semantic analysis of your indexed content, allowing people to find your content based on semantic matches, in addition to lexical matches.

If your app creates [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects for relevant actions, add those objects to your app’s search indexes, too. For example, if a person views information about a particular restaurant in your app, create an activity object and set its [`isEligibleForSearch`](https://developer.apple.com/documentation/Foundation/NSUserActivity/isEligibleForSearch) property to `true`. If someone searches for restaurants later using Spotlight, the system can include the restaurant from your activity object in the results.

> **Note**: Core Spotlight stores app-specific indexes locally on the device and doesn’t share them with Apple or a person’s other devices.

#### Extend the Reach of Your Content

Apps are one way to access content, but making your content available in other parts of the system helps people stay engaged with that content.

-  elevate a small amount of timely, personally relevant information, and display it where people can see it at a glance. On iPhone and iPad, people put widgets in Today View, on the Home Screen, and on the Lock Screen. On the Mac, people put widgets on the desktop and in Notification Center. On Apple Watch, widgets appear in the [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit).
-  are small elements on the Apple Watch face that display timely, relevant information. Complications might display the current weather conditions, or provide quick access to apps.
-  display up-to-date content from your app. For example, they display event and task information on the Lock Screen or in the Dynamic Island. Live Activities use [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit) and the [`Setting up a remote notification server`](https://developer.apple.com/documentation/UserNotifications/setting-up-a-remote-notification-server) (APNs) to deliver timely information.
-  allow people to [`Creating controls to perform actions across the system`](https://developer.apple.com/documentation/WidgetKit/Creating-controls-to-perform-actions-across-the-system) in Control Center, the Lock Screen, and from a device’s Action button.

To support any of these features, create an [`App extensions`](app-extensions.md) using the [`WidgetKit`](https://developer.apple.com/documentation/WidgetKit) framework. Your app extension runs separately from your app and works with the system to display your content. Whenever possible, build your app extensions to run independently from your app. For example, design your app extension to fetch data over the network instead of sharing data with your app. However, you can share data between an app and app extension using a [`Share content on the same device`](shared-data#Share-content-on-the-same-device.md) if needed.

#### Provide Helpful Information From Your App

Incorporate contextual information to make your app’s content more useful and relevant. For example, a map with a restaurant’s location makes it easier to understand how close that restaurant is to the person’s current location than the address alone. Incorporate other types of contextual information that make sense for your app, including:

-  Embed Apple Maps content in your app’s interface using [`MapKit`](https://developer.apple.com/documentation/MapKit). Annotate the maps in your interface with points of interest and other custom information. You can also configure turn-by-turn navigation to specific addresses.
-  Obtain weather forecasts and data related to weather events for a particular location using [`WeatherKit`](https://developer.apple.com/documentation/WeatherKit). Display the weather information on its own or use it to make people aware of adverse weather conditions.
-  Help people discover your app’s new, interesting, or unused features using [`TipKit`](https://developer.apple.com/documentation/TipKit). The framework helps point out features people might otherwise miss, and isn’t a subsitute for general help information.
-  Display URLs in a content-rich and consistent way using [`Link Presentation`](https://developer.apple.com/documentation/LinkPresentation). This framework fetches metadata such as page titles, images, video, and audio from the destination of a URL. Display that metadata yourself or present it using a [`LPLinkView`](https://developer.apple.com/documentation/LinkPresentation/LPLinkView). You can also pass that metadata to the [`Activity views`](https://developer.apple.com/design/Human-Interface-Guidelines/activity-views) and other system experiences.
-  Detect common types of data in text using [`DataDetection`](https://developer.apple.com/documentation/DataDetection). This framework identifies dates, email addresses, flight numbers, web links, phone numbers, shipment tracking numbers, and other types of well-known data in text strings. It then provides that data in a more program-friendly format. For example, it provides a [`Date`](https://developer.apple.com/documentation/Foundation/Date) type for date and time information in the text. You might use the provided date type to suggest an addition to the person’s calendar.

#### Help People Manage Their Device Usage

People sometimes need help managing the time they or their children spend on their devices. The [`Screen Time`](https://developer.apple.com/documentation/ScreenTime) framework gives you a way to help parents and guardians supervise their child’s web usage and take action against prohibited URLs. The [`FamilyControls`](https://developer.apple.com/documentation/FamilyControls) framework prevents a child from circumventing the parental controls on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/information)*