# init(address:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns the `NSHost` with the Internet address `address`.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use Network framework instead, see deprecation notice in <Foundation/NSHost.h>

## Declaration

```swift
convenience init(address: String)
```

```objc
+ (instancetype) hostWithAddress:(NSString *) address;
```

## Return Value

The host for `address`.

## Parameters

- `address`: Network address to look up. For example, `"127.0.0.1"` or `"fe80::1"`.

## See Also

### Creating Hosts
- [class func current() -> Self](./current%28%29.md)
  Returns an `NSHost` object representing the host the process is running on.
- [convenience init(name: String?)](./init%28name%29.md)
  Returns a host with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/init(address:))*