# address

**Framework**: Foundation  
**Kind**: property

Returns one of the network addresses of the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var address: String? { get }
```

#### Return Value

One of the network address for the receiver. For example, `"192.42.172.1"` or `"fe80::1"`.

## See Also

- [var addresses: [String]](host/addresses.md)
  Returns all the network addresses of the receiver.
- [var name: String?](host/name.md)
  Returns one of the hostnames of the receiver.
- [var localizedName: String?](host/localizedname.md)
  Returns the name used as by default when publishing `NSNetServices`.
- [var names: [String]](host/names.md)
  Returns all the hostnames of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/address)*