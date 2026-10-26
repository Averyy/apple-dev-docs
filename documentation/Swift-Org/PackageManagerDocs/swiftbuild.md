---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/swiftbuild"
framework: "Swift-Org/PackageManagerDocs"
---

# swift build

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Build sources into binary products.

#### Overview

```
build [--package-path=<package-path>]
  [--cache-path=<cache-path>] [--config-path=<config-path>]
  [--security-path=<security-path>]
  [--scratch-path=<scratch-path>]
  [--swift-sdks-path=<swift-sdks-path>]
  [--toolset=<toolset>...]
  [--pkg-config-path=<pkg-config-path>...]
  [--enable-dependency-cache|disable-dependency-cache]
  [--enable-build-manifest-caching|disable-build-manifest-caching]
  [--manifest-cache=<manifest-cache>]
  [--enable-experimental-prebuilts|disable-experimental-prebuilts]
  [--verbose] [--very-verbose|vv] [--quiet]
  [--color-diagnostics|no-color-diagnostics]
  [--disable-sandbox] [--netrc]
  [--enable-netrc|disable-netrc] [--netrc-file=<netrc-file>]
  [--enable-keychain|disable-keychain]
  [--resolver-fingerprint-checking=<resolver-fingerprint-checking>]
  [--resolver-signing-entity-checking=<resolver-signing-entity-checking>]
  [--enable-signature-validation|disable-signature-validation]
  [--enable-prefetching|disable-prefetching]
  [--force-resolved-versions|disable-automatic-resolution|only-use-versions-from-resolved-file]
  [--skip-update] [--disable-scm-to-registry-transformation]
  [--use-registry-identity-for-scm] 
  [--replace-scm-with-registry]
  [--default-registry-url=<default-registry-url>]
  [--configuration=<configuration>] [--=<Xcc>...]
  [--=<Xswiftc>...] [--=<Xlinker>...] [--=<Xcxx>...]
  [--triple=<triple>] [--sdk=<sdk>]
  [--toolchain=<toolchain>] [--swift-sdk=<swift-sdk>]
  [--sanitize=<sanitize>...]
  [--auto-index-store|enable-index-store|disable-index-store]
  [--enable-parseable-module-interfaces] [--jobs=<jobs>]
  [--use-integrated-swift-driver]
  [--explicit-target-dependency-import-check=<explicit-target-dependency-import-check>]
  [--build-system=<build-system>] [--=<debug-info-format>]
  [--enable-dead-strip|disable-dead-strip]
  [--disable-local-rpath] [--build-tests]
  [--enable-code-coverage|disable-code-coverage]
  [--show-bin-path] [--print-manifest-job-graph]
  [--print-pif-manifest-graph] [--target=<target>]
  [--product=<product>] [--enable-xctest|disable-xctest]
  [--enable-swift-testing|disable-swift-testing]
  [--traits=<traits>] [--enable-all-traits]
  [--disable-default-traits]
  [--static-swift-stdlib|no-static-swift-stdlib]
  [--sbom-spec=<sbom-spec>...] [--sbom-output-dir=<sbom-output-dir>]
  [--sbom-filter=<sbom-filter>] [--sbom-warning-only]
  [--version] [--help]
```

SEE ALSO: [swift run](./swiftrun.md), [swift package](./swiftpackagecommands.md), [swift test](./swifttest.md)

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

- ****–enable-dependency-cache|disable-dependency-cache****: 

*Use a shared cache when fetching dependencies.*

- ****–enable-build-manifest-caching|disable-build-manifest-caching****: 
- ****–manifest-cache=<manifest-cache>****: 

*Caching mode of Package.swift manifests. Valid values are: (shared: shared cache, local: package’s build directory, none: disabled)*

- ****–enable-experimental-prebuilts|disable-experimental-prebuilts****: 

*Whether to use prebuilt swift-syntax libraries for macros.*

- ****–verbose****: 

*Increase verbosity to include informational output.*

- ****–very-verbose|vv****: 

*Increase verbosity to include debug output.*

- ****–quiet****: 

*Decrease verbosity to only include error output.*

- ****–color-diagnostics|no-color-diagnostics****: 

*Enables or disables color diagnostics when printing to a TTY. By default, color diagnostics are enabled when connected to a TTY and disabled otherwise.*

- ****–disable-sandbox****: 

*Disable using the sandbox when executing subprocesses.*

- ****–netrc****: 

*Use netrc file even in cases where other credential stores are preferred.*

- ****–enable-netrc|disable-netrc****: 

*Load credentials from a netrc file.*

- ****–netrc-file=<netrc-file>****: 

*Specify the netrc file path.*

- ****–enable-keychain|disable-keychain****: 

*Search credentials in macOS keychain.*

- ****–resolver-fingerprint-checking=<resolver-fingerprint-checking>****: 
- ****–resolver-signing-entity-checking=<resolver-signing-entity-checking>****: 
- ****–enable-signature-validation|disable-signature-validation****: 

*Validate signature of a signed package release downloaded from registry.*

