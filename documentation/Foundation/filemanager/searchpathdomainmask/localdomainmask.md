# localDomainMask

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The place to install items available to everyone on this machine.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var localDomainMask: FileManager.SearchPathDomainMask { get }
```

```c
NSLocalDomainMask
```

## See Also

### Specifying Search Path Domains
- [static var userDomainMask: FileManager.SearchPathDomainMask](./userdomainmask.md)
  The user’s home directory—the place to install user’s personal items (`~`).
- [static var networkDomainMask: FileManager.SearchPathDomainMask](./networkdomainmask.md)
  The place to install items available on the network (`/Network`).
- [static var systemDomainMask: FileManager.SearchPathDomainMask](./systemdomainmask.md)
  A directory for system files provided by Apple (`/System`) .
- [static var allDomainsMask: FileManager.SearchPathDomainMask](./alldomainsmask.md)
  All domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask/localdomainmask)*