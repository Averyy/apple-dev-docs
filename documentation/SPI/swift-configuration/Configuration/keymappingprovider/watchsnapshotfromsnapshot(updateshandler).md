---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/watchsnapshotfromsnapshot(updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchSnapshotFromSnapshot(updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Implements `watchSnapshot` by getting the current snapshot and emitting it immediately.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
(nonsending) func watchSnapshotFromSnapshot<Return>(updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

#### Return Value

The value returned by the handler closure.

#### Discussion

Use this convenience method for providers whose state doesn’t change over time. The method creates an async sequence that emits the current snapshot once and then remains idle.

This is suitable for providers that load configuration from static sources like files or environment variables that don’t change during application runtime.

The following example shows using this convenience function:

```swift
func watchSnapshot(
    updatesHandler: (_ updates: ConfigUpdatesAsyncSequence<any ConfigSnapshot, Never>) async throws -> Void
) async throws {
    try await watchSnapshotFromSnapshot(updatesHandler)
}
```

> **Throws**: Provider-specific errors or errors thrown by the handler.

## Parameters

- `updatesHandler`: The closure that processes the async sequence of snapshot updates.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/watchsnapshotfromsnapshot(updateshandler:))*