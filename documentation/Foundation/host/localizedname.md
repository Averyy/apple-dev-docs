# localizedName

**Framework**: Foundation  
**Kind**: property

Returns the name used as by default when publishing `NSNetServices`.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var localizedName: String? { get }
```

#### Return Value

A string containing the computer name.

#### Discussion

This is the name displayed in the Finder sidebar, as well as in the Sharing preference panel.

This method only returns an `NSString` when sent to the [`current()`](host/current().md) instance, all other instances currently return `nil`.

This property is key-value observable.

## See Also

- [var address: String?](host/address.md)
  Returns one of the network addresses of the receiver.
- [var addresses: [String]](host/addresses.md)
  Returns all the network addresses of the receiver.
- [var name: String?](host/name.md)
  Returns one of the hostnames of the receiver.
- [var names: [String]](host/names.md)
  Returns all the hostnames of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/localizedname)*