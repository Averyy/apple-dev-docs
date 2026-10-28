# address

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns one of the network addresses of the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use Network framework instead, see deprecation notice in <Foundation/NSHost.h>

## Declaration

```swift
var address: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * address;
```

## Return Value

One of the network address for the receiver. For example, `"192.42.172.1"` or `"fe80::1"`.

## See Also

### Getting Host Information
- [var addresses: [String]](./addresses.md)
  Returns all the network addresses of the receiver.
- [var name: String?](./name.md)
  Returns one of the hostnames of the receiver.
- [var localizedName: String?](./localizedname.md)
  Returns the name used as by default when publishing `NSNetServices`.
- [var names: [String]](./names.md)
  Returns all the hostnames of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/address)*