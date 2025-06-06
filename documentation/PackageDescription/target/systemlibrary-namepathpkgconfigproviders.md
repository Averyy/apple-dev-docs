# systemLibrary(name:path:pkgConfig:providers:)

**Framework**: PackageDescription  
**Kind**: method

Creates a system library target.

## Declaration

```swift
static func systemLibrary(name: String, path: String? = nil, pkgConfig: String? = nil, providers: [SystemPackageProvider]? = nil) -> Target
```

#### Discussion

Use system library targets to adapt a library installed on the system to work with Swift packages. Such libraries are generally installed by system package managers (such as Homebrew and apt-get) and exposed to Swift packages by providing a `modulemap` file along with other metadata such as the library’s `pkgConfig` name.

## Parameters

- `name`: The name of the target.
- `path`: The custom path for the target. By default, a targets sources   are expected to be located in the predefined search paths, such as   . Do not escape the package root;   that is, values like   or   are invalid.
- `pkgConfig`: The name of the   file for this system library.
- `providers`: The providers for this system library.

## See Also

- [let pkgConfig: String?](target/pkgconfig.md)
  The name of the package configuration file, without extension, for the system library target.
- [let providers: [SystemPackageProvider]?](target/providers.md)
  The providers array for a system library target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/systemlibrary(name:path:pkgconfig:providers:))*