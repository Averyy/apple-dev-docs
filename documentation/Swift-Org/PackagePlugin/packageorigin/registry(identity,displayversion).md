---
url: "https://docs.swift.org/latest/documentation/packageplugin/packageorigin/registry(identity:displayversion:)"
framework: "Swift-Org/PackagePlugin"
---

# PackageOrigin.registry(identity:displayVersion:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

A package from a registry, with an identity and with a textual description of the resolved version or branch name (for display purposes only).

## Declaration

```swift
case registry(identity: String, displayVersion: String)
```

## See Also

### Package Origins
- [case repository(url: String, displayVersion: String, scmRevision: String)](./repository%28url,displayversion,scmrevision%29.md)
  A package from a Git repository, with a URL and with a textual description of the resolved version or branch name (for display purposes only), and the corresponding SCM revision.
- [PackageOrigin.local(path:)](./local%28path%29.md)
  A local package, referenced by path.
- [PackageOrigin.root](./root.md)
  A root package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packageorigin/registry(identity:displayversion:))*