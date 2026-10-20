# deviceController(_:getNodesWithStoredDataWithReply:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
optional func deviceController(_ controller: UUID, getNodesWithStoredDataWithReply reply: @escaping @Sendable ([NSNumber]) -> Void)
```

```swift
optional func deviceControllerGetNodesWithStoredData(_ controller: UUID) async -> [NSNumber]
```

```objc
- (void) deviceController:(NSUUID *) controller getNodesWithStoredDataWithReply:(void (^)(NSArray<NSNumber *> *)) reply;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcserverprotocol_mtrdevicecontroller/devicecontroller(_:getnodeswithstoreddatawithreply:))*