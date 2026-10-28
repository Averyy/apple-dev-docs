# interface()

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Instance Method

Returns the default Wi-Fi interface.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func interface() -> CWInterface?
```

```objc
- (CWInterface *) interface;
```

## Return Value

The [`CWInterface`](../cwinterface.md) object that represents the default Wi-Fi interface.

## See Also

### Getting Interfaces
- [func interface(withName: String?) -> CWInterface?](./interface%28withname%29.md)
  Returns the Wi-Fi interface with the given name.
- [func interfaces() -> [CWInterface]?](./interfaces%28%29.md)
  Returns all available Wi-Fi interfaces.
- [class func interfaceNames() -> [String]?](./interfacenames%28%29-swift.type.method.md)
  Returns the list of the names of available Wi-Fi interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/interface())*