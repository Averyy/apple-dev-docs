# interfaceNames()

**Framework**: Core WLAN  
**Kind**: method  
**Role**: Type Method

Returns the list of the names of available Wi-Fi interfaces.

**Availability**:
- macOS 10.10+ - Deprecated in 13.0

> **Deprecated**: Use -[CWWiFiClient interfaceNames] instead

## Declaration

```swift
class func interfaceNames() -> [String]?
```

```objc
+ (NSArray<NSString *> *) interfaceNames;
```

## Return Value

An array of strings representing the names of the available Wi-Fi interfaces in the system. Any one of these names can be used with the [`interface(withName:)`](./interface%28withname%29.md) method to obtain a reference to the corresponding [`CWInterface`](../cwinterface.md) instance.

## See Also

### Getting Interfaces
- [func interface() -> CWInterface?](./interface%28%29.md)
  Returns the default Wi-Fi interface.
- [func interface(withName: String?) -> CWInterface?](./interface%28withname%29.md)
  Returns the Wi-Fi interface with the given name.
- [func interfaces() -> [CWInterface]?](./interfaces%28%29.md)
  Returns all available Wi-Fi interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/interfacenames()-swift.type.method)*