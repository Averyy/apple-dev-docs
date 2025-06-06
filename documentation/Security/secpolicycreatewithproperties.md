# SecPolicyCreateWithProperties(_:_:)

**Framework**: Security  
**Kind**: func

Returns a policy object based on an object identifier for the policy type.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecPolicyCreateWithProperties(_ policyIdentifier: CFTypeRef, _ properties: CFDictionary?) -> SecPolicy?
```

## Mentions

- [Creating a Trust Object](creating-a-trust-object.md)

#### Return Value

A new policy, or `NULL` if the policy could not be created.

## Parameters

- `policyIdentifier`: The identifier for the desired policy type.
- `properties`: A properties dictionary. See   for a list of valid property names to use as keys in this dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicycreatewithproperties(_:_:))*