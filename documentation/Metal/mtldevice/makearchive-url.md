# makeArchive(url:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new archive from data available at an `NSURL` address.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeArchive(url: URL) throws -> any MTL4Archive
```

#### Return Value

A [`MTL4Archive`](mtl4archive.md) instance, or `nil` if the function failed.

## Parameters

- `url`: An   instance that represents the path from which the device loads the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makearchive(url:))*