---
url: "https://docs.swift.org/latest/documentation/packageplugin/packageorigin/root"
framework: "Swift-Org/PackagePlugin"
---

# PackageOrigin.root

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

A root package.

## Declaration

```swift
case root
```

#### Discussion

The root package is unversioned.

## See Also

### Package Origins
- [case repository(url: String, displayVersion: String, scmRevision: String)](./repository%28url,displayversion,scmrevision%29.md)
  A package from a Git repository, with a URL and with a textual description of the resolved version or branch name (for display purposes only), and the corresponding SCM revision.
- [case registry(identity: String, displayVersion: String)](./registry%28identity,displayversion%29.md)
  A package from a registry, with an identity and with a textual description of the resolved version or branch name (for display purposes only).
- [PackageOrigin.local(path:)](./local%28path%29.md)
  A local package, referenced by path.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packageorigin/root)*