- ****–enable-prefetching|disable-prefetching****: 
- ****–force-resolved-versions|disable-automatic-resolution|only-use-versions-from-resolved-file****: 

*Only use versions from the Package.resolved file and fail resolution if it is out-of-date.*

- ****–skip-update****: 

*Skip updating dependencies from their remote during a resolution.*

- ****–disable-scm-to-registry-transformation****: 

*Disable source control to registry transformation.*

- ****–use-registry-identity-for-scm****: 

*Look up source control dependencies in the registry and use their registry identity when possible to help deduplicate across the two origins.*

- ****–replace-scm-with-registry****: 

*Look up source control dependencies in the registry and use the registry to retrieve them instead of source control when possible.*

- ****–default-registry-url=<default-registry-url>****: 

*Default registry URL to use, instead of the registries.json configuration file.*

- ****–configuration=<configuration>****: 

*Build with configuration*

- ****–=<Xcc>****: 

*Pass flag through to all C compiler invocations.*

- ****–=<Xswiftc>****: 

*Pass flag through to all Swift compiler invocations.*

- ****–=<Xlinker>****: 

*Pass flag through to all linker invocations.*

- ****–=<Xcxx>****: 

*Pass flag through to all C++ compiler invocations.*

- ****–triple=<triple>****: 
- ****–sdk=<sdk>****: 
- ****–toolchain=<toolchain>****: 
- ****–swift-sdk=<swift-sdk>****: 

*Filter for selecting a specific Swift SDK to build with.*

- ****–sanitize=<sanitize>****: 

*Turn on runtime checks for erroneous behavior, possible values: address, thread, undefined, scudo.*

- ****–auto-index-store|enable-index-store|disable-index-store****: 

*Enable or disable indexing-while-building feature.*

- ****–enable-parseable-module-interfaces****: 
- ****–jobs=<jobs>****: 

*The number of jobs to spawn in parallel during the build process.*

- ****–use-integrated-swift-driver****: 
- ****–explicit-target-dependency-import-check=<explicit-target-dependency-import-check>****: 

*A flag that indicates this build should check whether targets only import their explicitly-declared dependencies.*

- ****–build-system=<build-system>****: 
- ****–=<debug-info-format>****: 

*The Debug Information Format to use.*

- ****–enable-dead-strip|disable-dead-strip****: 

*Disable/enable dead code stripping by the linker.*

- ****–disable-local-rpath****: 

*Disable adding $ORIGIN/@loader_path to the rpath by default.*

- ****–build-tests****: 

*Build both source and test targets.*

- ****–enable-code-coverage|disable-code-coverage****: 

*Enable code coverage.*

- ****–show-bin-path****: 

*Print the binary output path.*

- ****–print-manifest-job-graph****: 

*Write the command graph for the build manifest as a Graphviz file.*

- ****–print-pif-manifest-graph****: 

*Write the PIF JSON sent to Swift Build as a Graphviz file.*

- ****–target=<target>****: 

*Build the specified target.*

- ****–product=<product>****: 

*Build the specified product.*

- ****–enable-xctest|disable-xctest****: 

*Enable support for XCTest.*

- ****–enable-swift-testing|disable-swift-testing****: 

*Enable support for Swift Testing.*

- ****–traits=<traits>****: 

*Enables the passed traits of the package. Multiple traits can be specified by providing a comma separated list e.g. `--traits Trait1,Trait2`. When enabling specific traits the defaults traits need to explictily enabled as well by passing `defaults` to this command.*

- ****–enable-all-traits****: 

*Enables all traits of the package.*

- ****–disable-default-traits****: 

*Disables all default traits of the package.*

- ****–static-swift-stdlib|no-static-swift-stdlib****: 

*Link Swift stdlib statically.*

- ****–sbom-spec=<sbom-spec>****: 

*Set the SBOM specification(s) and generate SBOM(s).*

- ****–sbom-output-dir=<sbom-output-dir>****: 

*The absolute or relative directory path to generate the SBOM(s) in. Must be used with –sbom-spec. (default: <scratch_path>/sboms).*

- ****–sbom-filter=<sbom-filter>****: 

*Filter the SBOM components and dependencies by products and/or packages. Must be used with –sbom-spec.*

- ****–sbom-warning-only****: 

*Treat SBOM generation errors as warnings. Must be used with –sbom-spec. (default: false).*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*

#### build.help

Show subcommand help information.

```
build help [<subcommands>...] 
```

## See Also

### Swift Commands
- [swift test](./swifttest.md)
  Build and run tests.
- [swift package](./swiftpackagecommands.md)
  Subcommands to update and inspect your Swift package.
- [swift sdk](./swiftsdkcommands.md)
  Perform operations on Swift SDKs.
- [swift package-registry](./swiftpackageregistrycommands.md)
  Interact with package registry and manage related configuration.
- [swift package-collection](./swiftpackagecollectioncommands.md)
  Interact with package collections.
- [swift run](./swiftrun.md)
  Build and run an executable product.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/swiftbuild)*