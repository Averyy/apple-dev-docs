# CredentialSession.Credential.InstanceInfo.InstanceType.standalone

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

A type that indicates an instance doesn’t have any associative relationships with other instances.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case standalone
```

## Discussion

Use the [`instanceAID`](../instanceaid.md) of this credential instance with [`performTransactionInWiredMode(using:instanceAID:)`](../../../../credentialtransaction/performtransactioninwiredmode%28using,instanceaid%29.md).

## See Also

### Instance types
- [CredentialSession.Credential.InstanceInfo.InstanceType.headApplication](./headapplication.md)
  A type that indicates an instance is the head application of a group.
- [CredentialSession.Credential.InstanceInfo.InstanceType.groupApplication](./groupapplication.md)
  A type that indicates an instance is a member of a group of application instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/instancetype-swift.enum/standalone)*