# interface()

**Framework**: Core WLAN  
**Kind**: method

Returns the default Wi-Fi interface.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func interface() -> CWInterface?
```

#### Return Value

The [`CWInterface`](cwinterface.md) object that represents the default Wi-Fi interface.

## See Also

- [func interface(withName: String?) -> CWInterface?](cwwificlient/interface(withname:).md)
  Returns the Wi-Fi interface with the given name.
- [func interfaces() -> [CWInterface]?](cwwificlient/interfaces.md)
  Returns all available Wi-Fi interfaces.
- [class func interfaceNames() -> [String]?](cwwificlient/interfacenames-swift.type.method.md)
  Returns the list of the names of available Wi-Fi interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/interface())*