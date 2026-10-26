---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult/builtartifacts"
framework: "Swift-Org/PackagePlugin"
---

# builtArtifacts

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The artifacts built from the products in the package.

## Declaration

```swift
var builtArtifacts: [BuiltArtifact]
```

#### Discussion

Intermediates such as object files produced from individual targets aren’t listed.

## See Also

### Inspecting a Build Result
- [var logText: String](./logtext.md)
  The log output.
- [var succeeded: Bool](./succeeded.md)
  A Boolean value that indicates whether the build succeeded or failed.
- [PackageManager.BuildResult.BuiltArtifact](./builtartifact.md)
  The single artifact produced during a build.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult/builtartifacts)*