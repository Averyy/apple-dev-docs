---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkconfigurationshow"
framework: "Swift-Org/PackageManagerDocs"
---

# swift sdk configuration show

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Prints all configuration properties currently applied to a given Swift SDK and target triple.

**Availability**:
- Swift 6.1+

## Overview

```
sdk configuration show [--package-path=<package-path>]
  [--cache-path=<cache-path>] [--config-path=<config-path>]
  [--security-path=<security-path>]
  [--scratch-path=<scratch-path>]
  [--swift-sdks-path=<swift-sdks-path>]
  [--toolset=<toolset>...]
  [--pkg-config-path=<pkg-config-path>...] <sdk-id>
  <target-triple> [--version] [--help]
```

- ****–package-path=<package-path>****: 

*Specify the package path to operate on (default current directory). This changes the working directory before any other operation.*

- ****–cache-path=<cache-path>****: 

*Specify the shared cache directory path.*

- ****–config-path=<config-path>****: 

*Specify the shared configuration directory path.*

- ****–security-path=<security-path>****: 

*Specify the shared security directory path.*

- ****–scratch-path=<scratch-path>****: 

*Specify a custom scratch directory path. (default .build)*

- ****–swift-sdks-path=<swift-sdks-path>****: 

*Path to the directory containing installed Swift SDKs.*

- ****–toolset=<toolset>****: 

*Specify a toolset JSON file to use when building for the target platform. Use the option multiple times to specify more than one toolset. Toolsets will be merged in the order they’re specified into a single final toolset for the current build.*

- ****–pkg-config-path=<pkg-config-path>****: 

*Specify alternative path to search for pkg-config `.pc` files. Use the option multiple times to specify more than one path.*

- ****sdk-id****: 

*An identifier of an already installed Swift SDK. Use the `list` subcommand to see all available identifiers.*

- ****target-triple****: 

*The target triple of the Swift SDK to configure.*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*

## See Also

### Deprecated Commands
- [swift sdk configuration set](./sdkconfigurationset.md)
  Sets configuration options for installed Swift SDKs.
- [swift sdk configuration reset](./sdkconfigurationreset.md)
  Resets configuration properties currently applied to a given Swift SDK and target triple. If no specific property is specified, all of them are reset for the Swift SDK.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkconfigurationshow)*