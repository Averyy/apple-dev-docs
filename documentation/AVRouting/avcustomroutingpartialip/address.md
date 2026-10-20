# address

**Framework**: AVRouting  
**Kind**: property  
**Role**: Instance Property

A full or partial IP address for a device known to be on the network.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- visionOS 1.0+

## Declaration

```swift
var address: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * address;
```

## See Also

### Inspecting the IP fragment
- [var mask: Data](./mask.md)
  A mask that represents how many octets of the IP address to respect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingpartialip/address)*