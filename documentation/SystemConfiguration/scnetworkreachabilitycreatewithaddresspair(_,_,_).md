# SCNetworkReachabilityCreateWithAddressPair(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Creates a reachability reference to the specified network address.

**Availability**:
- iOS 2.0+ - Deprecated in 17.4
- iPadOS 2.0+ - Deprecated in 17.4
- Mac Catalyst 13.1+ - Deprecated in 17.4
- macOS 10.3+ - Deprecated in 14.4
- tvOS - Deprecated in 17.4
- visionOS 1.0+ - Deprecated in 1.1

## Declaration

```swift
func SCNetworkReachabilityCreateWithAddressPair(_ allocator: CFAllocator?, _ localAddress: UnsafePointer<sockaddr>?, _ remoteAddress: UnsafePointer<sockaddr>?) -> SCNetworkReachability?
```

```c
SCNetworkReachabilityRefSCNetworkReachabilityCreateWithAddressPair(CFAllocatorRef allocator, const struct sockaddr *localAddress, const struct sockaddr *remoteAddress);
```

#### Return Value

A new immutable reachability reference. You must release the returned value.

#### Discussion

You can use the reachability reference returned by this function to monitor the reachability of the target host.

## Parameters

- `allocator`: The allocator to use. Pass `NULL` or [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) to use the default allocator.
- `localAddress`: The local address associated with a network connection. If `NULL`, only the remote address is of interest. The value of this parameter is copied into the new object.
- `remoteAddress`: The remote address associated with a network connection. If `NULL`, only the local address is of interest. The value of this parameter is copied into the new object.

## See Also

### Creating a Reachability Reference
- [func SCNetworkReachabilityCreateWithAddress(CFAllocator?, UnsafePointer<sockaddr>) -> SCNetworkReachability?](./scnetworkreachabilitycreatewithaddress%28_,_%29.md)
  Creates a reachability reference to the specified network address.
- [func SCNetworkReachabilityCreateWithName(CFAllocator?, UnsafePointer<CChar>) -> SCNetworkReachability?](./scnetworkreachabilitycreatewithname%28_,_%29.md)
  Creates a reachability reference to the specified network host or node name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilitycreatewithaddresspair(_:_:_:))*