# AppIntentError.Unrecoverable

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Unknown or unrecoverable errors that might have occurred due to either a system or user error.

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
enum Unrecoverable
```

## Overview

Use these system-defined errors to inform people that there’s no immediate way to remedy an error.

## Topics

### Type Properties
- [static let entityNotFound: AppIntentError](./unrecoverable/entitynotfound.md)
  No app entity matched the search criteria.
- [static let featureCurrentlyRestricted: AppIntentError](./unrecoverable/featurecurrentlyrestricted.md)
  This feature is currently restricted due to Screen Time restrictions, MDM profiles, or similar.
- [static let networkFailure: AppIntentError](./unrecoverable/networkfailure.md)
  The person needs to be connected to the internet.
- [static let notAllowed: AppIntentError](./unrecoverable/notallowed.md)
  This action isn’t allowed.
- [static let partialFailure: AppIntentError](./unrecoverable/partialfailure.md)
  Not every action was completed.
- [static let unknown: AppIntentError](./unrecoverable/unknown.md)
  Something went wrong.
- [static let unsupportedOnDevice: AppIntentError](./unrecoverable/unsupportedondevice.md)
  This feature isn’t supported on this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/unrecoverable)*