# RegistrationError.Code.failed

**Framework**: ServicesAccountLinking  
**Kind**: case  
**Role**: Case

Registration failed.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case failed
```

```c
SALRegistrationErrorFailed
```

#### Discussion

This may indicate the user is not signed into an Apple Media & Purchases account or another system error occurred. Implement retry logic with appropriate user messaging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/code/failed)*