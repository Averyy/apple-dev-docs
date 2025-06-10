# write(to:)

**Framework**: RealityKit  
**Kind**: method

Writes the configurations of the configuration catalog to a reality file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
func write(to url: URL) async throws
```

#### Discussion

Another configuration catalog instance can open the `.reality` file for reading.

## Parameters

- `url`: The destination where the configuration catalog writes the   file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog-2tett/write(to:))*