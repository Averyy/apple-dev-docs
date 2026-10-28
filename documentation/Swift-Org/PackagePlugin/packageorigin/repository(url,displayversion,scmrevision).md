---
url: "https://docs.swift.org/latest/documentation/packageplugin/packageorigin/repository(url:displayversion:scmrevision:)"
framework: "Swift-Org/PackagePlugin"
---

# PackageOrigin.repository(url:displayVersion:scmRevision:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

A package from a Git repository, with a URL and with a textual description of the resolved version or branch name (for display purposes only), and the corresponding SCM revision.

## Declaration

```swift
case repository(url: String, displayVersion: String, scmRevision: String)
```

## Discussion

The revision is the Git commit hash and may be useful for plugins that generates source code that includes version information.

## See Also

### Package Origins
- [case registry(identity: String, displayVersion: String)](./registry%28identity,displayversion%29.md)
  A package from a registry, with an identity and with a textual description of the resolved version or branch name (for display purposes only).
- [PackageOrigin.local(path:)](./local%28path%29.md)
  A local package, referenced by path.
- [PackageOrigin.root](./root.md)
  A root package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packageorigin/repository(url:displayversion:scmrevision:))*