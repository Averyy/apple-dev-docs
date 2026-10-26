---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/5.7"
framework: "Swift-Org/PackageManagerDocs"
---

# SwiftPM 5.7 Release Notes

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

##### Package Plugins

[SE-0303: Build tool plugins](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0303-swiftpm-extensible-build-tools.md) and [SE-0332: Command Plugins](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0332-swiftpm-command-plugins.md) which were first introduced in Swift 5.6 have been further refined, with support for generating resources and improved diagnostics. To learn more, refer to the [Getting Started with Plugins](https://docs.swift.org/latest/documentation/Plugins.md) guide.

##### Package Registry Support

SwiftPM now supports package registry related capabilities introduced by [SE-0292](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0292-package-registry-service.md) and the corresponding [service specification](https://docs.swift.org/latest/documentation/Registry.md). With the exception of package publishing, SwiftPM can resolve and download dependencies from any compliant registry using the defined APIs.

To get started, users will need to specify their package registry by running the `swift package-registry set` subcommand or editing the `registries.json` configuration file. `swift package` tool’s `--use-registry-identity-for-scm` and `--replace-scm-with-registry` options might also be of interest.

##### Module Aliasing For Disambiguation

Modules with the same name from different packages can now be disambiguated by module aliasing [SE-0339](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0339-module-aliasing-for-disambiguation.md). When adding a product dependency for a target in a package manifest, use a new parameter `moduleAliases` to provide a new unique name for a conflicting module.

- [#4119]

  Add a `--disable-testable-imports` flag to `swift test` with which tests are built without the testability feature (`import @testable` disabled).

## See Also

- [SwiftPM 6.4 Release Notes](./api-6.4.md)
  Swift Package Manager 6.4 makes Swift Build the new default build system, providing a unified build experience across all platforms Swift supports. This release also adds first-class support for generating Software Bill of Materials (SBOM) documents.
- [SwiftPM 6.3 Release Notes](./api-6.3.md)
- [SwiftPM 5.9 Release Notes](./api-5.9.md)
- [SwiftPM 5.8 Release Notes](./api-5.8.md)
- [SwiftPM 5.6 Release Notes](./api-5.6.md)
- [SwiftPM 5.5 Release Notes](./api-5.5.md)
- [SwiftPM 5.4 Release Notes](./api-5.4.md)
  SwiftPM 5.4 includes several improvements, all of which are opt-in based on specifying a tools version of 5.4.
- [SwiftPM 5.3 Release Notes](./api-5.3.md)
  SwiftPM brings several new features in version 5.3, all of which are opt-in based on the tools-version.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/5.7)*