# init(address:)

**Framework**: Foundation  
**Kind**: init

Returns the `NSHost` with the Internet address `address`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
convenience init(address: String)
```

#### Return Value

The host for `address`.

## Parameters

- `address`: Network address to look up. For example,   or  .

## See Also

- [class func current() -> Self](host/current.md)
  Returns an `NSHost` object representing the host the process is running on.
- [convenience init(name: String?)](host/init(name:).md)
  Returns a host with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/init(address:))*