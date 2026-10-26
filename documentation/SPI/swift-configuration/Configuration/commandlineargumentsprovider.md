---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/commandlineargumentsprovider"
framework: "swift-configuration/Configuration"
---

# CommandLineArgumentsProvider

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration provider that sources values from command-line arguments.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct CommandLineArgumentsProvider
```

## Mentions

- [Integrating with Swift Argument Parser](./integrating-with-swift-argument-parser.md)

#### Overview

Reads configuration values from CLI arguments with type conversion and secrets handling. Keys are encoded to CLI flags at lookup time.

#### Package traits

This type is guarded by the `CommandLineArguments` package trait.

#### Key formats

- `--key value` - A key-value pair with separate arguments.
- `--key=value` - A key-value pair with an equals sign.
- `--flag` - A Boolean flag, treated as `true`.
- `--key val1 val2` - Multiple values (arrays).

Configuration keys are transformed to CLI flags: `["http", "serverTimeout"]` → `--http-server-timeout`.

#### Array handling

Arrays can be specified in multiple ways:

- **Space-separated**: `--tags swift configuration cli`
- **Repeated flags**: `--tags swift --tags configuration --tags cli`
- **Comma-separated**: `--tags swift,configuration,cli`
- **Mixed**: `--tags swift,configuration --tags cli`

All formats produce the same result when accessed as an array type.

#### Usage

```swift
// CLI: program --debug --host localhost --ports 8080 8443
let provider = CommandLineArgumentsProvider()
let config = ConfigReader(provider: provider)

let isDebug = config.bool(forKey: "debug", default: false) // true
let host = config.string(forKey: "host", default: "0.0.0.0") // "localhost"
let ports = config.intArray(forKey: "ports", default: []) // [8080, 8443]
```

##### With secrets

```swift
let provider = CommandLineArgumentsProvider(
    secretsSpecifier: .specific(["--api-key"])
)
```

##### Custom arguments

```swift
let provider = CommandLineArgumentsProvider(
    arguments: ["program", "--verbose", "--timeout", "30"],
    secretsSpecifier: .dynamic { key, _ in key.contains("--secret") }
)
```

#### Using with Swift Argument Parser

This provider doesn’t support subcommands, positional arguments, or generated help. To combine it with Swift Argument Parser, check out [Integrating with Swift Argument Parser](./integrating-with-swift-argument-parser.md).

## Topics

### Creating a command line arguments provider
- [init(arguments: [String], secretsSpecifier: SecretsSpecifier<String, String>, bytesDecoder: some ConfigBytesFromStringDecoder)](./commandlineargumentsprovider/init%28arguments,secretsspecifier,bytesdecoder%29.md)
  Creates a new CLI provider with the provided arguments.
### Default Implementations
- [ConfigProvider Implementations](./commandlineargumentsprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./commandlineargumentsprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./commandlineargumentsprovider/customstringconvertible-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/commandlineargumentsprovider)*