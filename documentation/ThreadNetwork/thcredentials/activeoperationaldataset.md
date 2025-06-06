# activeOperationalDataSet

**Framework**: ThreadNetwork  
**Kind**: property

The essential operational parameters for the Thread network.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var activeOperationalDataSet: Data? { get }
```

#### Discussion

The framework parses this property, then extracts and sets [`channel`](thcredentials/channel.md), [`extendedPANID`](thcredentials/extendedpanid.md), [`networkKey`](thcredentials/networkkey.md), [`networkName`](thcredentials/networkname.md), [`panID`](thcredentials/panid.md), and [`pskc`](thcredentials/pskc.md) when you call [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md).

## See Also

- [var borderAgentID: Data?](thcredentials/borderagentid.md)
  The identifer of an active Thread network Border Agent.
- [var channel: UInt8](thcredentials/channel.md)
  The Thread network radio channel.
- [var extendedPANID: Data?](thcredentials/extendedpanid.md)
  The Thread network extended PAN identifier.
- [var networkKey: Data?](thcredentials/networkkey.md)
  The Thread network key.
- [var networkName: String?](thcredentials/networkname.md)
  The Thread network name.
- [var panID: Data?](thcredentials/panid.md)
  The Thead network PAN identifier.
- [var pskc: Data?](thcredentials/pskc.md)
  The Thread network pre-shared key for the Commissioner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thcredentials/activeoperationaldataset)*