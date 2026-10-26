---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader-watch"
framework: "swift-configuration/Configuration"
---

# Watching values

**Framework**: swift-configuration/Configuration  
**Role**: API Collection

## Topics

### Watching string values
- [func watchString<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String?, Never>) async throws -> Return) async throws -> Return](./configreader/watchstring%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./configreader/watchstring%28forkey,as,issecret,fileid,line,updateshandler%29-4zs5y.md)
  Watches for updates to a config value for the given config key, converting from string.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./configreader/watchstring%28forkey,as,issecret,fileid,line,updateshandler%29-8hegv.md)
  Watches for updates to a config value for the given config key, converting from string.
- [func watchString<Return>(forKey: ConfigKey, isSecret: Bool, default: String, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String, Never>) async throws -> Return) async throws -> Return](./configreader/watchstring%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./configreader/watchstring%28forkey,as,issecret,default,fileid,line,updateshandler%29-hi1l.md)
  Watches for updates to a config value for the given config key with default fallback, converting from string.
- [func watchString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./configreader/watchstring%28forkey,as,issecret,default,fileid,line,updateshandler%29-9qsww.md)
  Watches for updates to a config value for the given config key with default fallback, converting from string.
### Watching required string values
- [func watchRequiredString<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<String, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredstring%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
- [func watchRequiredString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredstring%28forkey,as,issecret,fileid,line,updateshandler%29-581rg.md)
  Watches for updates to a required config value for the given config key, converting from string.
- [func watchRequiredString<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredstring%28forkey,as,issecret,fileid,line,updateshandler%29-13z9o.md)
  Watches for updates to a required config value for the given config key, converting from string.
### Watching lists of string values
- [func watchStringArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[String]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchstringarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchstringarray%28forkey,as,issecret,fileid,line,updateshandler%29-15oye.md)
  Watches for updates to an array of config values for the given config key, converting from strings.
- [func watchStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchstringarray%28forkey,as,issecret,fileid,line,updateshandler%29-7snta.md)
  Watches for updates to an array of config values for the given config key, converting from strings.
- [func watchStringArray<Return>(forKey: ConfigKey, isSecret: Bool, default: [String], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[String], Never>) async throws -> Return) async throws -> Return](./configreader/watchstringarray%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return](./configreader/watchstringarray%28forkey,as,issecret,default,fileid,line,updateshandler%29-9t8bb.md)
  Watches for updates to an array of config values for the given config key with default fallback, converting from strings.
- [func watchStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return](./configreader/watchstringarray%28forkey,as,issecret,default,fileid,line,updateshandler%29-256k2.md)
  Watches for updates to an array of config values for the given config key with default fallback, converting from strings.
### Watching required lists of string values
- [func watchRequiredStringArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[String], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredstringarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
- [func watchRequiredStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredstringarray%28forkey,as,issecret,fileid,line,updateshandler%29-4acy.md)
  Watches for updates to a required array of config values for the given config key, converting from strings.
- [func watchRequiredStringArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredstringarray%28forkey,as,issecret,fileid,line,updateshandler%29-8wvyc.md)
  Watches for updates to a required array of config values for the given config key, converting from strings.
### Watching Boolean values
- [func watchBool<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Bool?, Never>) async throws -> Return) async throws -> Return](./configreader/watchbool%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchBool<Return>(forKey: ConfigKey, isSecret: Bool, default: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Bool, Never>) async throws -> Return) async throws -> Return](./configreader/watchbool%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
### Watching required Boolean values
- [func watchRequiredBool<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Bool, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredbool%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
### Watching lists of Boolean values
- [func watchBoolArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Bool]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchboolarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchBoolArray<Return>(forKey: ConfigKey, isSecret: Bool, default: [Bool], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Bool], Never>) async throws -> Return) async throws -> Return](./configreader/watchboolarray%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
### Watching required lists of Boolean values
- [func watchRequiredBoolArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Bool], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredboolarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
### Watching integer values
- [func watchInt<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Int?, Never>) async throws -> Return) async throws -> Return](./configreader/watchint%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchInt<Return>(forKey: ConfigKey, isSecret: Bool, default: Int, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Int, Never>) async throws -> Return) async throws -> Return](./configreader/watchint%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./configreader/watchint%28forkey,as,issecret,fileid,line,updateshandler%29-1jgbh.md)
  Watches for updates to a config value for the given config key, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value?, Never>) async throws -> Return) async throws -> Return](./configreader/watchint%28forkey,as,issecret,fileid,line,updateshandler%29-8ybja.md)
  Watches for updates to a config value for the given config key, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./configreader/watchint%28forkey,as,issecret,default,fileid,line,updateshandler%29-933s1.md)
  Watches for updates to a config value for the given config key with default fallback, converting from an integer.
