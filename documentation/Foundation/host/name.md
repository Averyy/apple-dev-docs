# name

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns one of the hostnames of the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use Network framework instead, see deprecation notice in <Foundation/NSHost.h>

## Declaration

```swift
var name: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * name;
```

#### Return Value

One of the hostnames of the receiver. Can be either a simple hostname, such as `"sales"`, or a fully qualified domain name, such as `"sales.anycorp.com"`.

## See Also

### Getting Host Information
- [var address: String?](./address.md)
  Returns one of the network addresses of the receiver.
- [var addresses: [String]](./addresses.md)
  Returns all the network addresses of the receiver.
- [var localizedName: String?](./localizedname.md)
  Returns the name used as by default when publishing `NSNetServices`.
- [var names: [String]](./names.md)
  Returns all the hostnames of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/name)*