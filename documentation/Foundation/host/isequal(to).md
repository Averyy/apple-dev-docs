# isEqual(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the receiver represents the same host as another `NSHost` object.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use Network framework instead, see deprecation notice in <Foundation/NSHost.h>

## Declaration

```swift
func isEqual(to aHost: Host) -> Bool
```

```objc
- (BOOL) isEqualToHost:(NSHost *) aHost;
```

## Return Value

[`true`](../../Swift/true.md) when the receiver and `host` share at least one network address; [`false`](../../Swift/false.md) otherwise.

## Parameters

- `aHost`: Host to compare the receiver to.

## See Also

### Related Documentation
- [var addresses: [String]](./addresses.md)
  Returns all the network addresses of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/isequal(to:))*