# networkPrefixLengths

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The IPv6 network prefix lengths to assign to the TUN interface.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var networkPrefixLengths: [NSNumber] { get }
```

```objc
@property (readonly) NSArray<NSNumber *> * networkPrefixLengths;
```

## Discussion

Each network prefix length in this array is combined with the IP address in the corresponding index in `addresses` to specify an IPv6 network that the TUN interface is (virtually) connected to.

## See Also

### Accessing IPv6 properties
- [var addresses: [String]](./addresses.md)
  The IPv6 addresses to assign to the TUN interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6settings/networkprefixlengths)*