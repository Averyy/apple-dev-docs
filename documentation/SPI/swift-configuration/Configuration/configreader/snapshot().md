---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/snapshot()"
framework: "swift-configuration/Configuration"
---

# snapshot()

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Returns a snapshot of the current configuration state.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func snapshot() -> ConfigSnapshotReader
```

## Return Value

The snapshot.

## Discussion

The snapshot reader provides read-only access to the configuration’s state at the time you call this method.

```swift
let snapshot = config.snapshot()
// Use snapshot to read config values
let cert = snapshot.string(forKey: "cert")
let privateKey = snapshot.string(forKey: "privateKey")
// Ensures that both values are coming from the same underlying snapshot and that a provider
// didn't change its internal state between the two `string(...)` calls.
let identity = MyIdentity(cert: cert, privateKey: privateKey)
```

## See Also

### Reading from a snapshot
- [func watchSnapshot<Return>(fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<ConfigSnapshotReader, Never>) async throws -> Return) async throws -> Return](./watchsnapshot%28fileid,line,updateshandler%29.md)
  Watches the configuration for changes.
- [Synchronously reading values](../configreader-get.md)
- [Asynchronously fetching values](../configreader-fetch.md)
- [Watching values](../configreader-watch.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/snapshot())*