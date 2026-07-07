# ManagedApplicationConfigurationResponse.ApplicationConfigurationsItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains a managed app’s configurations item.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.15+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ManagedApplicationConfigurationResponse.ApplicationConfigurationsItem
```

## Topics

### Objects
- [object ManagedApplicationConfigurationResponse.ApplicationConfigurationsItem.Configuration](managedapplicationconfigurationresponse/applicationconfigurationsitem/configuration-data.dictionary.md)
  A dictionary that contains a managed app’s configuration items.

## Properties

- `Configuration` (ManagedApplicationConfigurationResponse.ApplicationConfigurationsItem.Configuration): The app’s configurations.
- `Identifier` (string) *(required)*: The app’s bundle identifier. > **Note**:  For a watchOS app, the identifier is the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone the watch pairs with.

## See Also

- [object ManagedApplicationConfigurationResponse.ErrorChainItem](managedapplicationconfigurationresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managedapplicationconfigurationresponse/applicationconfigurationsitem)*