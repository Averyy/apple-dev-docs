# init(name:)

**Framework**: Core WLAN  
**Kind**: init  
**Role**: Initializer

An instance method for obtaining an CWInterface object.

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: This method relies on direct access to system sockets, and therefore cannot be used in a sandboxed app. Use the [`interface(withName:)`](../cwwificlient/interface%28withname%29.md) instance method of [`CWWiFiClient`](../cwwificlient.md) instead.

## Declaration

```swift
convenience init(name: String?)
```

```objc
+ (instancetype) interfaceWithName:(NSString *) name;
```

#### Return Value

An CWInterface object configured to control the named CoreWLAN interface.

#### Discussion

The interface name must be in the BSD name form (e.g. “en1”), and can be passed in explicitly or derived from the call to *+(NSString *)supportedInterfaces*. If *name* is *nil*, the method returns an CWInterface object for the primary interface. This method is the designated initializer for the CWInterface class.

## Parameters

- `name`: An NSString representing the BSD name of a WLAN interface.

## See Also

### Getting an interface
- [init(interfaceName: String?)](./init%28interfacename%29.md)
  Convenience method for getting an CWInterface object with the specified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/init(name:))*