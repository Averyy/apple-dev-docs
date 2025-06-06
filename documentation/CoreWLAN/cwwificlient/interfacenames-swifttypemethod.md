# interfaceNames()

**Framework**: Core WLAN  
**Kind**: method

Returns the list of the names of available Wi-Fi interfaces.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func interfaceNames() -> [String]?
```

#### Return Value

An array of strings representing the names of the available Wi-Fi interfaces in the system. Any one of these names can be used with the [`interface(withName:)`](cwwificlient/interface(withname:).md) method to obtain a reference to the corresponding [`CWInterface`](cwinterface.md) instance.

## See Also

- [func interface() -> CWInterface?](cwwificlient/interface.md)
  Returns the default Wi-Fi interface.
- [func interface(withName: String?) -> CWInterface?](cwwificlient/interface(withname:).md)
  Returns the Wi-Fi interface with the given name.
- [func interfaces() -> [CWInterface]?](cwwificlient/interfaces.md)
  Returns all available Wi-Fi interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/interfacenames()-swift.type.method)*