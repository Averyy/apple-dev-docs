# legibleOutput(_:didOutputAttributedStrings:nativeSampleBuffers:forItemTime:)

**Framework**: AVFoundation  
**Kind**: method

Asks the delegate to process the delivery of new textual samples.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [Any], forItemTime itemTime: CMTime)
```

#### Discussion

For each media subtype in the array passed in to the `output` object’s  [`init(mediaSubtypesForNativeRepresentation:)`](avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation:).md) method, the delegate receives sample buffers carrying data in its native format via the `nativeSamples` parameter if there is media data of that subtype in the media resource.

For all other media subtypes present in the media resource, the delegate receives attributed strings in a common format via the `strings` parameter.  See [`CMTextMarkup`](https://developer.apple.com/documentation/CoreMedia/cmtextmarkup) for the string attributes keys and values that are used in the attributed strings.

## Parameters

- `output`: The   source instance.
- `strings`: An array of   objects, each containing both the run of text and the descriptive markup.
- `nativeSamples`: An array of   objects, for media subtypes included in the array passed to the   object’s   method.
- `itemTime`: The item time at which the strings should be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/legibleoutput(_:didoutputattributedstrings:nativesamplebuffers:foritemtime:))*