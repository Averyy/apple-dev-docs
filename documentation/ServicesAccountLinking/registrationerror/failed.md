# failed

**Framework**: ServicesAccountLinking  
**Kind**: property

Registration failed.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static var failed: RegistrationError.Code { get }
```

#### Discussion

This may indicate the user is not signed into an Apple Media & Purchases account or another system error occurred. Implement retry logic with appropriate user messaging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/failed)*