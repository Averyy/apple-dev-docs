# CloudKitContainer

**Framework**: TipKit  
**Kind**: struct

A type for specifying the CloudKit container used for syncing tips.

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
struct CloudKitContainer
```

#### Overview

For more information on CloudKit syncing, see [`cloudKitContainer(_:)`](tips/configurationoption/cloudkitcontainer(_:).md).

## Topics

### Type Properties
- [static var automatic: Tips.ConfigurationOption.CloudKitContainer](tips/configurationoption/cloudkitcontainer/automatic.md)
  Syncs the TipKit datastore using the first container in your app’s entitlements with a “.tips” suffix or, if none is available, the primary container is used.
### Type Methods
- [static func named(String) -> Tips.ConfigurationOption.CloudKitContainer](tips/configurationoption/cloudkitcontainer/named(_:).md)
  Syncs the TipKit datastore using the specified CloudKit container.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption/cloudkitcontainer)*