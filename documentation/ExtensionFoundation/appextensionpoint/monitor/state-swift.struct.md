# AppExtensionPoint.Monitor.State

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

A type that contains a snapshot of a monitor’s state information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
struct State
```

## Overview

Use this type to get more detailed information about the state of the app extensions available to the host app. This type contains [`AppExtensionIdentity`](../../appextensionidentity.md) types for all currently available app extensions. It also contains information about how many disabled extensions are present on the system.

## Topics

### Getting the app extension status
- [var identities: [AppExtensionIdentity]](./state-swift.struct/identities.md)
  The set of approved and enabled app extensions.
- [var disabledCount: Int](./state-swift.struct/disabledcount.md)
  The number of app extensions that someone disabled.
- [var unapprovedCount: Int](./state-swift.struct/unapprovedcount.md)
  The number of identity entries that someone hasn’t yet enabled.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the monitor state
- [var state: AppExtensionPoint.Monitor.State](./state-swift.property.md)
  The current details about the available, disabled, and unapproved extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/state-swift.struct)*