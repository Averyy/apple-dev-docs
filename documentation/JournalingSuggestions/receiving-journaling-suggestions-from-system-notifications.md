# Receiving journaling suggestions system notifications

**Framework**: Journaling Suggestions

Register your app to receive journaling suggestions when a person taps a system notification.

#### Overview

When the Journaling Suggestions and notifications settings are on, the system reminds people to journal and reflect on recent moments through periodic notifications. When someone taps a notification, the system launches the journal app indicated in the Open Notifications With setting.

The person chooses the specific app the system launches using the Settings > Notifications > Journaling Suggestions > Customize Notifications > Open Notifications With setting when multiple journal apps exist on the device that support Journaling Suggestions notifications.

If a tapped notification refers to a specific moment, the app displays the Journaling Suggestions picker prepopulated with the moment’s details. To pass along the details, the system provides the app with a URL that contains the journaling suggestion’s unique ID. The app prepopulates the picker with the details by parsing the URL and intializing the journaling suggestion picker with the ID. In the picker, the person chooses which information from the moment to write about. As the person progresses through the interface, the system returns the details to the app as a [`JournalingSuggestion`](journalingsuggestion.md) object.

> **Note**: To display the Journaling Suggestions picker, the system requires your app to have the [`com.apple.developer.journal.allow`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.journal.allow) entitlement. Add it to your app’s target by enabling the Journaling Suggestions capability in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

#### Add the Notification Url Target Property

When you add the [`JSNotificationURLFormat`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/JSNotificationURLFormat) target property to your app, the system adds your app as an available option in the Open Notifications With setting. The value you choose needs to be a , which also defines how the system provides notification information to your app. The format of the link is a base URL for your app, followed by the parameter string: `{journaling-suggestion-id}`, which represents the unique journaling suggestion. For example:

```http
<base_URL>/{journaling-suggesion-id}
```

As an alternative to including the parameter string as a path component, you can define it as a query argument. The following example specifies query argument `suggestion-identifier`:

```http
<base_URL>/?suggestion-identifier={journaling-suggesion-id}
```

The base URL is composed of a protocol identifier, your app’s domain name, and a unique path component that scopes the request to a journaling suggestion:

```http
<protocol_identifier><domain_name>/<path_component>
```

Here are complete example [`JSNotificationURLFormat`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/JSNotificationURLFormat) target property values:

```http
# Example value in path-component format:
http://myapp.com/journaling-suggestion/{journaling-suggesion-id}

# Example value with a query-parameter argument:
http://myapp.com/journaling-suggestion-notification/?suggestion-identifier={journaling-suggesion-id}
```

When a tapped notification refers to a specific moment and the system passes your app an URL of the specified format, it replaces `{journaling-suggesion-id}` with the ID of the moment, for example:

```http
# Example URL in path-component format:
http://myapp.com/journaling-suggestion/A5A193F6-5C20-4844-AA67-1BD95F94CBB8

# Example URL with a query-parameter argument:
http://myapp.com/journaling-suggestion-notification/?suggestion-identifier=A5A193F6-5C20-4844-AA67-1BD95F94CBB8
```

For more information on universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

#### Handle Notification Taps

