# requestAuthorization(completionHandler:)

**Framework**: Family Controls  
**Kind**: method  
**Role**: Instance Method

Requests authorization to provide parental controls for a child.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0

> **Deprecated**: Use [`requestAuthorization(for:)`](./requestauthorization%28for%29.md) instead.

## Declaration

```swift
func requestAuthorization(completionHandler: @escaping (Result<Void, any Error>) -> Void)
```

## Parameters

- `completionHandler`: A closure the system calls after it completes the authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationcenter/requestauthorization(completionhandler:))*