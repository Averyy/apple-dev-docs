# mask

**Framework**: AVRouting  
**Kind**: property  
**Role**: Instance Property

A mask that represents how many octets of the IP address to respect.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- visionOS 1.0+

## Declaration

```swift
var mask: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * mask;
```

## See Also

### Inspecting the IP fragment
- [var address: Data](./address.md)
  A full or partial IP address for a device known to be on the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingpartialip/mask)*