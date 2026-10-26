---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/watchvaluefromvalue(forkey:type:updateshandler:)"
framework: "swift-configuration/Configuration"
---

# watchValueFromValue(forKey:type:updatesHandler:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Implements `watchValue` by getting the current value and emitting it immediately.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
(nonsending) func watchValueFromValue<Return>(forKey key: AbsoluteConfigKey, type: ConfigType, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Return) async throws -> Return where Return : ~Copyable
```

#### Return Value

The value returned by the handler closure.

#### Discussion

Use this convenience method for providers that store static values in memory. The method creates an async sequence that emits the current value once and then remains idle, since the values don’t change over time.

This is the most common implementation for simple providers like environment variables or JSON file providers.

The following example shows using this convenience function:

```swift
func watchValue(
    forKey: AbsoluteConfigKey,
    type: ConfigType,
    updatesHandler: (_ updates: ConfigUpdatesAsyncSequence<Result<LookupResult, any Error>, Never>) async throws -> Void
) async throws {
    try await watchValueFromValue(forKey: key, type: type, updatesHandler: updatesHandler)
}
```

> **Throws**: Provider-specific errors or errors thrown by the handler.

## Parameters

- `key`: The configuration key to monitor.
- `type`: The expected configuration value type.
- `updatesHandler`: The closure that processes the async sequence of value updates.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/keymappingprovider/watchvaluefromvalue(forkey:type:updateshandler:))*