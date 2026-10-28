# temporary

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

A temporary disconnection.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static var temporary: NSFileProviderManager.DisconnectionOptions { get }
```

```c
NSFileProviderManagerDisconnectionOptionsTemporary
```

## Discussion

Include the [`temporary`](./temporary.md) value when the disconnection is temporary, such as when updating the domain. Exclude this value when the disconnection isn’t temporary, like when the user logs out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/disconnectionoptions/temporary)*