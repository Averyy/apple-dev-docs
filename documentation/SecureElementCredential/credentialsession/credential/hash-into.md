# hash(into:)

**Framework**: SecureElementCredential  
**Kind**: method

Hashes the essential components of the value by feeding them into the given hasher.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the  [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) protocol. The components you use for hashing must be the same as the components you compare in your type’s `==` operator implementation. Call [`combine(_:)`](https://developer.apple.com/documentation/Swift/Hasher/combine(_:)) with each of these components.

> ❗ **Important**:  Don’t call `finalize()` on `hasher`. It may become a compile-time error.

 Don’t call `finalize()` on `hasher`. It may become a compile-time error.

See [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) for more information about the concepts and uses of hashing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/hash(into:))*