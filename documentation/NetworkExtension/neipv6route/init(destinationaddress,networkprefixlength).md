# init(destinationAddress:networkPrefixLength:)

**Framework**: Network Extension  
**Kind**: init  
**Role**: Initializer

Initialize the NEIPv6Route

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(destinationAddress address: String, networkPrefixLength: NSNumber)
```

```objc
- (instancetype) initWithDestinationAddress:(NSString *) address networkPrefixLength:(NSNumber *) networkPrefixLength;
```

## Return Value

The initialized `NEIPv6Route` object.

## Parameters

- `address`: An IPv6 address string. This string is combined with `networkPrefixLength` to specify the destination network of the route.
- `networkPrefixLength`: An IPv6 network prefix length. This number is combined with `address` to specify the destination network of the route. The network prefix length must be an integer between 0 and 128.

## See Also

### Creating an IPv6 Route
- [class func `default`() -> NEIPv6Route](./default%28%29.md)
  A convenience method for creating the default IPv4 route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6route/init(destinationaddress:networkprefixlength:))*