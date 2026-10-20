# availableMetadataFormats

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metadata formats that contain metadata associated with the option.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var availableMetadataFormats: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableMetadataFormats;
```

#### Discussion

The array contains `NSString` objects, each representing a metadata format that contains metadata associated with the option (for example, ID3, iTunes metadata, and so on).

## See Also

### Managing metadata
- [var commonMetadata: [AVMetadataItem]](./commonmetadata.md)
  An array of metadata items for each common metadata key for which a value is available.
- [func metadata(forFormat: String) -> [AVMetadataItem]](./metadata%28forformat%29.md)
  Returns an array of metadata items—one for each metadata item in the container of a given format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/availablemetadataformats)*