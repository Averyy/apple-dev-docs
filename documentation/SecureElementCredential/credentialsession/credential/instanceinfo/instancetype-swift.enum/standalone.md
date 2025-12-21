# CredentialSession.Credential.InstanceInfo.InstanceType.standalone

**Framework**: SecureElementCredential  
**Kind**: case

A type that indicates an instance doesn’t have any associative relationships with other instances.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case standalone
```

#### Discussion

Use the [`instanceAID`](credentialsession/credential/instanceinfo/instanceaid.md) of this credential instance with [`performTransactionInWiredMode(using:instanceAID:)`](credentialtransaction/performtransactioninwiredmode(using:instanceaid:).md).

## See Also

- [CredentialSession.Credential.InstanceInfo.InstanceType.headApplication](credentialsession/credential/instanceinfo/instancetype-swift.enum/headapplication.md)
  A type that indicates an instance is the head application of a group.
- [CredentialSession.Credential.InstanceInfo.InstanceType.groupApplication](credentialsession/credential/instanceinfo/instancetype-swift.enum/groupapplication.md)
  A type that indicates an instance is a member of a group of application instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/instancetype-swift.enum/standalone)*