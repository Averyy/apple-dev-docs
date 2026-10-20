# CredentialSession.Credential.InstanceInfo.InstanceType.headApplication

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

A type that indicates an instance is the head application of a group.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case headApplication
```

#### Discussion

Use the [`instanceAID`](../instanceaid.md) of this object when calling [`performTransactionInWiredMode(using:instanceAID:)`](../../../../credentialtransaction/performtransactioninwiredmode%28using,instanceaid%29.md). Doing so delivers the authentication token to all of the [`CredentialSession.Credential.InstanceInfo.InstanceType.groupApplication`](./groupapplication.md) members through the broker interface on the Secure Element, as described in the [Apple Business Register](https://register.apple.com) Secure Element (ABR SE) documents.

## See Also

### Instance types
- [CredentialSession.Credential.InstanceInfo.InstanceType.standalone](./standalone.md)
  A type that indicates an instance doesn’t have any associative relationships with other instances.
- [CredentialSession.Credential.InstanceInfo.InstanceType.groupApplication](./groupapplication.md)
  A type that indicates an instance is a member of a group of application instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/instancetype-swift.enum/headapplication)*