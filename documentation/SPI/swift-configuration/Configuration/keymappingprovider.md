---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider"
framework: "swift-configuration/Configuration"
---

# KeyMappingProvider

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration provider that maps all keys before delegating to an upstream provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct KeyMappingProvider<Upstream> where Upstream : ConfigProvider
```

## Mentions

- [Example use cases](./example-use-cases.md)
- [Migrating to Swift Configuration](./migrating-to-swift-configuration.md)

## Overview

Use `KeyMappingProvider` to automatically apply a mapping function to every configuration key before passing it to an underlying provider. This is particularly useful when the upstream source of configuration keys differs from your own. Another example is namespacing configuration values from specific sources, such as prefixing environment variables with an application name while leaving other configuration sources unchanged.

### Common use cases

Use `KeyMappingProvider` for:

- Rewriting configuration keys to match upstream configuration sources.
- Legacy system integration that adapts existing sources with different naming conventions.

## Example

Use `KeyMappingProvider` when you want to map keys for specific providers in a multi-provider setup:

```swift
// Create providers
let envProvider = EnvironmentVariablesProvider()
let jsonProvider = try await FileProvider<JSONSnapshot>(filePath: "/etc/config.json")

// Only remap the environment variables, not the JSON config
let keyMappedEnvProvider = KeyMappingProvider(upstream: envProvider) { key in
    key.prepending(["myapp", "prod"])
}

let config = ConfigReader(providers: [
    keyMappedEnvProvider, // Reads from "MYAPP_PROD_*" environment variables
    jsonProvider          // Reads from JSON without prefix
])

// This reads from "MYAPP_PROD_DATABASE_HOST" env var or "database.host" in JSON
let host = config.string(forKey: "database.host", default: "localhost")
```

## Convenience method

You can also use the [`prefixKeys(with:)`](./configprovider/prefixkeys%28with%29.md) convenience method on configuration provider types to wrap one in a [`KeyMappingProvider`](./keymappingprovider.md):

```swift
let envProvider = EnvironmentVariablesProvider()
let keyMappedEnvProvider = envProvider.prefixKeys(with: ["myapp", "prod"])
```

## Topics

### Creating a key-mapping provider
- [init(upstream: Upstream, keyMapper: (AbsoluteConfigKey) -> AbsoluteConfigKey)](./keymappingprovider/init%28upstream,keymapper%29.md)
  Creates a new provider.
### Default Implementations
- [ConfigProvider Implementations](./keymappingprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./keymappingprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./keymappingprovider/customstringconvertible-implementations.md)

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
- [struct DirectoryFilesProvider](./directoryfilesprovider.md)
  A configuration provider that reads values from individual files in a directory.
- [Using in-memory providers](./using-in-memory-providers.md)
  Learn about the [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) built-in types.
- [struct InMemoryProvider](./inmemoryprovider.md)
  A configuration provider that stores values in memory.
- [class MutableInMemoryProvider](./mutableinmemoryprovider.md)
  A configuration provider that stores mutable values in memory.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider)*