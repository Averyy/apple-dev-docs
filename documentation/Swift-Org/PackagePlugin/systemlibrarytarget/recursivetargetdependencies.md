---
url: "https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget/recursivetargetdependencies"
framework: "Swift-Org/PackagePlugin"
---

# recursiveTargetDependencies

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The transitive closure of all the targets on which the receiver depends.

## Declaration

```swift
var recursiveTargetDependencies: [Target] { get }
```

#### Discussion

Package manager orders the results such that every dependency appears before any other target that depends on it.

The dependencies are sorted in topological sort order.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget/recursivetargetdependencies)*