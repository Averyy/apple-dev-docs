# init(name:)

**Framework**: Core WLAN  
**Kind**: init

An instance method for obtaining an CWInterface object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
convenience init(name: String?)
```

#### Return Value

An CWInterface object configured to control the named CoreWLAN interface.

#### Discussion

The interface name must be in the BSD name form (e.g. “en1”), and can be passed in explicitly or derived from the call to . If  is , the method returns an CWInterface object for the primary interface. This method is the designated initializer for the CWInterface class.

## Parameters

- `name`: An NSString representing the BSD name of a WLAN interface.

## See Also

- [init(interfaceName: String?)](cwinterface/init(interfacename:).md)
  Convenience method for getting an CWInterface object with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/init(name:))*