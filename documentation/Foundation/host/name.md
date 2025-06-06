# name

**Framework**: Foundation  
**Kind**: property

Returns one of the hostnames of the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var name: String? { get }
```

#### Return Value

One of the hostnames of the receiver. Can be either a simple hostname, such as `"sales"`, or a fully qualified domain name, such as `"sales.anycorp.com"`.

## See Also

- [var address: String?](host/address.md)
  Returns one of the network addresses of the receiver.
- [var addresses: [String]](host/addresses.md)
  Returns all the network addresses of the receiver.
- [var localizedName: String?](host/localizedname.md)
  Returns the name used as by default when publishing `NSNetServices`.
- [var names: [String]](host/names.md)
  Returns all the hostnames of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/name)*