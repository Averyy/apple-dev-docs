---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildparameters/init(configuration:logging:echologs:)"
framework: "Swift-Org/PackagePlugin"
---

# init(configuration:logging:echoLogs:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: init  
**Role**: Initializer

Creates a new sert of build parameters.

## Declaration

```swift
init(configuration: BuildConfiguration = .debug, logging: BuildLogVerbosity = .concise, echoLogs: Bool = false)
```

## Parameters

- `configuration`: The build configuration to use.
- `logging`: The level of detail to include in the build logs returned in the build result.
- `echoLogs`: Whether to print build logs to the console.

## See Also

### Creating Build Parameters
- [PackageManager.BuildConfiguration](../buildconfiguration.md)
  The configuration to use for the build.
- [PackageManager.BuildLogVerbosity](../buildlogverbosity.md)
  The amount of detail to include in a build log.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildparameters/init(configuration:logging:echologs:))*