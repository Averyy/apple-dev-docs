# write(to:)

**Framework**: RealityKit  
**Kind**: method

Exports the entity as a RealityKit file to a location in the file system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func write(to url: URL) async throws
```

#### Discussion

This method generates a file with a `.reality` suffix, automatically setting its compatibility with other systems based on the Entity’s tree content. The Entity and its children may contain components or assets that can require the resulting RealityKit file to be compatible with system versions between:

- iOS 18 or later
- macOS 15 or later
- visionOS 2 or later

Logs with the prefix [RealityKit File Compatibility Info] will be posted to the console whenever a component or asset requires a compatibility adjustment.

> ❗ **Important**:  During its initial setup phase, this method can indirectly block the main thread, and also has the potential to block it for the full duration of the call if the system has additional work it needs to do there.

## Parameters

- `url`: The location URL in the file system where you want to save the   file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/write(to:))*