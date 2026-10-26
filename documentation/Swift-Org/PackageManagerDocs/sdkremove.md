---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkremove"
framework: "Swift-Org/PackageManagerDocs"
---

# swift sdk remove

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Removes a previously installed Swift SDK bundle from the filesystem.

**Availability**:
- Swift 6.1+

#### Overview

```
sdk remove [--package-path=<package-path>]
  [--cache-path=<cache-path>] [--config-path=<config-path>]
  [--security-path=<security-path>]
  [--scratch-path=<scratch-path>]
  [--swift-sdks-path=<swift-sdks-path>]
  [--toolset=<toolset>...]
  [--pkg-config-path=<pkg-config-path>...]
  <sdk-id-or-bundle-name> [--version] [--help]
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

- ****sdk-id-or-bundle-name****: 

*Name of the Swift SDK bundle or ID of the Swift SDK to remove from the filesystem.*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkremove)*