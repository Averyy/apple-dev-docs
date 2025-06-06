# SCNetworkReachabilityCreateWithAddress(_:_:)

**Framework**: System Configuration  
**Kind**: func

Creates a reachability reference to the specified network address.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func SCNetworkReachabilityCreateWithAddress(_ allocator: CFAllocator?, _ address: UnsafePointer<sockaddr>) -> SCNetworkReachability?
```

#### Return Value

A new immutable reachability reference. You must release the returned value.

#### Discussion

You can use the reachability reference returned by this function to monitor the reachability of the target host.

## Parameters

- `allocator`: The allocator to use. Pass   or   to use the default allocator.
- `address`: The address of the desired host. The value of this parameter is copied into the new object.

## See Also

- [func SCNetworkReachabilityCreateWithAddressPair(CFAllocator?, UnsafePointer<sockaddr>?, UnsafePointer<sockaddr>?) -> SCNetworkReachability?](scnetworkreachabilitycreatewithaddresspair(_:_:_:).md)
  Creates a reachability reference to the specified network address.
- [func SCNetworkReachabilityCreateWithName(CFAllocator?, UnsafePointer<CChar>) -> SCNetworkReachability?](scnetworkreachabilitycreatewithname(_:_:).md)
  Creates a reachability reference to the specified network host or node name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycreatewithaddress(_:_:))*