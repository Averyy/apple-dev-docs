# datastoreLocation(_:)

**Framework**: TipKit  
**Kind**: method  
**Role**: Type Method

Specify a custom location for your tips datastore.

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
static func datastoreLocation(_ storeLocation: Tips.ConfigurationOption.DatastoreLocation) -> Tips.ConfigurationOption
```

## Overview

Use `datastoreLocation` to change the on-disk location of your tips persistent storage.

By default `URL.applicationSupportDirectory` is used on macOS, iOS, watchOS, and visionOS.

On tvOS, `URL.cachesDirectory` is used by default in conjunction with `UserDefaults` to manage tip statuses.

```swift
@main
struct SampleApp: App {
    init() {
        do {
            // Save the tips datastore in a group container.
            try Tips.configure([
                .datastoreLocation(.groupContainer(identifier: "group.com.apple.TipKitTrails"))
            ])
        }
        catch {
            // Handle TipKit errors
            print("Error initializing TipKit \(error.localizedDescription)")
        }
    }
}
```

### Datastore Location Values

- [`applicationDefault`](./datastorelocation/applicationdefault.md)
  The default location for persisting tips, which is generally your application’s support directory.
- [`groupContainer(identifier:)`](./datastorelocation/groupcontainer%28identifier%29.md)
  DatastoreLocation for persisting tips in a group container.
- [`url(_:)`](./datastorelocation/url%28_%29.md)
  Configuration option for persisting tips at a custom on-disk location.

## See Also

### Configuration
- [static func configure([Tips.ConfigurationOption]) throws](../configure%28_%29.md)
  Loads and configures the persistent state of all tips in your app.
- [static func cloudKitContainer(Tips.ConfigurationOption.CloudKitContainer?) -> Tips.ConfigurationOption](./cloudkitcontainer%28_%29.md)
  Sets the CloudKit container used for syncing tips.
- [static func displayFrequency(Tips.ConfigurationOption.DisplayFrequency) -> Tips.ConfigurationOption](./displayfrequency%28_%29.md)
  Customizes how often new tips are presented in your app after another tip has been displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption/datastorelocation(_:))*