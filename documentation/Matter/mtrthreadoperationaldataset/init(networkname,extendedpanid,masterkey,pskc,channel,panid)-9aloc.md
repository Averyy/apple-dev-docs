# init(networkName:extendedPANID:masterKey:psKc:channel:panID:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use initWithNetworkName:extendedPANID:masterKey:PSKc:channelNumber:panID

## Declaration

```swift
init?(networkName: String, extendedPANID: Data, masterKey: Data, psKc PSKc: Data, channel: UInt16, panID: Data)
```

```objc
- (instancetype) initWithNetworkName:(NSString *) networkName extendedPANID:(NSData *) extendedPANID masterKey:(NSData *) masterKey PSKc:(NSData *) PSKc channel:(uint16_t) channel panID:(NSData *) panID;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrthreadoperationaldataset/init(networkname:extendedpanid:masterkey:pskc:channel:panid:)-9aloc)*