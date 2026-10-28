# init(name:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a host with a specific name.

**Availability**:
- macOS 10.0+ - Deprecated in 27.2

> **Deprecated**: Use Network framework instead, see deprecation notice in <Foundation/NSHost.h>

## Declaration

```swift
convenience init(name: String?)
```

```objc
+ (instancetype) hostWithName:(NSString *) name;
```

## Return Value

The host named `hostname`.

## Parameters

- `name`: Name of the host to look up. Can be either a simple hostname, such as `"sales"`, or a fully qualified domain name, such as `"sales.anycorp.com"`.

## See Also

### Creating Hosts
- [class func current() -> Self](./current%28%29.md)
  Returns an `NSHost` object representing the host the process is running on.
- [convenience init(address: String)](./init%28address%29.md)
  Returns the `NSHost` with the Internet address `address`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/host/init(name:))*