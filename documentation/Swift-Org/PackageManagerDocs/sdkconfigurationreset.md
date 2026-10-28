---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkconfigurationreset"
framework: "Swift-Org/PackageManagerDocs"
---

# swift sdk configuration reset

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Resets configuration properties currently applied to a given Swift SDK and target triple. If no specific property is specified, all of them are reset for the Swift SDK.

**Availability**:
- Swift 6.1+

## Overview

```
sdk configuration reset [--package-path=<package-path>]
  [--cache-path=<cache-path>] [--config-path=<config-path>]
  [--security-path=<security-path>]
  [--scratch-path=<scratch-path>]
  [--swift-sdks-path=<swift-sdks-path>]
  [--toolset=<toolset>...]
  [--pkg-config-path=<pkg-config-path>...] [--sdk-root-path]
  [--swift-resources-path] [--swift-static-resources-path]
  [--include-search-path] [--library-search-path]
  [--toolset-path] <sdk-id> <target-triple> [--version]
  [--help]
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

- ****–sdk-root-path****: 

*Reset custom configuration for a path to a directory containing the SDK root.*

- ****–swift-resources-path****: 

*Reset custom configuration for a path to a directory containing Swift resources for dynamic linking.*

- ****–swift-static-resources-path****: 

*Reset custom configuration for a path to a directory containing Swift resources for static linking.*

- ****–include-search-path****: 

*Reset custom configuration for a path to a directory containing headers.*

- ****–library-search-path****: 

*Reset custom configuration for a path to a directory containing libraries.*

- ****–toolset-path****: 

*Reset custom configuration for a path to a toolset file.*

- ****sdk-id****: 

*An identifier of an already installed Swift SDK. Use the `list` subcommand to see all available identifiers.*

- ****target-triple****: 

*A target triple of the Swift SDK specified by `sdk-id` identifier string.*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*

## See Also

### Deprecated Commands
- [swift sdk configuration set](./sdkconfigurationset.md)
  Sets configuration options for installed Swift SDKs.
- [swift sdk configuration show](./sdkconfigurationshow.md)
  Prints all configuration properties currently applied to a given Swift SDK and target triple.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkconfigurationreset)*