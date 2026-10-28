---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/watchvalue(forkey:type:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchValue(forKey:type:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Monitors a configuration key for value changes over time.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func watchValue<Return>(forKey key: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

Available when `Snapshot` conforms to `FileConfigSnapshot`.

## Return Value

The value returned by the closure.

## Discussion

The async sequence provided to the handler should immediately emit the current value (equivalent to calling [`value(forKey:type:)`](./value%28forkey,type%29.md)), followed by subsequent updates as they occur.

The sequence completes gracefully when the current task is canceled, to allow proper cleanup of resources.

> **Throws**: Provider-specific errors or errors thrown by the handler closure.

## Parameters

- `key`: The configuration key to monitor.
- `type`: The expected configuration value type.
- `updatesHandler`: The closure that processes the async sequence of value updates.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider/watchvalue(forkey:type:updateshandler:))*