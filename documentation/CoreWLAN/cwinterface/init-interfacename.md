# init(interfaceName:)

**Framework**: Core WLAN  
**Kind**: init

Convenience method for getting an CWInterface object with the specified name.

**Availability**:
- macOS 10.6+

## Declaration

```swift
init(interfaceName name: String?)
```

#### Return Value

An CWInterface object configured to control the named CoreWLAN interface.

#### Discussion

The interface name must be in the BSD name form (e.g. “en1”), and can be passed in explicitly or derived from the call to . If  is , the method returns an CWInterface object for the primary interface.

## Parameters

- `name`: An NSString representing the BSD name of a WLAN interface.

## See Also

- [convenience init(name: String?)](cwinterface/init(name:).md)
  An instance method for obtaining an CWInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/init(interfacename:))*