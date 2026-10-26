---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader-fetch"
framework: "swift-configuration/Configuration"
---

# Asynchronously fetching values

**Framework**: swift-configuration/Configuration  
**Role**: API Collection

## Topics

### Asynchronously fetching string values
- [func fetchString(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> String?](./configreader/fetchstring%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchString(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt) async throws -> String](./configreader/fetchstring%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./configreader/fetchstring%28forkey,as,issecret,fileid,line%29-6m5tu.md)
  Asynchronously fetches a config value for the given config key, converting from string.
- [func fetchString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./configreader/fetchstring%28forkey,as,issecret,fileid,line%29-2zxxs.md)
  Asynchronously fetches a config value for the given config key, converting from string.
- [func fetchString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) async throws -> Value](./configreader/fetchstring%28forkey,as,issecret,default,fileid,line%29-9vhmw.md)
  Asynchronously fetches a config value for the given config key with default fallback, converting from string.
- [func fetchString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) async throws -> Value](./configreader/fetchstring%28forkey,as,issecret,default,fileid,line%29-7hxpy.md)
  Asynchronously fetches a config value for the given config key with default fallback, converting from string.
### Asynchronously fetching lists of string values
- [func fetchStringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [String]?](./configreader/fetchstringarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./configreader/fetchstringarray%28forkey,as,issecret,fileid,line%29-4yv3p.md)
  Asynchronously fetches an array of config values for the given config key, converting from strings.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./configreader/fetchstringarray%28forkey,as,issecret,fileid,line%29-4nmik.md)
  Asynchronously fetches an array of config values for the given config key, converting from strings.