- [func watchInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: Value, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, Never>) async throws -> Return) async throws -> Return](./configreader/watchint%28forkey,as,issecret,default,fileid,line,updateshandler%29-4fnhy.md)
  Watches for updates to a config value for the given config key with default fallback, converting from an integer.
### Watching required integer values
- [func watchRequiredInt<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Int, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredint%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
- [func watchRequiredInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredint%28forkey,as,issecret,fileid,line,updateshandler%29-9s54e.md)
  Watches for updates to a required config value for the given config key, converting from an integer.
- [func watchRequiredInt<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Value, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredint%28forkey,as,issecret,fileid,line,updateshandler%29-8ydgp.md)
  Watches for updates to a required config value for the given config key, converting from an integer.
### Watching lists of integer values
- [func watchIntArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Int]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchintarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchIntArray<Return>(forKey: ConfigKey, isSecret: Bool, default: [Int], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Int], Never>) async throws -> Return) async throws -> Return](./configreader/watchintarray%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchintarray%28forkey,as,issecret,fileid,line,updateshandler%29-getl.md)
  Watches for updates to an array of config values for the given config key, converting from integers.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchintarray%28forkey,as,issecret,fileid,line,updateshandler%29-3wh9t.md)
  Watches for updates to an array of config values for the given config key, converting from integers.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return](./configreader/watchintarray%28forkey,as,issecret,default,fileid,line,updateshandler%29-1qrsh.md)
  Watches for updates to an array of config values for the given config key with default fallback, converting from integers.
- [func watchIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, default: [Value], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], Never>) async throws -> Return) async throws -> Return](./configreader/watchintarray%28forkey,as,issecret,default,fileid,line,updateshandler%29-3987h.md)
  Watches for updates to an array of config values for the given config key with default fallback, converting from integers.
### Watching required lists of integer values
- [func watchRequiredIntArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Int], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredintarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
- [func watchRequiredIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredintarray%28forkey,as,issecret,fileid,line,updateshandler%29-84hp3.md)
  Watches for updates to a required array of config values for the given config key, converting from integers.
- [func watchRequiredIntArray<Value, Return>(forKey: ConfigKey, as: Value.Type, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Value], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredintarray%28forkey,as,issecret,fileid,line,updateshandler%29-6r3y7.md)
  Watches for updates to a required array of config values for the given config key, converting from integers.
### Watching double values
- [func watchDouble<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Double?, Never>) async throws -> Return) async throws -> Return](./configreader/watchdouble%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchDouble<Return>(forKey: ConfigKey, isSecret: Bool, default: Double, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Double, Never>) async throws -> Return) async throws -> Return](./configreader/watchdouble%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
### Watching required double values
- [func watchRequiredDouble<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Double, any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequireddouble%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
### Watching lists of double values
- [func watchDoubleArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Double]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchdoublearray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchDoubleArray<Return>(forKey: ConfigKey, isSecret: Bool, default: [Double], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Double], Never>) async throws -> Return) async throws -> Return](./configreader/watchdoublearray%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
### Watching required lists of double values
- [func watchRequiredDoubleArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[Double], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequireddoublearray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
### Watching bytes
- [func watchBytes<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[UInt8]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchbytes%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchBytes<Return>(forKey: ConfigKey, isSecret: Bool, default: [UInt8], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[UInt8], Never>) async throws -> Return) async throws -> Return](./configreader/watchbytes%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
### Watching required bytes
- [func watchRequiredBytes<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[UInt8], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredbytes%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.
### Watching lists of byte chunks
- [func watchByteChunkArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[[UInt8]]?, Never>) async throws -> Return) async throws -> Return](./configreader/watchbytechunkarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key.
- [func watchByteChunkArray<Return>(forKey: ConfigKey, isSecret: Bool, default: [[UInt8]], fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[[UInt8]], Never>) async throws -> Return) async throws -> Return](./configreader/watchbytechunkarray%28forkey,issecret,default,fileid,line,updateshandler%29.md)
  Watches for updates to a config value for the given config key with default fallback.
### Watching required lists of byte chunks
- [func watchRequiredByteChunkArray<Return>(forKey: ConfigKey, isSecret: Bool, fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<[[UInt8]], any Error>) async throws -> Return) async throws -> Return](./configreader/watchrequiredbytechunkarray%28forkey,issecret,fileid,line,updateshandler%29.md)
  Watches for updates to a required config value for the given config key.

## See Also

### Reading from a snapshot
- [func snapshot() -> ConfigSnapshotReader](./configreader/snapshot%28%29.md)
  Returns a snapshot of the current configuration state.
- [func watchSnapshot<Return>(fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<ConfigSnapshotReader, Never>) async throws -> Return) async throws -> Return](./configreader/watchsnapshot%28fileid,line,updateshandler%29.md)
  Watches the configuration for changes.
- [Synchronously reading values](./configreader-get.md)
- [Asynchronously fetching values](./configreader-fetch.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader-watch)*