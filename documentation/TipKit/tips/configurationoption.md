# ConfigurationOption

**Framework**: TipKit  
**Kind**: struct  
**Role**: Structure

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
- [struct CloudKitContainer](./configurationoption/cloudkitcontainer.md)
  A type for specifying the CloudKit container used for syncing tips.
- [struct DatastoreLocation](./configurationoption/datastorelocation.md)
  A type for specifying a custom location for your tips datastore.
- [struct DisplayFrequency](./configurationoption/displayfrequency.md)
  A type for specifying the minimum duration after one tip is shown before another tip will become eligible.
### Type Methods
- [static func cloudKitContainer(Tips.ConfigurationOption.CloudKitContainer?) -> Tips.ConfigurationOption](./configurationoption/cloudkitcontainer%28_%29.md)
  Sets the CloudKit container used for syncing tips.
- [static func datastoreLocation(Tips.ConfigurationOption.DatastoreLocation) -> Tips.ConfigurationOption](./configurationoption/datastorelocation%28_%29.md)
  Specify a custom location for your tips datastore.
- [static func displayFrequency(Tips.ConfigurationOption.DisplayFrequency) -> Tips.ConfigurationOption](./configurationoption/displayfrequency%28_%29.md)
  Customizes how often new tips are presented in your app after another tip has been displayed.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuration
- [static func configure([Tips.ConfigurationOption]) throws](./configure%28_%29.md)
  Loads and configures the persistent state of all tips in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption)*