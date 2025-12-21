# SecPolicyCreateBasicX509()

**Framework**: Security  
**Kind**: func

Returns a policy object for the default X.509 policy.

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
func SecPolicyCreateBasicX509() -> SecPolicy
```

## Mentions

- [Creating a Trust Object](creating-a-trust-object.md)

#### Return Value

The policy object. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to release the object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicycreatebasicx509())*