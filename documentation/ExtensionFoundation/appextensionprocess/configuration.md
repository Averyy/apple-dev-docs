# AppExtensionProcess.Configuration

**Framework**: ExtensionFoundation  
**Kind**: struct

A structure that holds the identity of an app extension and process-related details.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
struct Configuration
```

#### Overview

This type manages the configuration details you use to create an [`AppExtensionProcess`](appextensionprocess.md) structure. Create an instance of this type and initialize it with the identity of the app extension you want and a closure to run if the app extension terminates unexpectedly.

## Topics

### Creating the configuration structure
- [init(appExtensionIdentity: AppExtensionIdentity, onInterruption: () -> Void)](appextensionprocess/configuration/init(appextensionidentity:oninterruption:).md)
### Responding to process interruptions
- [var onInterruption: () -> Void](appextensionprocess/configuration/oninterruption.md)
  The closure to run if the app extension’s process exits unexpectedly.
### Getting the app-extension details
- [var appExtensionIdentity: AppExtensionIdentity](appextensionprocess/configuration/appextensionidentity.md)
  The identifying information for the app extension you want to launch.

## See Also

- [init(configuration: AppExtensionProcess.Configuration) throws](appextensionprocess/init(configuration:)-2g0cy.md)
  Finds an existing process for the specified app extension or creates a new one synchronously.
- [init(configuration: AppExtensionProcess.Configuration) async throws](appextensionprocess/init(configuration:)-38zf.md)
  Finds an existing process for the specified app extension or creates a new one asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/configuration)*