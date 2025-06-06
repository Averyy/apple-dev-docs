# init(name:)

**Framework**: Foundation  
**Kind**: init

Returns a host with a specific name.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init(name: String?)
```

#### Return Value

The host named `hostname`.

## Parameters

- `name`: Name of the host to look up. Can be either a simple hostname, such as  , or a fully qualified domain name, such as  .

## See Also

- [class func current() -> Self](host/current.md)
  Returns an `NSHost` object representing the host the process is running on.
- [convenience init(address: String)](host/init(address:).md)
  Returns the `NSHost` with the Internet address `address`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/init(name:))*