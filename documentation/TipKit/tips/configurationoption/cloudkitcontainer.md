# CloudKitContainer

**Framework**: TipKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

For more information on CloudKit syncing, see [`cloudKitContainer(_:)`](./cloudkitcontainer%28_%29.md).

## Topics

### Type Properties
- [static var automatic: Tips.ConfigurationOption.CloudKitContainer](./cloudkitcontainer/automatic.md)
  Syncs the TipKit datastore using the first container in your app’s entitlements with a “.tips” suffix or, if none is available, the primary container is used.
### Type Methods
- [static func named(String) -> Tips.ConfigurationOption.CloudKitContainer](./cloudkitcontainer/named%28_%29.md)
  Syncs the TipKit datastore using the specified CloudKit container.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/configurationoption/cloudkitcontainer)*