# metadata

**Framework**: AVFoundation  
**Kind**: property

An array of metadata items for all metadata identifiers for which a value is available.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
var metadata: [AVMetadataItem] { get }
```

#### Discussion

You can filter the metadata items by language using the [`metadataItems(from:filteredAndSortedAccordingToPreferredLanguages:)`](avmetadataitem/metadataitems(from:filteredandsortedaccordingtopreferredlanguages:).md) method, or by identifier with the [`metadataItems(from:filteredByIdentifier:)`](avmetadataitem/metadataitems(from:filteredbyidentifier:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/metadata)*