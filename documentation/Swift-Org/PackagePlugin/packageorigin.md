---
url: "https://docs.swift.org/latest/documentation/packageplugin/packageorigin"
framework: "Swift-Org/PackagePlugin"
---

# PackageOrigin

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The origin of a package.

## Declaration

```swift
enum PackageOrigin
```

## Topics

### Package Origins
- [case repository(url: String, displayVersion: String, scmRevision: String)](./packageorigin/repository%28url,displayversion,scmrevision%29.md)
  A package from a Git repository, with a URL and with a textual description of the resolved version or branch name (for display purposes only), and the corresponding SCM revision.
- [case registry(identity: String, displayVersion: String)](./packageorigin/registry%28identity,displayversion%29.md)
  A package from a registry, with an identity and with a textual description of the resolved version or branch name (for display purposes only).
- [PackageOrigin.local(path:)](./packageorigin/local%28path%29.md)
  A local package, referenced by path.
- [PackageOrigin.root](./packageorigin/root.md)
  A root package.

## See Also

### Inspecting the Package Representation
- [struct Package](./package.md)
  A single package in a graph of packages.
- [struct ToolsVersion](./toolsversion.md)
  A version of Swift package manager on whose semantics a package relies.
- [struct PackageDependency](./packagedependency.md)
  A resolved dependency of a package.
- [protocol Product](./product.md)
  A single product defined in a package.
- [struct ExecutableProduct](./executableproduct.md)
  An executable product defined in a package.
- [struct LibraryProduct](./libraryproduct.md)
  A library product defined in a package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packageorigin)*