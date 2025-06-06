# configurationData

**Framework**: CryptoTokenKit  
**Kind**: property

Additional configuration information for the token instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var configurationData: Data? { get set }
```

#### Discussion

[`configurationData`](tktoken/configuration-swift.class/configurationdata.md) can provide token-implementation-specific additional data, which the app that hosts the token driver extension and configures the token provides. The system doesn’t interpret this data in any way.

For example, the network-based hardware security module (HSM) can store encoded target network addresses, access credentials, or the list of identities the HSM contains.

## See Also

- [var instanceID: TKToken.InstanceID](tktoken/configuration-swift.class/instanceid.md)
  The unique, persistent identifier of this token that the token implementation creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.class/configurationdata)*