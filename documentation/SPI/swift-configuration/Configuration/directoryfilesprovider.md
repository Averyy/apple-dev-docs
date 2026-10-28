---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/directoryfilesprovider"
framework: "swift-configuration/Configuration"
---

# DirectoryFilesProvider

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration provider that reads values from individual files in a directory.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct DirectoryFilesProvider
```

## Mentions

- [Example use cases](./example-use-cases.md)
- [Handling secrets correctly](./handling-secrets-correctly.md)
- [Migrating to Swift Configuration](./migrating-to-swift-configuration.md)
- [Troubleshooting and access reporting](./troubleshooting.md)

## Overview

This provider reads configuration values from a directory where each file represents a single configuration key-value pair. The file name becomes the configuration key, and the file contents become the value. This approach is commonly used by secret management systems that mount secrets as individual files.

## Key mapping

This provider transforms configuration keys into file names using these rules:

- Joins components with dashes.
- Replaces non-alphanumeric characters (except dashes) with underscores.

For example:

- `database.password` -> `database-password`

## Value handling

The provider reads file contents as UTF-8 strings and converts them to the requested type. For binary data (bytes type), it reads raw file contents directly without string conversion. The provider always trims leading and trailing whitespace from string values.

## Supported data types

The provider supports all standard configuration types:

- Strings (UTF-8 text files)
- Integers, doubles, and booleans (parsed from string contents)
- Arrays (using configurable separator, comma by default)
- Byte arrays (raw file contents)

## Secret handling

By default, all values are marked as secrets for security. This is appropriate since this provider is typically used for sensitive data mounted by secret management systems.

## Usage

### Reading from a secrets directory

```swift
// Assuming /run/secrets contains files:
// - database-password (contains: "secretpass123")
// - max-connections (contains: "100")
// - enable-cache (contains: "true")

let provider = try await DirectoryFilesProvider(
    directoryPath: "/run/secrets"
)

let config = ConfigReader(provider: provider)
let dbPassword = config.string(forKey: "database.password")  // "secretpass123"
let maxConn = config.int(forKey: "max.connections", default: 50)  // 100
let cacheEnabled = config.bool(forKey: "enable.cache", default: false)  // true
```

### Reading binary data

```swift
// For binary files like certificates or keys
let provider = try await DirectoryFilesProvider(
    directoryPath: "/run/secrets"
)

let config = ConfigReader(provider: provider)
let certData = try config.requiredBytes(forKey: "tls.cert")  // Raw file bytes
```

### Custom array handling

```swift
// If files contain comma-separated lists
let provider = try await DirectoryFilesProvider(
    directoryPath: "/etc/config"
)

// File "allowed-hosts" contains: "host1.example.com,host2.example.com,host3.example.com"
let hosts = config.stringArray(forKey: "allowed.hosts", default: [])
// ["host1.example.com", "host2.example.com", "host3.example.com"]
```

## Configuration context

This provider ignores the context passed in [`context`](./absoluteconfigkey/context.md). All keys are resolved using only their component path.

## Topics

### Creating a directory files provider
- [init(directoryPath: FilePath, allowMissing: Bool, secretsSpecifier: SecretsSpecifier<String, Data>, arraySeparator: Character) async throws](./directoryfilesprovider/init%28directorypath,allowmissing,secretsspecifier,arrayseparator%29.md)
  Creates a new provider that reads files from a directory.
### Default Implementations
- [ConfigProvider Implementations](./directoryfilesprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./directoryfilesprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./directoryfilesprovider/customstringconvertible-implementations.md)

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
- [struct EnvironmentVariablesProvider](./environmentvariablesprovider.md)
  A configuration provider that reads values from environment variables.
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
- [Using in-memory providers](./using-in-memory-providers.md)
  Learn about the [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) built-in types.
- [struct InMemoryProvider](./inmemoryprovider.md)
  A configuration provider that stores values in memory.
- [class MutableInMemoryProvider](./mutableinmemoryprovider.md)
  A configuration provider that stores mutable values in memory.
- [struct KeyMappingProvider](./keymappingprovider.md)
  A configuration provider that maps all keys before delegating to an upstream provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/directoryfilesprovider)*