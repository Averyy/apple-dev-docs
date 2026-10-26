---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader"
framework: "swift-configuration/Configuration"
---

# ConfigSnapshotReader

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A container type for reading config values from snapshots.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfigSnapshotReader
```

#### Overview

A config snapshot reader provides read-only access to config values stored in an underlying [`ConfigSnapshot`](./configsnapshot.md). Unlike a config reader, which can access live, changing config values from providers, a snapshot reader works with a fixed, immutable snapshot of the configuration data.

#### Usage

Get a snapshot reader from a config reader by using the [`snapshot()`](./configreader/snapshot%28%29.md) method. All values in the snapshot are guaranteed to be from the same point in time:

```swift
// Get a snapshot from a ConfigReader
let config = ConfigReader(provider: EnvironmentVariablesProvider())
let snapshot = config.snapshot()
// Use snapshot to read config values
let cert = snapshot.string(forKey: "cert")
let privateKey = snapshot.string(forKey: "privateKey")
// Ensures that both values are coming from the same
// underlying snapshot and that a provider didn't change
// its internal state between the two `string(...)` calls.
let identity = MyIdentity(cert: cert, privateKey: privateKey)
```

Or you can watch for snapshot updates using the [`watchSnapshot(fileID:line:updatesHandler:)`](./configreader/watchsnapshot%28fileid,line,updateshandler%29.md) method:

```swift
try await config.watchSnapshot { snapshots in
    for await snapshot in snapshots {
        // Process each new configuration snapshot
        let cert = snapshot.string(forKey: "cert")
        let privateKey = snapshot.string(forKey: "privateKey")
        // Ensures that both values are coming from the same
        // underlying snapshot and that a provider didn't change
        // its internal state between the two `string(...)` calls.
        let newCert = MyCert(cert: cert, privateKey: privateKey)
        print("Certificate was updated: \(newCert.redactedDescription)")
    }
}
```

##### Scoping

Like `ConfigReader`, you can set a key prefix on the config snapshot reader, allowing all config lookups to prepend a prefix to the keys, which lets you pass a scoped snapshot reader to nested components.

```swift
let httpConfig = snapshotReader.scoped(to: "http")
let timeout = httpConfig.int(forKey: "timeout")
// Reads from "http.timeout" in the snapshot
```

##### Config keys and context

The library requests config values using a canonical “config key”, that represents a key path. You can provide additional context that some providers use when creating the snapshot.

```swift
let httpTimeout = snapshotReader.int(
    forKey: ConfigKey("http.timeout", context: ["upstream": "example.com"]),
    default: 60
)
```

##### Automatic type conversion

String configuration values can be automatically converted to other types using the `as:` parameter. This works with:

- String-backed enum types, as they conform to `RawRepresentable<String>`.
- Types that you explicitly conform to [`ExpressibleByConfigString`](./expressiblebyconfigstring.md).
- Built-in types that already conform to [`ExpressibleByConfigString`](./expressiblebyconfigstring.md):

  - `SystemPackage.FilePath` - Converts from file paths.
  - `Foundation.URL` - Converts from URL strings.
  - `Foundation.UUID` - Converts from UUID strings.
  - `Foundation.Date` - Converts from ISO8601 date strings.

```swift
// Built-in type conversion
let apiUrl = snapshot.string(
    forKey: "api.url",
    as: URL.self
)
let requestId = snapshot.string(
    forKey: "request.id",
    as: UUID.self
)

// Custom enum conversion (RawRepresentable<String>)
enum LogLevel: String {
    case debug, info, warning, error
}
let logLevel = snapshot.string(
    forKey: "logging.level",
    as: LogLevel.self,
    default: .info
)

// Custom type conversion (ExpressibleByConfigString)
struct DatabaseURL: ExpressibleByConfigString {
    let url: URL

    init?(configString: String) {
        guard let url = URL(string: configString) else { return nil }
        self.url = url
    }

