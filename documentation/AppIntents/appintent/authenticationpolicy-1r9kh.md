# authenticationPolicy

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property

The authentication policy to enforce when running the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
static var authenticationPolicy: IntentAuthenticationPolicy { get }
```

## Discussion

Set the value of this property if you want someone to provide authentication before running the app intent. The default value of this property is [`IntentAuthenticationPolicy.alwaysAllowed`](../intentauthenticationpolicy/alwaysallowed.md), which allows the intent to run without authentication, including when the device is locked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/authenticationpolicy-1r9kh)*