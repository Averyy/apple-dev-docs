# cloudKitContainer(_:)

**Framework**: TipKit  
**Kind**: method  
**Role**: Type Method

Sets the CloudKit container used for syncing tips.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func cloudKitContainer(_ cloudKitContainer: Tips.ConfigurationOption.CloudKitContainer?) -> Tips.ConfigurationOption
```

#### Overview

Use `cloudKitContainer` to sync TipKit’s datastore across devices.

In order to avoid record collisions between your app and TipKit, it is recommended that you use a separate container for syncing tips.

By default, TipKit’s datastore does not sync with CloudKit.

#### Discussion

Syncing TipKit’s datastore requires two separate capabilities in your app’s entitlements: the iCloud capability which lets you specify a CloudKit container, and the Background Modes capability, which lets your app receive remote notifications from CloudKit that contain information about new changes on the server.

![A screenshot of Xcode showing the entitlements for enabling TipKit's CloudKit syncing.](https://developer.apple.com/tutorials/images/com.apple.TipKit/xcode_cloudkit_entitlements@2x.png)

```swift
@main
struct TipKitTrails: App {
    init() {
        do {
            // Sync the TipKit datastore using CloudKit.
            try Tips.configure([
                .cloudKitContainer(.named("iCloud.com.apple.TipKitTrails.tips"))
            ])
        }
        catch {
            // Handle TipKit errors
            print("Error initializing TipKit \(error.localizedDescription)")
        }
    }
}
```

##### CloudKit Container Values

- [`automatic`](./cloudkitcontainer/automatic.md)
  Syncs the TipKit datastore using the first container in your app’s entitlements with a “.tips” suffix or, if none is available, the primary container is used.
- [`named(_:)`](./cloudkitcontainer/named%28_%29.md)
  Syncs the TipKit datastore using the specified CloudKit container.

## Parameters

- `cloudKitContainer`: The option to use for specifying TipKit’s CloudKit datastore. Use `nil` to disable CloudKit syncing.

## See Also

### Configuration
- [static func configure([Tips.ConfigurationOption]) throws](../configure%28_%29.md)
  Loads and configures the persistent state of all tips in your app.
- [static func datastoreLocation(Tips.ConfigurationOption.DatastoreLocation) -> Tips.ConfigurationOption](./datastorelocation%28_%29.md)
  Specify a custom location for your tips datastore.
- [static func displayFrequency(Tips.ConfigurationOption.DisplayFrequency) -> Tips.ConfigurationOption](./displayfrequency%28_%29.md)
  Customizes how often new tips are presented in your app after another tip has been displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption/cloudkitcontainer(_:))*