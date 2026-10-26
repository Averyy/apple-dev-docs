---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/packagecollectionadd"
framework: "Swift-Org/PackageManagerDocs"
---

# swift package-collection add

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Add a new collection.

**Availability**:
- Swift 5.5+

#### Overview

This subcommand adds a package collection hosted on the web (HTTPS required):

```bash
$ swift package-collection add https://www.example.com/packages.json
Added "Sample Package Collection" to your package collections.
```

Or found in the local file system:

```bash
$ swift package-collection add file:///absolute/path/to/packages.json
Added "Sample Package Collection" to your package collections.
```

The optional `order` hint can be used to order collections and may potentially influence ranking in search results:

```bash
$ swift package-collection add https://www.example.com/packages.json [--order N]
Added "Sample Package Collection" to your package collections.
```

##### Signed package collections

Publishers of a package collection may [sign a collection to protect its contents](./packagecollections.md#Protecting-package-collections). The package manager will check if a signed collection’s signature is valid before importing it. If the validation check fails, the package manager returns an error:

```bash
$ swift package-collection add https://www.example.com/bad-packages.json
The collection's signature is invalid. If you would like to continue please rerun command with '--skip-signature-check'.
```

Users may continue adding the collection despite the error or preemptively skip the signature check on a package collection by passing the `--skip-signature-check` flag:

```bash
$ swift package-collection add https://www.example.com/packages.json --skip-signature-check
```

For package collections hosted on the web, publishers may ask the package manager to [enforce the signature requirement](./packagesecurity.md#Trusted-root-certificates). If a package collection is expected to be signed but it isn’t, users will see the following error message:

```bash
$ swift package-collection add https://www.example.com/bad-packages.json
The collection is missing required signature, which means it might have been compromised.
```

Users should NOT add the package collection in this case.

For more details on signature validation, see [Signed package collections](./packagesecurity.md#Signed-package-collections).

###### Trusted root certificates

The package manager [validates the certificate](./packagesecurity.md#Trusted-root-certificates) of a signed collection as a part of its signature validation to make sure that the root certificate is trusted.

```bash
$ swift package-collection add https://www.example.com/packages.json
The collection's signature cannot be verified due to missing configuration.
```

Users can explicitly specify they trust a publisher and any collections they publish, by obtaining that publisher’s root certificate and saving it to `~/.swiftpm/config/trust-root-certs`. The root certificates must be DER-encoded. Since the package manager trusts all certificate chains under a root, depending on what roots are installed, some publishers may already be trusted implicitly and users don’t need to explicitly specify each one.

###### Unsigned package collections

Users will get an error when trying to add an unsigned package collection:

```bash
$ swift package-collection add https://www.example.com/packages.json
The collection is not signed. If you would still like to add it please rerun 'add' with '--trust-unsigned'.
```

To continue, users must confirm their trust by passing the `--trust-unsigned` flag:

```bash
$ swift package-collection add https://www.example.com/packages.json --trust-unsigned
```

The `--skip-signature-check` flag has no effects on unsigned collections.

#### Usage

```
package-collection add <collection-url> [--order=<order>]
  [--trust-unsigned] [--skip-signature-check]
  [--package-path=<package-path>] [--cache-path=<cache-path>]
  [--config-path=<config-path>]
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
  [--disable-local-rpath] [--version] [--help]
```

- ****collection-url****: 

*URL of the collection to add.*

- ****–order=<order>****: 

*Sort order for the added collection.*

- ****–trust-unsigned****: 

*Trust the collection even if it is unsigned.*

- ****–skip-signature-check****: 

*Skip signature check if the collection is signed.*

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

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/packagecollectionadd)*