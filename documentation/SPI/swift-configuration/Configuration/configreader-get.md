---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader-get"
framework: "swift-configuration/Configuration"
---

# Synchronously reading values

**Framework**: swift-configuration/Configuration  
**Role**: API Collection

## Topics

### Synchronously reading string values
- [func string(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> String?](./configreader/string%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func string(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt) -> String](./configreader/string%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configreader/string%28forkey,as,issecret,fileid,line%29-1syvw.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configreader/string%28forkey,as,issecret,fileid,line%29-4oust.md)
  Synchronously gets a config value for the given config key, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configreader/string%28forkey,as,issecret,default,fileid,line%29-9xr3c.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.
- [func string<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configreader/string%28forkey,as,issecret,default,fileid,line%29-1sqv7.md)
  Synchronously gets a config value for the given config key with default fallback, converting from string.
### Synchronously reading lists of string values
- [func stringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [String]?](./configreader/stringarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configreader/stringarray%28forkey,as,issecret,fileid,line%29-2oujn.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configreader/stringarray%28forkey,as,issecret,fileid,line%29-90bg2.md)
  Synchronously gets an array of config values for the given config key, converting from strings.
- [func stringArray(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt) -> [String]](./configreader/stringarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configreader/stringarray%28forkey,as,issecret,default,fileid,line%29-7tit4.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from strings.
- [func stringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configreader/stringarray%28forkey,as,issecret,default,fileid,line%29-139vb.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from strings.
### Synchronously reading required string values
- [func requiredString(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> String](./configreader/requiredstring%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configreader/requiredstring%28forkey,as,issecret,fileid,line%29-2fljl.md)
  Synchronously gets a required config value for the given config key, converting from string.
- [func requiredString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configreader/requiredstring%28forkey,as,issecret,fileid,line%29-15z38.md)
  Synchronously gets a required config value for the given config key, converting from string.
### Synchronously reading required lists of string values
- [func requiredStringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [String]](./configreader/requiredstringarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configreader/requiredstringarray%28forkey,as,issecret,fileid,line%29-97pcp.md)
  Synchronously gets a required array of config values for the given config key, converting from strings.
- [func requiredStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configreader/requiredstringarray%28forkey,as,issecret,fileid,line%29-pxel.md)
  Synchronously gets a required array of config values for the given config key, converting from strings.
### Synchronously reading Boolean values
- [func bool(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Bool?](./configreader/bool%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func bool(forKey: ConfigKey, isSecret: Bool, default: Bool, fileID: String, line: UInt) -> Bool](./configreader/bool%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required Boolean values
- [func requiredBool(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> Bool](./configreader/requiredbool%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading lists of Boolean values
- [func boolArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Bool]?](./configreader/boolarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func boolArray(forKey: ConfigKey, isSecret: Bool, default: [Bool], fileID: String, line: UInt) -> [Bool]](./configreader/boolarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required lists of Boolean values
- [func requiredBoolArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [Bool]](./configreader/requiredboolarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading integer values
- [func int(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Int?](./configreader/int%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func int(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt) -> Int](./configreader/int%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configreader/int%28forkey,as,issecret,fileid,line%29-6ng32.md)
  Synchronously gets a config value for the given config key, converting from an integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> Value?](./configreader/int%28forkey,as,issecret,fileid,line%29-11fn2.md)
  Synchronously gets a config value for the given config key, converting from an integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configreader/int%28forkey,as,issecret,default,fileid,line%29-4zrhi.md)
  Synchronously gets a config value for the given config key with default fallback, converting from an integer.
- [func int<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) -> Value](./configreader/int%28forkey,as,issecret,default,fileid,line%29-4ie6l.md)
  Synchronously gets a config value for the given config key with default fallback, converting from an integer.
### Synchronously reading required integer values
- [func requiredInt(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> Int](./configreader/requiredint%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configreader/requiredint%28forkey,as,issecret,fileid,line%29-3dzjk.md)
  Synchronously gets a required config value for the given config key, converting from an integer.
- [func requiredInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> Value](./configreader/requiredint%28forkey,as,issecret,fileid,line%29-2xiji.md)
  Synchronously gets a required config value for the given config key, converting from an integer.
### Synchronously reading lists of integer values
- [func intArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Int]?](./configreader/intarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func intArray(forKey: ConfigKey, isSecret: Bool, default: [Int], fileID: String, line: UInt) -> [Int]](./configreader/intarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configreader/intarray%28forkey,as,issecret,fileid,line%29-3goaq.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) -> [Value]?](./configreader/intarray%28forkey,as,issecret,fileid,line%29-9sp0s.md)
  Synchronously gets an array of config values for the given config key, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configreader/intarray%28forkey,as,issecret,default,fileid,line%29-9ini5.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from integers.
- [func intArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) -> [Value]](./configreader/intarray%28forkey,as,issecret,default,fileid,line%29-1so32.md)
  Synchronously gets an array of config values for the given config key with default fallback, converting from integers.
### Synchronously reading required lists of integer values
- [func requiredIntArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [Int]](./configreader/requiredintarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
- [func requiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configreader/requiredintarray%28forkey,as,issecret,fileid,line%29-cyh0.md)
  Synchronously gets a required array of config values for the given config key, converting from integers.
- [func requiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) throws -> [Value]](./configreader/requiredintarray%28forkey,as,issecret,fileid,line%29-1car4.md)
  Synchronously gets a required array of config values for the given config key, converting from integers.
### Synchronously reading double values
- [func double(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> Double?](./configreader/double%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func double(forKey: ConfigKey, isSecret: Bool, default: Double, fileID: String, line: UInt) -> Double](./configreader/double%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required double values
- [func requiredDouble(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> Double](./configreader/requireddouble%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading lists of double values
- [func doubleArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [Double]?](./configreader/doublearray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func doubleArray(forKey: ConfigKey, isSecret: Bool, default: [Double], fileID: String, line: UInt) -> [Double]](./configreader/doublearray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required lists of double values
- [func requiredDoubleArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [Double]](./configreader/requireddoublearray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading bytes
- [func bytes(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [UInt8]?](./configreader/bytes%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func bytes(forKey: ConfigKey, isSecret: Bool, default: [UInt8], fileID: String, line: UInt) -> [UInt8]](./configreader/bytes%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required bytes
- [func requiredBytes(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [UInt8]](./configreader/requiredbytes%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.
### Synchronously reading collections of byte chunks
- [func byteChunkArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) -> [[UInt8]]?](./configreader/bytechunkarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a config value for the given config key.
- [func byteChunkArray(forKey: ConfigKey, isSecret: Bool, default: [[UInt8]], fileID: String, line: UInt) -> [[UInt8]]](./configreader/bytechunkarray%28forkey,issecret,default,fileid,line%29.md)
  Synchronously gets a config value for the given config key, with a default fallback.
### Synchronously reading required collections of byte chunks
- [func requiredByteChunkArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) throws -> [[UInt8]]](./configreader/requiredbytechunkarray%28forkey,issecret,fileid,line%29.md)
  Synchronously gets a required config value for the given config key, throwing an error if it’s missing.

## See Also

### Reading from a snapshot
- [func snapshot() -> ConfigSnapshotReader](./configreader/snapshot%28%29.md)
  Returns a snapshot of the current configuration state.
- [func watchSnapshot<Return>(fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<ConfigSnapshotReader, Never>) async throws -> Return) async throws -> Return](./configreader/watchsnapshot%28fileid,line,updateshandler%29.md)
  Watches the configuration for changes.
- [Asynchronously fetching values](./configreader-fetch.md)
- [Watching values](./configreader-watch.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader-get)*