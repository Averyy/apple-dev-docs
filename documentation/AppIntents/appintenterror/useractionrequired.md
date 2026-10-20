# AppIntentError.UserActionRequired

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Errors that represent a state where a person needs to respond to successfully complete the action.

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
enum UserActionRequired
```

#### Overview

Use these system-defined errors to inform people about steps they can take to fix the error.

## Topics

### Type Properties
- [static let accountSetup: AppIntentError](./useractionrequired/accountsetup.md)
  The person needs to set up their account.
- [static let confirmation: AppIntentError](./useractionrequired/confirmation.md)
  The person needs to confirm the action.
- [static let signin: AppIntentError](./useractionrequired/signin.md)
  The person needs to sign in to continue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/useractionrequired)*