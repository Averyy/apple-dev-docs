# metadata(forFormat:)

**Framework**: AVFoundation  
**Kind**: method

Returns metadata items that a track contains for the specified format.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
func metadata(forFormat format: AVMetadataFormat) -> [AVMetadataItem]
```

#### Return Value

An array of metadata items matching the specified format, or an empty array if none are found.

#### Discussion

Apple discourages the use of this method in iOS 15, tvOS 15, and macOS 12 or later. Load track metadata asynchronously using [`loadMetadata(for:completionHandler:)`](avassettrack/loadmetadata(for:completionhandler:).md) instead.

You can call this method without blocking the current thread after you’ve loaded the [`availableMetadataFormats`](avassettrack/availablemetadataformats.md) property.

## Parameters

- `format`: The format of the metadata items to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/metadata(forformat:))*