    var description: String { url.absoluteString }
}
let dbUrl = snapshot.string(
    forKey: "database.url",
    as: DatabaseURL.self
)
```

##### Access reporting

When reading from a snapshot, access events are reported to the access reporter from the original config reader. This helps debug which config values are accessed, even when reading from snapshots.

## Topics

### Creating a snapshot
- [func snapshot() -> ConfigSnapshotReader](./configreader/snapshot%28%29.md)
  Returns a snapshot of the current configuration state.
- [func watchSnapshot<Return>(fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<ConfigSnapshotReader, Never>) async throws -> Return) async throws -> Return](./configreader/watchsnapshot%28fileid,line,updateshandler%29.md)
  Watches the configuration for changes.
### Namespacing
- [func scoped(to: ConfigKey) -> ConfigSnapshotReader](./configsnapshotreader/scoped%28to%29.md)
  Returns a scoped snapshot reader by appending the provided key to the current key prefix.
### Synchronously reading string values
- [func string(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> String?](./configsnapshotreader/string%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func string(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt) -> String](./configsnapshotreader/string%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configsnapshotreader/string%28forkey,as,issecret,fileid,line%29-8hlcf.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configsnapshotreader/string%28forkey,as,issecret,fileid,line%29-7bpif.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configsnapshotreader/string%28forkey,as,issecret,default,fileid,line%29-fzpe.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configsnapshotreader/string%28forkey,as,issecret,default,fileid,line%29-2mphx.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.
### Synchronously reading lists of string values
- [func stringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [String]?](./configsnapshotreader/stringarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configsnapshotreader/stringarray%28forkey,as,issecret,fileid,line%29-7athn.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configsnapshotreader/stringarray%28forkey,as,issecret,fileid,line%29-v5ap.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt) -> [String]](./configsnapshotreader/stringarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configsnapshotreader/stringarray%28forkey,as,issecret,default,fileid,line%29-8n896.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from strings.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configsnapshotreader/stringarray%28forkey,as,issecret,default,fileid,line%29-yx0h.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from strings.
### Synchronously reading required string values
- [func requiredString(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> String](./configsnapshotreader/requiredstring%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configsnapshotreader/requiredstring%28forkey,as,issecret,fileid,line%29-85qdd.md)
  Synchronously gets a required config value for the given config key, converting from string.
- [func requiredString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configsnapshotreader/requiredstring%28forkey,as,issecret,fileid,line%29-3iy7q.md)
  Synchronously gets a required config value for the given config key, converting from string.
### Synchronously reading required lists of string values
- [func requiredStringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [String]](./configsnapshotreader/requiredstringarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configsnapshotreader/requiredstringarray%28forkey,as,issecret,fileid,line%29-4nuew.md)
  Synchronously gets a required array of config values for the given config key, converting from strings.
- [func requiredStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configsnapshotreader/requiredstringarray%28forkey,as,issecret,fileid,line%29-4pyhg.md)
  Synchronously gets a required array of config values for the given config key, converting from strings.
### Synchronously reading Boolean values
- [func bool(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Bool?](./configsnapshotreader/bool%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func bool(forKey: ConfigKey, isSecret: Bool, default: Bool, fileID: String, line: UInt) -> Bool](./configsnapshotreader/bool%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required Boolean values
- [func requiredBool(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> Bool](./configsnapshotreader/requiredbool%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading lists of Boolean values
- [func boolArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Bool]?](./configsnapshotreader/boolarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func boolArray(forKey: ConfigKey, isSecret: Bool, default: [Bool], fileID: String, line: UInt) -> [Bool]](./configsnapshotreader/boolarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required lists of Boolean values
- [func requiredBoolArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [Bool]](./configsnapshotreader/requiredboolarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading integer values
- [func int(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Int?](./configsnapshotreader/int%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func int(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt) -> Int](./configsnapshotreader/int%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configsnapshotreader/int%28forkey,as,issecret,fileid,line%29-3edsa.md)
  Synchronously gets a config value for the given config key, converting from integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configsnapshotreader/int%28forkey,as,issecret,fileid,line%29-1l91m.md)
  Synchronously gets a config value for the given config key, converting from integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configsnapshotreader/int%28forkey,as,issecret,default,fileid,line%29-8oo8c.md)
  Synchronously gets a config value for the given config key with default fallback, converting from integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configsnapshotreader/int%28forkey,as,issecret,default,fileid,line%29-3a0gv.md)
  Synchronously gets a config value for the given config key with default fallback, converting from integer.
### Synchronously reading required integer values
- [func requiredInt(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> Int](./configsnapshotreader/requiredint%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configsnapshotreader/requiredint%28forkey,as,issecret,fileid,line%29-4jh1t.md)
  Synchronously gets a required config value for the given config key, converting from integer.
- [func requiredInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configsnapshotreader/requiredint%28forkey,as,issecret,fileid,line%29-x6dx.md)
  Synchronously gets a required config value for the given config key, converting from integer.
### Synchronously reading lists of integer values
- [func intArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Int]?](./configsnapshotreader/intarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func intArray(forKey: ConfigKey, isSecret: Bool, default: [Int], fileID: String, line: UInt) -> [Int]](./configsnapshotreader/intarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configsnapshotreader/intarray%28forkey,as,issecret,fileid,line%29-5dw7j.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configsnapshotreader/intarray%28forkey,as,issecret,fileid,line%29-8nwxy.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configsnapshotreader/intarray%28forkey,as,issecret,default,fileid,line%29-85dpy.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configsnapshotreader/intarray%28forkey,as,issecret,default,fileid,line%29-4u516.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from integers.
### Synchronously reading required lists of integer values
- [func requiredIntArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [Int]](./configsnapshotreader/requiredintarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configsnapshotreader/requiredintarray%28forkey,as,issecret,fileid,line%29-82bhm.md)
  Synchronously gets a required array of config values for the given config key, converting from integers.
- [func requiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configsnapshotreader/requiredintarray%28forkey,as,issecret,fileid,line%29-1c4qk.md)
  Synchronously gets a required array of config values for the given config key, converting from integers.
### Synchronously reading double values
- [func double(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Double?](./configsnapshotreader/double%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func double(forKey: ConfigKey, isSecret: Bool, default: Double, fileID: String, line: UInt) -> Double](./configsnapshotreader/double%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required double values
- [func requiredDouble(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> Double](./configsnapshotreader/requireddouble%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading lists of double values
- [func doubleArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Double]?](./configsnapshotreader/doublearray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func doubleArray(forKey: ConfigKey, isSecret: Bool, default: [Double], fileID: String, line: UInt) -> [Double]](./configsnapshotreader/doublearray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required lists of double values
- [func requiredDoubleArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [Double]](./configsnapshotreader/requireddoublearray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading bytes
- [func bytes(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [UInt8]?](./configsnapshotreader/bytes%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func bytes(forKey: ConfigKey, isSecret: Bool, default: [UInt8], fileID: String, line: UInt) -> [UInt8]](./configsnapshotreader/bytes%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required bytes
- [func requiredBytes(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [UInt8]](./configsnapshotreader/requiredbytes%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading collections of byte chunks
- [func byteChunkArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [[UInt8]]?](./configsnapshotreader/bytechunkarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func byteChunkArray(forKey: ConfigKey, isSecret: Bool, default: [[UInt8]], fileID: String, line: UInt) -> [[UInt8]]](./configsnapshotreader/bytechunkarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required collections of byte chunks
- [func requiredByteChunkArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [[UInt8]]](./configsnapshotreader/requiredbytechunkarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Default Implementations
- [CustomStringConvertible Implementations](./configsnapshotreader/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Readers and providers
- [struct ConfigReader](./configreader.md)
  A type that provides read-only access to configuration values from underlying providers.
- [protocol ConfigProvider](./configprovider.md)
  A type that provides configuration values from a data source.
- [Choosing the access pattern](./choosing-access-patterns.md)
  Learn how to select the right method for reading configuration values based on your needs.
- [Choosing reader methods](./choosing-reader-methods.md)
  Choose between optional, default, and required variants of configuration methods.
- [Handling secrets correctly](./handling-secrets-correctly.md)
  Protect sensitive configuration values from accidental disclosure in logs and debug output.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshotreader)*