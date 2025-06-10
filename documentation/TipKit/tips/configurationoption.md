# ConfigurationOption

**Framework**: TipKit  
**Kind**: struct

A type that marks an object as a tip configuration.

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
struct ConfigurationOption
```

## Topics

### Structures
- [struct CloudKitContainer](tips/configurationoption/cloudkitcontainer.md)
  A type for specifying the CloudKit container used for syncing tips.
- [struct DatastoreLocation](tips/configurationoption/datastorelocation.md)
  A type for specifying a custom location for your tips datastore.
- [struct DisplayFrequency](tips/configurationoption/displayfrequency.md)
  A type for specifying the minimum duration after one tip is shown before another tip will become eligible.
### Type Methods
- [static func cloudKitContainer(Tips.ConfigurationOption.CloudKitContainer?) -> Tips.ConfigurationOption](tips/configurationoption/cloudkitcontainer(_:).md)
  Sets the CloudKit container used for syncing tips.
- [static func datastoreLocation(Tips.ConfigurationOption.DatastoreLocation) -> Tips.ConfigurationOption](tips/configurationoption/datastorelocation(_:).md)
  Specify a custom location for your tips datastore.
- [static func displayFrequency(Tips.ConfigurationOption.DisplayFrequency) -> Tips.ConfigurationOption](tips/configurationoption/displayfrequency(_:).md)
  Customizes how often new tips are presented in your app after another tip has been displayed.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func configure([Tips.ConfigurationOption]) throws](tips/configure(_:).md)
  Loads and configures the persistent state of all tips in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption)*