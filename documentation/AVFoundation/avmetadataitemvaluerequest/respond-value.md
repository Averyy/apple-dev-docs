# respond(value:)

**Framework**: AVFoundation  
**Kind**: method

Returns the metadata item’s value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func respond(value: any NSCopying & NSObjectProtocol)
```

#### Discussion

You call this method to return the metadata item’s value.

## Parameters

- `value`: The value to return for the request.

## See Also

- [func respond(error: any Error)](avmetadataitemvaluerequest/respond(error:).md)
  Returns an error when the system fails to load the value.
- [var metadataItem: AVMetadataItem?](avmetadataitemvaluerequest/metadataitem.md)
  The metadata item to request a value for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/respond(value:))*