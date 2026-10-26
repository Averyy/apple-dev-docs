---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/packageregistrypublish"
framework: "Swift-Org/PackageManagerDocs"
---

# swift package-registry publish

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Publish to a registry.

**Availability**:
- Swift 5.9+

#### Overview

This command creates a source archive for the package release, optionally signs it, and finally [publishes the package release](./registryserverspecification.md#46-Create-a-package-release) to the registry.

If authentication is required for package publication, package authors should [configure registry login](./usingswiftpackageregistry.md#Registry-authentication) before running `publish`.

##### Publisher TOFU

Some certificates allow the package manager to extract additional information about the signing identity. For packages signed with these certificates, package manager performs publisher TOFU (trust-on-first-use) to ensure the signer remains the same across all versions of the package.

The `--resolver-signing-entity-checking` option controls whether a publisher mismatch should result in a warning (`warn`) or error (`strict`). Data used by publisher TOFU is saved to `~/.swiftpm/security/signing-entities/`.

For more details on trust-on-first-use, see [Trust on First Use](./packagesecurity.md#Trust-on-First-Use).

###### Package release metadata

Package authors can specify a custom location of the package release metadata file by setting the `--metadata-path` option of the `publish` subcommand. Otherwise, package manager looks for a file named `package-metadata.json` in the package directory.

Contents of the metadata file must conform to the [JSON schema](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0391-package-registry-publish.md#package-release-metadata-standards) defined in SE-0391.

Refer to the [registry specification](./registryserverspecification.md#422-Package-release-metadata-standards) for any additional requirements.

###### Package signing

If a registry requires signing, package authors need to sign the package release by either setting the `signing-identity` (for reading from operating system’s identity store such as Keychain in macOS), or `private-key-path` and `cert-chain-paths` (for reading from files) options of the `publish` subcommand. This allows Package manager to locate the signing key and certificate.

For more information on package signing, see [Signed packages from a registry](./packagesecurity.md#Signed-packages-from-a-registry).

##### Usage

```
package-registry publish [--package-path=<package-path>]
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
  [--disable-local-rpath] <package-id> <package-version>
  [--url|registry-url=<url>]
  [--scratch-directory=<scratch-directory>]
  [--metadata-path=<metadata-path>]
  [--signing-identity=<signing-identity>]
  [--private-key-path=<private-key-path>]
  [--cert-chain-paths=<cert-chain-paths>...]
  [--allow-insecure-http] [--dry-run] [--version] [--help]
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

- ****package-id****: 

*The package identifier.*

- ****package-version****: 

*The package release version being created.*

- ****–url|registry-url=<url>****: 

*The registry URL.*

- ****–scratch-directory=<scratch-directory>****: 

*The path of the directory where working file(s) will be written.*

- ****–metadata-path=<metadata-path>****: 

*The path to the package metadata JSON file if it is not ‘package-metadata.json’ in the package directory.*

- ****–signing-identity=<signing-identity>****: 

*The label of the signing identity to be retrieved from the system’s identity store if supported.*

- ****–private-key-path=<private-key-path>****: 

*The path to the certificate’s PKCS#8 private key (DER-encoded).*

- ****–cert-chain-paths=<cert-chain-paths>****: 

*Path(s) to the signing certificate (DER-encoded) and optionally the rest of the certificate chain. Certificates should be ordered with the leaf first and the root last.*

- ****–allow-insecure-http****: 

*Allow using a non-HTTPS registry URL.*

- ****–dry-run****: 

*Dry run only; prepare the archive and sign it but do not publish to the registry.*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*

## See Also

### Accessing Registries
- [swift package-registry login](./packageregistrylogin.md)
  Log in to a registry.
- [swift package-registry logout](./packageregistrylogout.md)
  Log out from a registry.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/packageregistrypublish)*