# interfaces()

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Returns all available Wi-Fi interfaces.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func interfaces() -> [CWInterface]?
```

```objc
- (NSArray<CWInterface *> *) interfaces;
```

## Return Value

An array of [`CWInterface`](../cwinterface.md) objects, representing all of the available Wi-Fi interfaces in the system.

## See Also

### Getting Interfaces
- [func interface() -> CWInterface?](./interface%28%29.md)
  Returns the default Wi-Fi interface.
- [func interface(withName: String?) -> CWInterface?](./interface%28withname%29.md)
  Returns the Wi-Fi interface with the given name.
- [class func interfaceNames() -> [String]?](./interfacenames%28%29-swift.type.method.md)
  Returns the list of the names of available Wi-Fi interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/interfaces())*