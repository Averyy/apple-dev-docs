---
url: "https://docs.swift.org/latest/documentation/packageplugin/packageorigin/local(path:)"
framework: "Swift-Org/PackagePlugin"
---

# PackageOrigin.local(path:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

A local package, referenced by path.

## Declaration

```swift
case local(path: String)
```

#### Discussion

A local package is unversioned.

## See Also

### Package Origins
- [case repository(url: String, displayVersion: String, scmRevision: String)](./repository%28url,displayversion,scmrevision%29.md)
  A package from a Git repository, with a URL and with a textual description of the resolved version or branch name (for display purposes only), and the corresponding SCM revision.
- [case registry(identity: String, displayVersion: String)](./registry%28identity,displayversion%29.md)
  A package from a registry, with an identity and with a textual description of the resolved version or branch name (for display purposes only).
- [PackageOrigin.root](./root.md)
  A root package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packageorigin/local(path:))*