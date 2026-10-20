# configure(_:)

**Framework**: TipKit  
**Kind**: method

Loads and configures the persistent state of all tips in your app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func configure(_ configuration: [Tips.ConfigurationOption] = []) throws
```

#### Discussion

> **Note**: This function must be called before tips display in your app.

Call this function during app initialization. By default, all tips persist to a default location with a display frequency of [`immediate`](tips/configurationoption/displayfrequency/immediate.md).

```swift
@main
struct SampleApp: App {
    init() {
        do {
            // Configure tips in the app.
            try Tips.configure()
        }
        catch {
            // Handle TipKit errors
            print("Error initializing TipKit \(error.localizedDescription)")
        }
    }
}
```

To change the default location of where your tips persist use the convenience method [`datastoreLocation(_:)`](tips/configurationoption/datastorelocation(_:).md).

To change the display frequency use the convenience method [`displayFrequency(_:)`](tips/configurationoption/displayfrequency(_:).md).

```swift
do {
    // Configure tips in the app.
    try Tips.configure([
        .datastoreLocation(.groupContainer(identifier: "MyGroupContainer")),
        .displayFrequency(.hourly)
    ])
}
catch {
    // Handle TipKit errors
    print("Error initializing TipKit \(error.localizedDescription)")
}
```

## Parameters

- `configuration`: An array of options for customizing your tip’s datastore location and default frequency control interval.

## See Also

- [static func cloudKitContainer(Tips.ConfigurationOption.CloudKitContainer?) -> Tips.ConfigurationOption](tips/configurationoption/cloudkitcontainer(_:).md)
  Sets the CloudKit container used for syncing tips.
- [static func datastoreLocation(Tips.ConfigurationOption.DatastoreLocation) -> Tips.ConfigurationOption](tips/configurationoption/datastorelocation(_:).md)
  Specify a custom location for your tips datastore.
- [static func displayFrequency(Tips.ConfigurationOption.DisplayFrequency) -> Tips.ConfigurationOption](tips/configurationoption/displayfrequency(_:).md)
  Customizes how often new tips are presented in your app after another tip has been displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configure(_:))*