---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchsnapshot(fileid:line:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchSnapshot(fileID:line:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Watches the configuration for changes.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchSnapshot<Return>(fileID: String = #fileID, line: UInt = #line, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<ConfigSnapshotReader, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

## Return Value

The value returned by the handler.

## Discussion

This method watches the configuration for changes and provides a stream of snapshots to the handler closure. Each snapshot represents the configuration state at a specific point in time.

```swift
try await config.watchSnapshot { snapshots in
    for await snapshot in snapshots {
        // Process each new configuration snapshot
        let cert = snapshot.string(forKey: "cert")
        let privateKey = snapshot.string(forKey: "privateKey")
        // Ensures that both values are coming from the same underlying snapshot and that a provider
        // didn't change its internal state between the two `string(...)` calls.
        let newCert = MyCert(cert: cert, privateKey: privateKey)
        print("Certificate was updated: \(newCert.redactedDescription)")
    }
}
```

> **Throws**: Any error thrown by the handler.

## Parameters

- `fileID`: The file where this method is called from.
- `line`: The line where this method is called from.
- `updatesHandler`: A closure that receives an async sequence of `ConfigSnapshotReader` instances.

## See Also

### Reading from a snapshot
- [func snapshot() -> ConfigSnapshotReader](./snapshot%28%29.md)
  Returns a snapshot of the current configuration state.
- [Synchronously reading values](../configreader-get.md)
- [Asynchronously fetching values](../configreader-fetch.md)
- [Watching values](../configreader-watch.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader/watchsnapshot(fileid:line:updateshandler:))*