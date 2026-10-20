# activeOperationalDataSet

**Framework**: ThreadNetwork  
**Kind**: property  
**Role**: Instance Property

The essential operational parameters for the Thread network.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var activeOperationalDataSet: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * activeOperationalDataSet;
```

#### Discussion

The framework parses this property, then extracts and sets [`channel`](./channel.md), [`extendedPANID`](./extendedpanid.md), [`networkKey`](./networkkey.md), [`networkName`](./networkname.md), [`panID`](./panid.md), and [`pskc`](./pskc.md) when you call [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](../thclient/storecredentials%28forborderagent,activeoperationaldataset,completion%29.md).

## See Also

### Getting the Thread Parameters
- [var borderAgentID: Data?](./borderagentid.md)
  The identifier of an active Thread network Border Agent.
- [var channel: UInt8](./channel.md)
  The Thread network radio channel.
- [var extendedPANID: Data?](./extendedpanid.md)
  The Thread network extended PAN identifier.
- [var networkKey: Data?](./networkkey.md)
  The Thread network key.
- [var networkName: String?](./networkname.md)
  The Thread network name.
- [var panID: Data?](./panid.md)
  The Thread network PAN identifier.
- [var pskc: Data?](./pskc.md)
  The Thread network pre-shared key (PSKC) for the Commissioner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thcredentials/activeoperationaldataset)*