---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/packageregistrylogin"
framework: "Swift-Org/PackageManagerDocs"
---

# swift package-registry login

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Log in to a registry.

**Availability**:
- Swift 5.9+

#### Overview

The package manager verifies the credentials using the registry service’s login API. If it returns a successful response, the credentials are persisted to the operating system’s credential store (for example, Keychain in macOS). On non-macOS platforms, or if the `--netrc` flag is provided, the credentials are persisted to the user-level .netrc (which by default is located at `~/.netrc`). The user-level configuration file located at ~/.swiftpm/configuration/registries.json is also updated.

The `url` should be the registry’s base URL (for example, `https://example-registry.com`). If the location of the login API endpoint is not `/login` (for example, `https://example-registry.com/api/v1/login`), provide the full URL.

The URL must be HTTPS.

The table below shows the supported authentication types and their required option(s):

| Authentication Method | Required Option(s) |
| --- | --- |
| Basic | –username, –password |
| Token | –token |

The tool analyzes the provided options to determine the authentication type and prompt (that is, interactive mode) for the password/token if it is missing. For example, if only `--username` is present, the tool assumes basic authentication and prompts for the password.

For non-interactive mode, provide the `--password` or `--token` option as required or make sure the secret is present in credential storage.

If the operating system’s credential store is not supported, the tool prompts the user for confirmation before writing credentials to the less secure netrc file. Use `--no-confirm` to disable this confirmation.

To force usage of netrc file instead of the operating system’s credential store, pass the `--netrc` flag.

##### Example: basic authentication (macOS, interactive)

```bash
> swift package-registry login https://example-registry.com \
    --username jappleseed
Enter password for 'jappleseed':

Login successful.
Credentials have been saved to the operating system's secure credential store.
```

An entry for `example-registry.com` is added to Keychain.

Package manager updated `registries.json` to indicate that `example-registry.com` requires basic authentication:

{ “authentication”: { “example-registry.com”: { “type”: “basic” }, … }, … }

##### Example: basic authentication (operating system’s credential store not supported, interactive)

```bash
> swift package-registry login https://example-registry.com \
    --username jappleseed
Enter password for 'jappleseed':

Login successful.

WARNING: Secure credential store is not supported on this platform.
Your credentials will be written out to netrc file.
Continue? (Yes/No): Yes

Credentials have been saved to netrc file.
```

An entry for `example-registry.com` is added to the netrc file:

```bash
machine example-registry.com
login jappleseed
password alpine
```

Package manager updates `registries.json` to indicate that example-registry.com requires basic authentication:

```json
{
  "authentication": {
    "example-registry.com": {
      "type": "basic"
    },
    ...
  },
  ...
}
```

##### Example: basic authentication (use netrc file instead of operating system’s credential store, interactive)

```bash
> swift package-registry login https://example-registry.com \
    --username jappleseed
    --netrc
Enter password for 'jappleseed':

Login successful.

WARNING: You choose to use netrc file instead of the operating system's secure credential store. 
Your credentials will be written out to netrc file.
Continue? (Yes/No): Yes

Credentials have been saved to netrc file.
```

An entry for `example-registry.com` is added to the netrc file:

```bash
machine example-registry.com
login jappleseed
password alpine
```

Package manager updates `registries.json` to indicate that `example-registry.com` requires basic authentication:

```json
{
  "authentication": {
    "example-registry.com": {
      "type": "basic"
    },
    ...
  },
  ...
}
```

##### Example: basic authentication (operating system’s credential store not supported, non-interactive)

```bash
> swift package-registry login https://example-registry.com \
    --username jappleseed \
    --password alpine \
    --no-confirm
    
Login successful.
Credentials have been saved to netrc file.
```

An entry for `example-registry.com` is added to the netrc file:

```bash
machine example-registry.com
login jappleseed
password alpine
```

Package manager updates `registries.json` to indicate that `example-registry.com` requires basic authentication:

```json
{
  "authentication": {
    "example-registry.com": {
      "type": "basic"
    },
    ...
  },
  ...
}
```

##### Example: basic authentication (operating system’s credential store not supported, non-interactive, non-default login URL)

```bash
> swift package-registry login https://example-registry.com/api/v1/login \
    --username jappleseed \
    --password alpine \
    --no-confirm
    
Login successful.
Credentials have been saved to netrc file.
```

An entry for `example-registry.com` is added to the netrc file:

```bash
machine example-registry.com
login jappleseed
password alpine
```

Package manager updates `registries.json` to indicate that `example-registry.com` requires basic authentication:

```json
{
  "authentication": {
    "example-registry.com": {
      "type": "basic",
      "loginAPIPath": "/api/v1/login"
    },
    ...
  },
  ...
}
```

##### Example: token authentication

```bash
> swift package-registry login https://example-registry.com \
    --token jappleseedstoken
```

An entry for `example-registry.com` is added to the operating system’s credential store if supported, or the user-level netrc file otherwise:

```bash
machine example-registry.com
login token
password jappleseedstoken
```

Package manager updates `registries.json` to indicate that `example-registry.com` requires token authentication:

```json
{
  "authentication": {
    "example-registry.com": {
      "type": "token"
    },
    ...
  },
  ...
}
```

##### Usage

```
package-registry login [--package-path=<package-path>]
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
  [--disable-local-rpath] [<url>] [--username=<username>]
  [--password=<password>] [--token=<token>]
  [--token-file=<token-file>] [--no-confirm] [--version]
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

- ****url****: 

*The registry URL.*

- ****–username=<username>****: 

*The username for the registry.*

- ****–password=<password>****: 

*The password for the registry.*

- ****–token=<token>****: 

*The access token for the registry.*

- ****–token-file=<token-file>****: 

*Path to the file containing access token.*

- ****–no-confirm****: 

*Allow writing to netrc file without confirmation.*

- ****–version****: 

*Show the version.*

- ****–help****: 

*Show help information.*

## See Also

### Accessing Registries
- [swift package-registry publish](./packageregistrypublish.md)
  Publish to a registry.
- [swift package-registry logout](./packageregistrylogout.md)
  Log out from a registry.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/packageregistrylogin)*