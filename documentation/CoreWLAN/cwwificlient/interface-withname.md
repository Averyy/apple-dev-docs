# interface(withName:)

**Framework**: Core WLAN  
**Kind**: method

Returns the Wi-Fi interface with the given name.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func interface(withName interfaceName: String?) -> CWInterface?
```

#### Return Value

The [`CWInterface`](cwinterface.md) object bound to the given interface name, or the default interface if no name is specified.

## Parameters

- `interfaceName`: The name of an available Wi-Fi interface. Use the   class method to obtain a list of valid interface names.

## See Also

- [func interface() -> CWInterface?](cwwificlient/interface.md)
  Returns the default Wi-Fi interface.
- [func interfaces() -> [CWInterface]?](cwwificlient/interfaces.md)
  Returns all available Wi-Fi interfaces.
- [class func interfaceNames() -> [String]?](cwwificlient/interfacenames-swift.type.method.md)
  Returns the list of the names of available Wi-Fi interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwwificlient/interface(withname:))*