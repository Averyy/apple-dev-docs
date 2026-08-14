# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the receiver represents the same host as another `NSHost` object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func isEqual(to aHost: Host) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when the receiver and `host` share at least one network address; [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `aHost`: Host to compare the receiver to.

## See Also

- [var addresses: [String]](host/addresses.md)
  Returns all the network addresses of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/isequal(to:))*