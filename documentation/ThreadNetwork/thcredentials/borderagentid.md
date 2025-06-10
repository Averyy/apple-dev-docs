# borderAgentID

**Framework**: ThreadNetwork  
**Kind**: property

The identifier of an active Thread network Border Agent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var borderAgentID: Data? { get }
```

#### Discussion

This property’s value is the MAC Extended Address, a random identifier that the active Thread network Thread Border Router generates.

## See Also

- [var activeOperationalDataSet: Data?](thcredentials/activeoperationaldataset.md)
  The essential operational parameters for the Thread network.
- [var channel: UInt8](thcredentials/channel.md)
  The Thread network radio channel.
- [var extendedPANID: Data?](thcredentials/extendedpanid.md)
  The Thread network extended PAN identifier.
- [var networkKey: Data?](thcredentials/networkkey.md)
  The Thread network key.
- [var networkName: String?](thcredentials/networkname.md)
  The Thread network name.
- [var panID: Data?](thcredentials/panid.md)
  The Thread network PAN identifier.
- [var pskc: Data?](thcredentials/pskc.md)
  The Thread network pre-shared key (PSKC) for the Commissioner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thcredentials/borderagentid)*