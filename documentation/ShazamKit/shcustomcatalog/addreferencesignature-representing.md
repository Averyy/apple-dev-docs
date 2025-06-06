# addReferenceSignature(_:representing:)

**Framework**: ShazamKit  
**Kind**: method

Adds a reference signature and its associated metadata to a catalog.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func addReferenceSignature(_ signature: SHSignature, representing mediaItems: [SHMediaItem]) throws
```

#### Discussion

> **Note**:  This system ignores calls to `addReferenceSignature(_:representing:)` after adding the catalog to an `SHSession`.

 This system ignores calls to `addReferenceSignature(_:representing:)` after adding the catalog to an `SHSession`.

## Parameters

- `signature`: The reference signature for the audio recording.
- `mediaItems`: The metadata for the recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shcustomcatalog/addreferencesignature(_:representing:))*