The system invokes your app using the link when a person taps a journaling suggestion notification and your app is the selected app to open from notifications. In SwiftUI, your app’s view launches with the [`onOpenURL(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onOpenURL(perform:)) view modifier. Access the URL in the `url` argument:

```swift
struct Example: App {
    @State private var suggestionPresentationToken: 
                            JournalingSuggestionPresentationToken?
    @State private var presentPicker = false
    var body: some Scene {
        WindowGroup {
            ExampleView(presentPicker: $presentPicker, 
                                token: $suggestionPresentationToken)
                .onOpenURL { url in
                    // ...
```

Parse the `url` according to your app’s URL format. The following code assumes the query argument `suggestion-identifier`:

```swift
if let components = URLComponents(url: url, 
              resolvingAgainstBaseURL: false),
   let queryItems = components.queryItems,
   let suggestionIDString = queryItems.first(where: { 
        queryItem -> Bool in queryItem.name == 
            "suggestion-identifier" }).value,
```

If the notification is a general reminder, the ID portion of the URL is empty. Check for a value and create a [`JournalingSuggestionPresentationToken`](journalingsuggestionpresentationtoken.md) with the ID if the value is present:

```swift
if let suggestionID =  UUID(uuidString: suggestionIDString) {
 presentPicker = true
 suggestionPresentationToken = JournalingSuggestionPresentationToken(
    suggestionIdentifier: suggestionID)
}
```

Display a [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md) with the token by passing it to the [`journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)) view modifier, which enables the picker to preload its contents with the notified suggestion:

```swift
struct ExampleView: View {
    @Binding var presentPicker: Bool
    @Binding var token: JournalingSuggestionPresentationToken?
    var body: some View {        
        journalingSuggestionsPicker(
            isPresented: $presentPicker,
            journalingSuggestionToken: token,
            onCompletion: { suggestion in
                // ...
```

> **Note**: If your app implements an app delegate, see  [`Supporting universal links in your app`](https://developer.apple.com/documentation/Xcode/supporting-universal-links-in-your-app#Update-your-app-delegate-to-respond-to-a-universal-link) to update your app delegate to receive the universal link.

#### Display the Notification Schedule

When your app uses the [`JournalingSuggestionsConfiguration`](journalingsuggestionsconfiguration.md) class, your app can determine if notifications are on and whether the person sets a specific notification schedule, or allows the system to determine the schedule. The person configures notifications in Settings, and your app can remind them of the feature, for example, by displaying the setting’s current value in a view:

```swift
struct ContentView: View {
    /// Create a configuration instance.
    @State private var config = JournalingSuggestionsConfiguration()

    // Defined a view that adds text based on the notification setting. 
    var body: some View {
        switch (config.notificationSchedule) {
        case .smart:
            Text("Notification: Smart schedule")
        case .custom:
            Text("Notification: Custom schedule")
        case .off:
            Text("Notification: Off")
        }
    }
}
```

When [`notificationSchedule`](journalingsuggestionsconfiguration/notificationschedule-swift.property.md) is [`JournalingSuggestionsConfiguration.NotificationSchedule.smart`](journalingsuggestionsconfiguration/notificationschedule-swift.enum/smart.md), the system personalizes the schedule according to the person’s unique routines. The value is [`JournalingSuggestionsConfiguration.NotificationSchedule.custom`](journalingsuggestionsconfiguration/notificationschedule-swift.enum/custom.md) if the person chooses a specific schedule in Settings.

A [`JournalingSuggestionsConfiguration.NotificationSchedule.off`](journalingsuggestionsconfiguration/notificationschedule-swift.enum/off.md) value can mean:

- Journaling Suggestions aren’t enabled in Settings.
- Your app isn’t a preferred journal app in Settings.
- Journaling Suggestions are on but notifications are off in Settings.
- Your app has incomplete notification setup, for example, it’s missing the [`JSNotificationURLFormat`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/JSNotificationURLFormat) target property.

#### Configure Settings to Open Your App From Notifications

To test how your app responds to tapped Journaling Suggestions notifications, follow the same process a person uses to select your app in Settings:

- Complete the one-time Journaling Suggestions enrollment process, if you haven’t already, by opening the system Journal app, or your app with the Journaling Suggestions capability enabled. Accept the Journaling Suggestions prompt, and tap Turn on Journaling Suggestions.
- Enable Journaling Suggestions notifications by accepting an additional prompt during enrollement, or by toggling the Settings > Notifications > Journaling Suggestions > Allow Notifications switch control.
- Run your app once with the [`JSNotificationURLFormat`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/JSNotificationURLFormat) target property present, which causes the system to add your app as an available option in the Settings > Notifications > Journaling Suggestions > Customize Notifications > Open Notifications With setting if multiple journal apps exist on the device that support Journaling Suggestions notifications.

## See Also

- [struct JournalingSuggestionPresentationToken](journalingsuggestionpresentationtoken.md)
  A container for a Journaling Suggestion identifier.
- [class JournalingSuggestionsConfiguration](journalingsuggestionsconfiguration.md)
  The configuration for Journaling Suggestion notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/receiving-journaling-suggestions-from-system-notifications)*