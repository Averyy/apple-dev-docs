# RegistrationError.Code.rateLimited

**Framework**: ServicesAccountLinking  
**Kind**: case

The server rate-limited the request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case rateLimited
```

#### Discussion

Check the error’s `userInfo` for [`RegistrationErrorRetryAfterKey`](registrationerrorretryafterkey.md) to get the server-provided retry interval. If absent, use exponential backoff.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/registrationerror/code/ratelimited)*