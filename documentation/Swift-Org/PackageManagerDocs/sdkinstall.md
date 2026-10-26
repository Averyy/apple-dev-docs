---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkinstall"
framework: "Swift-Org/PackageManagerDocs"
---

# swift sdk install

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Installs a given Swift SDK bundle to a location discoverable by SwiftPM.

**Availability**:
- Swift 6.1+

#### Overview

If the artifact bundle is at a remote location, it’s downloaded to local filesystem first.

```
sdk install [--package-path=<package-path>]
  [--cache-path=<cache-path>] [--config-path=<config-path>]
  [--security-path=<security-path>]
  [--scratch-path=<scratch-path>]
  [--swift-sdks-path=<swift-sdks-path>]
  [--toolset=<toolset>...]
  [--pkg-config-path=<pkg-config-path>...]
  <bundle-path-or-url> [--checksum=<checksum>]
  [--color-diagnostics] [--no-color-diagnostics] [--version]
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

- ****bundle-path-or-url****: 

*A local filesystem path or a URL of a Swift SDK bundle to install.*

- ****–checksum=<checksum>****: 

*The checksum of the bundle generated with `swift package compute-checksum`.*

- ****–color-diagnostics|no-color-diagnostics****: 

*Enables or disables color diagnostics when printing to a TTY. By default, color diagnostics are enabled when connected to a TTY and disabled otherwise.*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/sdkinstall)*