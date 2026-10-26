---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/packagedumpsymbolgraph"
framework: "Swift-Org/PackageManagerDocs"
---

# swift package dump-symbol-graph

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Dump symbol graphs.

#### Overview

```
package dump-symbol-graph [--package-path=<package-path>]
  [--cache-path=<cache-path>] [--config-path=<config-path>]
  [--security-path=<security-path>]
  [--scratch-path=<scratch-path>]
  [--swift-sdks-path=<swift-sdks-path>]
  [--toolset=<toolset>...]
  [--pkg-config-path=<pkg-config-path>...]
  [--enable-dependency-cache] [--disable-dependency-cache]
  [--enable-build-manifest-caching]
  [--disable-build-manifest-caching]
  [--manifest-cache=<manifest-cache>]
  [--enable-experimental-prebuilts]
  [--disable-experimental-prebuilts] [--verbose]
  [--very-verbose|vv] [--quiet] [--color-diagnostics]
  [--no-color-diagnostics] [--disable-sandbox] [--netrc]
  [--enable-netrc] [--disable-netrc]
  [--netrc-file=<netrc-file>] [--enable-keychain]
  [--disable-keychain]
  [--resolver-fingerprint-checking=<resolver-fingerprint-checking>]
  [--resolver-signing-entity-checking=<resolver-signing-entity-checking>]
  [--enable-signature-validation]
  [--disable-signature-validation] [--enable-prefetching]
  [--disable-prefetching]
  [--force-resolved-versions|disable-automatic-resolution|only-use-versions-from-resolved-file]
  [--skip-update] [--disable-scm-to-registry-transformation]
  [--use-registry-identity-for-scm]
  [--replace-scm-with-registry]
  [--default-registry-url=<default-registry-url>]
  [--configuration=<configuration>] [--=<Xcc>...]
  [--=<Xswiftc>...] [--=<Xlinker>...] [--=<Xcxx>...]
  [--triple=<triple>] [--sdk=<sdk>] [--toolchain=<toolchain>]
  [--swift-sdk=<swift-sdk>] [--sanitize=<sanitize>...]
  [--auto-index-store] [--enable-index-store]
  [--disable-index-store]
  [--enable-parseable-module-interfaces] [--jobs=<jobs>]
  [--use-integrated-swift-driver]
  [--explicit-target-dependency-import-check=<explicit-target-dependency-import-check>]
  [--build-system=<build-system>] [--=<debug-info-format>]
  [--enable-dead-strip] [--disable-dead-strip]
  [--disable-local-rpath] [--pretty-print]
  [--skip-synthesized-members]
  [--minimum-access-level=<minimum-access-level>]
  [--skip-inherited-docs] [--include-spi-symbols]
  [--emit-extension-block-symbols]
  [--omit-extension-block-symbols] [--version] [--help]
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

- ****–pretty-print****: 

*Pretty-print the output JSON.*

- ****–skip-synthesized-members****: 

*Skip members inherited through classes or default implementations.*

- ****–minimum-access-level=<minimum-access-level>****: 

*Include symbols with this access level or more. Possible values: private | fileprivate | internal | package | public | open.*

- ****–skip-inherited-docs****: 

*Skip emitting doc comments for members inherited through classes or default implementations.*

- ****–include-spi-symbols****: 

*Add symbols with SPI information to the symbol graph.*

- ****–emit-extension-block-symbols|omit-extension-block-symbols****: 

*Emit extension block symbols for extensions to external types or directly associate members and conformances with the extended nominal.*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*

## See Also

### Inspecting packages
- [swift package describe](./packagedescribe.md)
  Describe the current package.
- [swift package show-dependencies](./packageshowdependencies.md)
  Print the resolved dependency graph.
- [swift package show-executables](./packageshowexecutables.md)
  List the available executables from this package.
- [swift package show-traits](./packageshowtraits.md)
  List the available traits for a package.
- [swift package tools-version](./packagetoolsversion.md)
  Manipulate tools version of the current package.
- [swift package dump-package](./packagedumppackage.md)
  Print parsed Package.swift as JSON.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/packagedumpsymbolgraph)*