---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/5.5"
framework: "Swift-Org/PackageManagerDocs"
---

# SwiftPM 5.5 Release Notes

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

### Package Collections

You can now use package collections to discover, manage, and publish curated lists of packages. Package collections are authored as static JSON documents and can be published to the web or distributed to local file systems. SwiftPM and Xcode locally share the same package collections, so either interface can manage your added collections.

To try the official Apple Swift Packages collection, run:

```
swift package-collection add https://developer.apple.com/swift/packages/collections/apple.json
```

Then, to see which packages are included in that collection and can now be imported in your code, run:

```
swift package-collection describe https://developer.apple.com/swift/packages/collections/apple.json
```

For more information about usage and how to publish your own package collections, see the [Package Collections documentation](https://docs.swift.org/latest/documentation/PackageCollections.md).

### Executable target testing

Test targets can now link against executable targets as if they were libraries, so that they can test any data structures or algorithms in them. All the code in the executable except for the main entry point itself is available to the unit test. Separate executables are still linked, and can be tested as a subprocess in the same way as before. This feature is available to tests defined in packages that have a tools version of `5.5` or newer. (#3316)

### Manifest API improvements

Two new dependency convenience initializers are now available (#3292, #3310):

```
.package(url: String, revision: String)
.package(url: String, branch: String)
```

Target-based dependency resolution has also been improved. A more intuitive `.product(name:, package:)` syntax is now accepted, where `package` is the package name as defined by the package URL. (#3280)

### Other improvements

`@main` can now be used in a single-source file executable as long as the name of the source file isn’t `main.swift`. To work around special compiler semantics with single-file modules, SwiftPM now passes `-parse-as-library` when compiling an executable module that contains a single Swift source file whose name is not `main.swift`. This feature is available in packages that have a tools version of `5.5` or newer. (#3410)

An issue where resolution of packages with binary dependencies failed to extract the binary archive was fixed. (#3507)

## See Also

- [SwiftPM 6.4 Release Notes](./api-6.4.md)
  Swift Package Manager 6.4 makes Swift Build the new default build system, providing a unified build experience across all platforms Swift supports. This release also adds first-class support for generating Software Bill of Materials (SBOM) documents.
- [SwiftPM 6.3 Release Notes](./api-6.3.md)
- [SwiftPM 5.9 Release Notes](./api-5.9.md)
- [SwiftPM 5.8 Release Notes](./api-5.8.md)
- [SwiftPM 5.7 Release Notes](./api-5.7.md)
- [SwiftPM 5.6 Release Notes](./api-5.6.md)
- [SwiftPM 5.4 Release Notes](./api-5.4.md)
  SwiftPM 5.4 includes several improvements, all of which are opt-in based on specifying a tools version of 5.4.
- [SwiftPM 5.3 Release Notes](./api-5.3.md)
  SwiftPM brings several new features in version 5.3, all of which are opt-in based on the tools-version.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/5.5)*