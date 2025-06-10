# AppIntentError.Unrecoverable

**Framework**: App Intents  
**Kind**: enum

Unknown or unrecoverable error that might have occurred due to either a system or user error.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum Unrecoverable
```

#### Overview

Use these system-defined errors to inform a person that there is no immediate way to remedy an error.

## Topics

### Type Properties
- [static let entityNotFound: AppIntentError](appintenterror/unrecoverable/entitynotfound.md)
  You are looking to fetch an entity that does not exist
- [static let featureCurrentlyRestricted: AppIntentError](appintenterror/unrecoverable/featurecurrentlyrestricted.md)
  This feature is currently restricted (due to screen time restrictions, MDM profiles etc.)
- [static let networkFailure: AppIntentError](appintenterror/unrecoverable/networkfailure.md)
  User needs to be connected to internet
- [static let notAllowed: AppIntentError](appintenterror/unrecoverable/notallowed.md)
  This current action is not allowed
- [static let partialFailure: AppIntentError](appintenterror/unrecoverable/partialfailure.md)
  Not every action was completed
- [static let unknown: AppIntentError](appintenterror/unrecoverable/unknown.md)
  Something went wrong
- [static let unsupportedOnDevice: AppIntentError](appintenterror/unrecoverable/unsupportedondevice.md)
  This feature is not supported on this device


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/unrecoverable)*