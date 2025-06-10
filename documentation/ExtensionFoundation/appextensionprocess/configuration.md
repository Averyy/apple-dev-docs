# AppExtensionProcess.Configuration

**Framework**: ExtensionFoundation  
**Kind**: struct

An object that holds configuration options for an app extension process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Handling Process Interruptions
- [var onInterruption: () -> Void](appextensionprocess/configuration/oninterruption.md)
  A closure the system calles when an extension process exits.
### Initializers
- [init(appExtensionIdentity: AppExtensionIdentity, onInterruption: () -> Void)](appextensionprocess/configuration/init(appextensionidentity:oninterruption:).md)
### Instance Properties
- [var appExtensionIdentity: AppExtensionIdentity](appextensionprocess/configuration/appextensionidentity.md)

## See Also

- [init(configuration: AppExtensionProcess.Configuration) throws](appextensionprocess/init(configuration:)-2g0cy.md)
  Synchronously finds an existing extension process or launches a new one.
- [init(configuration: AppExtensionProcess.Configuration) async throws](appextensionprocess/init(configuration:)-38zf.md)
  Asynchronously finds an existing extension process or launches a one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/configuration)*