# write(to:)

**Framework**: RealityKit  
**Kind**: method

Exports the entity as a RealityKit file to a location in the file system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func write(to url: URL) async throws
```

#### Discussion

This method generates a file with a `.reality` suffix that’s compatible with the following systems:

- iOS 18 and later
- macOS 15 and later
- visionOS 2 and later

> ❗ **Important**:  During its initial setup phase, this method can indirectly block the main thread, and also has the potential to block it for the full duration of the call if the system has additional work it needs to do there.

 During its initial setup phase, this method can indirectly block the main thread, and also has the potential to block it for the full duration of the call if the system has additional work it needs to do there.

## Parameters

- `url`: The location URL in the file system where you want to save the   file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/write(to:))*