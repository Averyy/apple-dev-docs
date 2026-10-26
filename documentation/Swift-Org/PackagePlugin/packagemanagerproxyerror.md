---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanagerproxyerror"
framework: "Swift-Org/PackagePlugin"
---

# PackageManagerProxyError

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

Errors from methods using the package manager.

## Declaration

```swift
enum PackageManagerProxyError
```

## Topics

### Types of Proxy Errors from Package Manager
- [PackageManagerProxyError.unimplemented(_:)](./packagemanagerproxyerror/unimplemented%28_%29.md)
  Indicates that the functionality isn’t implemented in the plugin host.
- [PackageManagerProxyError.unspecified(_:)](./packagemanagerproxyerror/unspecified%28_%29.md)
  An unspecified other kind of error from the package manager proxy.
### Default Implementations
- [Error Implementations](./packagemanagerproxyerror/error-implementations.md)

## Relationships

### Conforms To
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Interacting with Package Manager
- [struct PackageManager](./packagemanager.md)
  Provides specialized information and services from the Swift Package Manager or an IDE that supports Swift packages.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanagerproxyerror)*