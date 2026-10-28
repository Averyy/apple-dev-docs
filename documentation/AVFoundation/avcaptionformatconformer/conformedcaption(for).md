# conformedCaption(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a caption that conforms to a specific format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func conformedCaption(for caption: AVCaption) throws -> AVCaption
```

```objc
- (AVCaption *) conformedCaptionForCaption:(AVCaption *) caption error:(NSError **) outError;
```

## Return Value

A caption that conforms to the defined caption format.

## Parameters

- `caption`: The caption to conform.

## See Also

### Conforming captions
- [var conformsCaptionsToTimeRange: Bool](./conformscaptionstotimerange.md)
  A Boolean value that indicates whether to conform the time range of a canonical caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionformatconformer/conformedcaption(for:))*