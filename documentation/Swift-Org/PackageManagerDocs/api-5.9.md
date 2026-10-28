---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/5.9"
framework: "Swift-Org/PackageManagerDocs"
---

# SwiftPM 5.9 Release Notes

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

## Cross compilation

SwiftPM now supports cross compilation based on the Swift SDK bundle format. While the feature is still considered experimental, we invite users to try it out and provide feedback.

## Package registry

SwiftPM can now publish to a registry following the specification defined in SE-0391, as well as support signed packages, which may be required by a registry. Trust-on-first-use (TOFU) validation checks can now use signing identities in addition to fingerprints, and are enforced for source archives as well as package manifests.

## Embedded resources

Basic support for a new `.embedInCode` resource rule which allows embedding the contents of the resource into the executable code by generating a byte array

```
struct PackageResources {
  static let best_txt: [UInt8] = [104,101,108,108,111,32,119,111,114,108,100,10]
}
```

## Other improvements

The `CompilerPluginSupport` module enables defining macro targets. Macro targets allow authoring and distributing custom Swift macros as APIs in a library.

Packages can use the new `package` access modifier, allowing access of symbols in another target / module within the same package without making them public. SwiftPM automatically sets the new compiler configuration to ensure this feature works out-of-the-box for packages.

The `allowNetworkConnections(scope:reason:)` setting gives a command plugin permissions to access the network. Permissions can be scoped to Unix domain sockets as well as local or remote IP connections, with an option to limit by port. For non-interactive use cases, the `--allow-network-connections` command-line flag allows network connections for a particular scope.

When a package contains a single target, sources may be distributed anywhere within the `./Sources` directory. If sources are placed in a subdirectory under `./Sources/<target>`, or there is more than one target, the existing expectation for sources apply

Build tool plugins can be used with C-family targets

## See Also

- [SwiftPM 6.4 Release Notes](./api-6.4.md)
  Swift Package Manager 6.4 makes Swift Build the new default build system, providing a unified build experience across all platforms Swift supports. This release also adds first-class support for generating Software Bill of Materials (SBOM) documents.
- [SwiftPM 6.3 Release Notes](./api-6.3.md)
- [SwiftPM 5.8 Release Notes](./api-5.8.md)
- [SwiftPM 5.7 Release Notes](./api-5.7.md)
- [SwiftPM 5.6 Release Notes](./api-5.6.md)
- [SwiftPM 5.5 Release Notes](./api-5.5.md)
- [SwiftPM 5.4 Release Notes](./api-5.4.md)
  SwiftPM 5.4 includes several improvements, all of which are opt-in based on specifying a tools version of 5.4.
- [SwiftPM 5.3 Release Notes](./api-5.3.md)
  SwiftPM brings several new features in version 5.3, all of which are opt-in based on the tools-version.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/5.9)*