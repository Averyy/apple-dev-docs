# SecPolicyCreateSSL(_:_:)

**Framework**: Security  
**Kind**: func

Returns a policy object for evaluating SSL certificate chains.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecPolicyCreateSSL(_ server: Bool, _ hostname: CFString?) -> SecPolicy
```

## Mentions

- [Creating a Trust Object](creating-a-trust-object.md)

#### Return Value

The policy object. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to release the object when you are finished with it.

## Parameters

- `server`: Specify   on the client side to return a policy for SSL server certificates.
- `hostname`: If you specify a value for this parameter, the policy will require the specified value to match the host name in the leaf certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicycreatessl(_:_:))*