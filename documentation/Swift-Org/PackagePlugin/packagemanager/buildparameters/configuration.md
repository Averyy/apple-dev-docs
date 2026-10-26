---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildparameters/configuration"
framework: "Swift-Org/PackagePlugin"
---

# configuration

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The build configuration to use while building.

## Declaration

```swift
var configuration: BuildConfiguration
```

#### Discussion

Typically whether to build for debug or release.

## See Also

### Inspecting Build Parameters
- [var logging: BuildLogVerbosity](./logging.md)
  Controls the amount of detail in the log returned in the build result.
- [var echoLogs: Bool](./echologs.md)
  A Boolean value that indicates whether to print build logs to the console.
- [var otherCFlags: [String]](./othercflags.md)
  Additional flags to pass to all C compiler invocations for the destination platform.
- [var otherCxxFlags: [String]](./othercxxflags.md)
  Additional flags to pass to all C++ compiler invocations for the destination platform.
- [var otherLinkerFlags: [String]](./otherlinkerflags.md)
  Additional flags to pass to all linker invocations for the destination platform.
- [var otherSwiftcFlags: [String]](./otherswiftcflags.md)
  Additional flags to pass to all Swift compiler invocations for the destination platform.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildparameters/configuration)*