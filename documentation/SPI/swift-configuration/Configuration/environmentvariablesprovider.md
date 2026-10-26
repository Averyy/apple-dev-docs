---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider"
framework: "swift-configuration/Configuration"
---

# EnvironmentVariablesProvider

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration provider that reads values from environment variables.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct EnvironmentVariablesProvider
```

## Mentions

- [Troubleshooting and access reporting](./troubleshooting.md)
- [Configuring applications](./configuring-applications.md)
- [Example use cases](./example-use-cases.md)
- [Migrating to Swift Configuration](./migrating-to-swift-configuration.md)

#### Overview

This provider reads configuration values from environment variables, supporting both the current process environment and `.env` files. It automatically converts hierarchical configuration keys into standard environment variable naming conventions and handles type conversion for all supported configuration value types.

#### Key transformation

This provider transforms configuration keys into environment variable names using these rules:

- Joins components with underscores.
- Converts all characters to uppercase.
- Detects CamelCase and marks word boundaries with underscores.
- Replaces non-alphanumeric characters with underscores.

For example: `http.serverTimeout` becomes `HTTP_SERVER_TIMEOUT`

#### Supported data types

The provider supports all standard configuration types:

- Strings, integers, doubles, and booleans
- Arrays of strings, integers, doubles, and booleans (comma-separated by default)
- Byte arrays (base64-encoded by default)
- Arrays of byte chunks

#### Secret handling

You can mark environment variables as secrets using a [`SecretsSpecifier`](./secretsspecifier.md). The provider automatically redacts secret values in debug output and logging.

> ❗ **Important**: This provider performs case-insensitive lookup of environment variable names.

#### Usage

##### Reading environment variables in the current process

```swift
// Assuming the environment contains the following variables:
// HTTP_CLIENT_USER_AGENT=Config/1.0 (Test)
// HTTP_CLIENT_TIMEOUT=15.0
// HTTP_SECRET=s3cret
// HTTP_VERSION=2
// ENABLED=true

let provider = EnvironmentVariablesProvider(
    secretsSpecifier: .specific(["HTTP_SECRET"])
)
// Prints all values, redacts "HTTP_SECRET" automatically.
print(provider)
let config = ConfigReader(provider: provider)
let isEnabled = config.bool(forKey: "enabled", default: false)
let userAgent = config.string(forKey: "http.client.user-agent", default: "unspecified")
// ...
```

##### Reading environment variables from a `.env`-style file

```swift
// Assuming the local file system has a file called `.env` in the current working directory
// with the following contents:
//
//    HTTP_CLIENT_USER_AGENT=Config/1.0 (Test)
//    HTTP_CLIENT_TIMEOUT=15.0
//    HTTP_SECRET=s3cret
//    HTTP_VERSION=2
//    ENABLED=true

let provider = try await EnvironmentVariablesProvider(
    environmentFilePath: ".env",
    secretsSpecifier: .specific(["HTTP_SECRET"])
)
// Prints all values, redacts "HTTP_SECRET" automatically.
print(provider)
let config = ConfigReader(provider: provider)
let isEnabled = config.bool(forKey: "enabled", default: false)
let userAgent = config.string(forKey: "http.client.user-agent", default: "unspecified")
// ...
```

##### Config context

The environment variables provider ignores the context passed in [`context`](./absoluteconfigkey/context.md).

## Topics

### Creating an environment variable provider
- [init(secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character)](./environmentvariablesprovider/init%28secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider that reads from the current process environment.
- [init(environmentVariables: [String : String], secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character)](./environmentvariablesprovider/init%28environmentvariables,secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider from a custom dictionary of environment variables.
- [init(environmentFilePath: FilePath, allowMissing: Bool, secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder, arraySeparator: Character) async throws](./environmentvariablesprovider/init%28environmentfilepath,allowmissing,secretsspecifier,bytesdecoder,arrayseparator%29.md)
  Creates a new provider that reads from an environment file.
### Inspecting an environment variable provider
- [func environmentValue(forName: String) throws -> String?](./environmentvariablesprovider/environmentvalue%28forname%29.md)
  Returns the raw string value for a specific environment variable name.
### Default Implementations
- [ConfigProvider Implementations](./environmentvariablesprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./environmentvariablesprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./environmentvariablesprovider/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [ConfigProvider](./configprovider.md)
- Swift.Copyable
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Built-in providers
- [struct CommandLineArgumentsProvider](./commandlineargumentsprovider.md)
  A configuration provider that sources values from command-line arguments.
- [Integrating with Swift Argument Parser](./integrating-with-swift-argument-parser.md)
  Combine the commands and options of Swift Argument Parser with the provider hierarchy of Swift Configuration.
- [struct FileProvider](./fileprovider.md)
  A configuration provider that reads from a file on disk using a configurable snapshot type.
- [class ReloadingFileProvider](./reloadingfileprovider.md)
  A configuration provider that reads configuration from a file on disk with automatic reloading capability.
- [struct JSONSnapshot](./jsonsnapshot.md)
  A snapshot of configuration values parsed from JSON data.
- [class YAMLSnapshot](./yamlsnapshot.md)
  A snapshot of configuration values parsed from YAML data.
- [struct PropertyListSnapshot](./propertylistsnapshot.md)
  A snapshot of configuration values parsed from property list (plist) data.
- [Using reloading providers](./using-reloading-providers.md)
  Automatically reload configuration from files when they change.
- [struct DirectoryFilesProvider](./directoryfilesprovider.md)
  A configuration provider that reads values from individual files in a directory.
- [Using in-memory providers](./using-in-memory-providers.md)
  Learn about the [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) built-in types.
- [struct InMemoryProvider](./inmemoryprovider.md)
  A configuration provider that stores values in memory.
- [class MutableInMemoryProvider](./mutableinmemoryprovider.md)
  A configuration provider that stores mutable values in memory.
- [struct KeyMappingProvider](./keymappingprovider.md)
  A configuration provider that maps all keys before delegating to an upstream provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/environmentvariablesprovider)*