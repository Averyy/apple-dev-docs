# init(signing:fabricId:ipk:)

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

> **Deprecated**: Please use initWithIPK:fabricID:nocSigner:

## Declaration

```swift
init(signing nocSigner: any MTRKeypair, fabricId: UInt64, ipk: Data)
```

```objc
- (instancetype) initWithSigningKeypair:(id<MTRKeypair>) nocSigner fabricId:(uint64_t) fabricId ipk:(NSData *) ipk;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontrollerstartupparams/init(signing:fabricid:ipk:))*