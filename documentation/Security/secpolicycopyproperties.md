# SecPolicyCopyProperties(_:)

**Framework**: Security  
**Kind**: func

Returns a dictionary containing a policy’s properties.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecPolicyCopyProperties(_ policyRef: SecPolicy) -> CFDictionary?
```

#### Return Value

A dictionary with the policy’s properties. See [`Security Policy Keys`](security-policy-keys.md) for a list of valid keys. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the dictionary’s memory when you are done with it.

## Parameters

- `policyRef`: The policy from which properties should be copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicycopyproperties(_:))*