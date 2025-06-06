# systemDomainMask

**Framework**: Foundation  
**Kind**: property

A directory for system files provided by Apple (`/System`) .

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
static var systemDomainMask: FileManager.SearchPathDomainMask { get }
```

#### Discussion

This directory can’t be modified.

## See Also

- [static var userDomainMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/userdomainmask.md)
  The user’s home directory—the place to install user’s personal items (`~`).
- [static var localDomainMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/localdomainmask.md)
  The place to install items available to everyone on this machine.
- [static var networkDomainMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/networkdomainmask.md)
  The place to install items available on the network (`/Network`).
- [static var allDomainsMask: FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask/alldomainsmask.md)
  All domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask/systemdomainmask)*