- [func fetchStringArray(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt) async throws -> [String]](./configreader/fetchstringarray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchstringarray%28forkey,as,issecret,default,fileid,line%29-1fcex.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from strings.
- [func fetchStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchstringarray%28forkey,as,issecret,default,fileid,line%29-3te90.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from strings.
### Asynchronously fetching required string values
- [func fetchRequiredString(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> String](./configreader/fetchrequiredstring%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
- [func fetchRequiredString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value](./configreader/fetchrequiredstring%28forkey,as,issecret,fileid,line%29-79md3.md)
  Asynchronously fetches a required config value for the given config key, converting from string.
- [func fetchRequiredString<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value](./configreader/fetchrequiredstring%28forkey,as,issecret,fileid,line%29-e16l.md)
  Asynchronously fetches a required config value for the given config key, converting from string.
### Asynchronously fetching required lists of string values
- [func fetchRequiredStringArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [String]](./configreader/fetchrequiredstringarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
- [func fetchRequiredStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchrequiredstringarray%28forkey,as,issecret,fileid,line%29-6es6t.md)
  Asynchronously fetches a required array of config values for the given config key, converting from strings.
- [func fetchRequiredStringArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchrequiredstringarray%28forkey,as,issecret,fileid,line%29-1bf0t.md)
  Asynchronously fetches a required array of config values for the given config key, converting from strings.
### Asynchronously fetching Boolean values
- [func fetchBool(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> Bool?](./configreader/fetchbool%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchBool(forKey: ConfigKey, isSecret: Bool, default: Bool, fileID: String, line: UInt) async throws -> Bool](./configreader/fetchbool%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
### Asynchronously fetching required Boolean values
- [func fetchRequiredBool(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> Bool](./configreader/fetchrequiredbool%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
### Asynchronously fetching lists of Boolean values
- [func fetchBoolArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Bool]?](./configreader/fetchboolarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchBoolArray(forKey: ConfigKey, isSecret: Bool, default: [Bool], fileID: String, line: UInt) async throws -> [Bool]](./configreader/fetchboolarray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
### Asynchronously fetching required lists of Boolean values
- [func fetchRequiredBoolArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Bool]](./configreader/fetchrequiredboolarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
### Asynchronously fetching integer values
- [func fetchInt(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> Int?](./configreader/fetchint%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchInt(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt) async throws -> Int](./configreader/fetchint%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./configreader/fetchint%28forkey,as,issecret,fileid,line%29-107qe.md)
  Asynchronously fetches a config value for the given config key, converting from an integer.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value?](./configreader/fetchint%28forkey,as,issecret,fileid,line%29-6tdet.md)
  Asynchronously fetches a config value for the given config key, converting from an integer.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) async throws -> Value](./configreader/fetchint%28forkey,as,issecret,default,fileid,line%29-3161u.md)
  Asynchronously fetches a config value for the given config key with default fallback, converting from an integer.
- [func fetchInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt) async throws -> Value](./configreader/fetchint%28forkey,as,issecret,default,fileid,line%29-41vzw.md)
  Asynchronously fetches a config value for the given config key with default fallback, converting from an integer.
### Asynchronously fetching required integer values
- [func fetchRequiredInt(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> Int](./configreader/fetchrequiredint%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
- [func fetchRequiredInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value](./configreader/fetchrequiredint%28forkey,as,issecret,fileid,line%29-12gf.md)
  Asynchronously fetches a required config value for the given config key, converting from an integer.
- [func fetchRequiredInt<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> Value](./configreader/fetchrequiredint%28forkey,as,issecret,fileid,line%29-8b0sw.md)
  Asynchronously fetches a required config value for the given config key, converting from an integer.
### Asynchronously fetching lists of integer values
- [func fetchIntArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Int]?](./configreader/fetchintarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchIntArray(forKey: ConfigKey, isSecret: Bool, default: [Int], fileID: String, line: UInt) async throws -> [Int]](./configreader/fetchintarray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
- [func fetchIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./configreader/fetchintarray%28forkey,as,issecret,fileid,line%29-16vlr.md)
  Asynchronously fetches an array of config values for the given config key, converting from integers.
- [func fetchIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]?](./configreader/fetchintarray%28forkey,as,issecret,fileid,line%29-6rhh4.md)
  Asynchronously fetches an array of config values for the given config key, converting from integers.
- [func fetchIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchintarray%28forkey,as,issecret,default,fileid,line%29-79l2m.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from integers.
- [func fetchIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchintarray%28forkey,as,issecret,default,fileid,line%29-8ldio.md)
  Asynchronously fetches an array of config values for the given config key with default fallback, converting from integers.
### Asynchronously fetching required lists of integer values
- [func fetchRequiredIntArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Int]](./configreader/fetchrequiredintarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
- [func fetchRequiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchrequiredintarray%28forkey,as,issecret,fileid,line%29-6a1e3.md)
  Asynchronously fetches a required array of config values for the given config key, converting from integers.
- [func fetchRequiredIntArray<Value>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt) async throws -> [Value]](./configreader/fetchrequiredintarray%28forkey,as,issecret,fileid,line%29-599c5.md)
  Asynchronously fetches a required array of config values for the given config key, converting from integers.
### Asynchronously fetching double values
- [func fetchDouble(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> Double?](./configreader/fetchdouble%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchDouble(forKey: ConfigKey, isSecret: Bool, default: Double, fileID: String, line: UInt) async throws -> Double](./configreader/fetchdouble%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
### Asynchronously fetching required double values
- [func fetchRequiredDouble(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> Double](./configreader/fetchrequireddouble%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
### Asynchronously fetching lists of double values
- [func fetchDoubleArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Double]?](./configreader/fetchdoublearray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchDoubleArray(forKey: ConfigKey, isSecret: Bool, default: [Double], fileID: String, line: UInt) async throws -> [Double]](./configreader/fetchdoublearray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
### Asynchronously fetching required lists of double values
- [func fetchRequiredDoubleArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [Double]](./configreader/fetchrequireddoublearray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
### Asynchronously fetching bytes
- [func fetchBytes(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [UInt8]?](./configreader/fetchbytes%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchBytes(forKey: ConfigKey, isSecret: Bool, default: [UInt8], fileID: String, line: UInt) async throws -> [UInt8]](./configreader/fetchbytes%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
### Asynchronously fetching required bytes
- [func fetchRequiredBytes(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [UInt8]](./configreader/fetchrequiredbytes%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.
### Asynchronously fetching lists of byte chunks
- [func fetchByteChunkArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [[UInt8]]?](./configreader/fetchbytechunkarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key.
- [func fetchByteChunkArray(forKey: ConfigKey, isSecret: Bool, default: [[UInt8]], fileID: String, line: UInt) async throws -> [[UInt8]]](./configreader/fetchbytechunkarray%28forkey,issecret,default,fileid,line%29.md)
  Asynchronously fetches a config value for the given config key, with a default fallback.
### Asynchronously fetching required lists of byte chunks
- [func fetchRequiredByteChunkArray(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt) async throws -> [[UInt8]]](./configreader/fetchrequiredbytechunkarray%28forkey,issecret,fileid,line%29.md)
  Asynchronously fetches a required config value for the given config key, throwing an error if it’s missing.

## See Also

### Reading from a snapshot
- [func snapshot() -> ConfigSnapshotReader](./configreader/snapshot%28%29.md)
  Returns a snapshot of the current configuration state.
- [func watchSnapshot<Return>(fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<ConfigSnapshotReader, Never>) async throws -> Return) async throws -> Return](./configreader/watchsnapshot%28fileid,line,updateshandler%29.md)
  Watches the configuration for changes.
- [Synchronously reading values](./configreader-get.md)
- [Watching values](./configreader-watch.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader-fetch)*