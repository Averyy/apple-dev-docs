# interfaces()

**Framework**: Core WLAN  
**Kind**: method

Returns all available Wi-Fi interfaces.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func interfaces() -> [CWInterface]?
```

#### Return Value

An array of [`CWInterface`](cwinterface.md) objects, representing all of the available Wi-Fi interfaces in the system.

## See Also

- [func interface() -> CWInterface?](cwwificlient/interface.md)
  Returns the default Wi-Fi interface.
- [func interface(withName: String?) -> CWInterface?](cwwificlient/interface(withname:).md)
  Returns the Wi-Fi interface with the given name.
- [class func interfaceNames() -> [String]?](cwwificlient/interfacenames-swift.type.method.md)
  Returns the list of the names of available Wi-Fi interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/interfaces())*