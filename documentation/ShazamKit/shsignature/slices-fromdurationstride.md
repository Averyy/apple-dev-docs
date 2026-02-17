# slices(from:duration:stride:)

**Framework**: ShazamKit  
**Kind**: method

Returns a sequence of signatures of the specified duration from a starting value, stepping by the stride.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func slices(from start: TimeInterval, duration: TimeInterval, stride: TimeInterval? = nil) throws -> SHSignature.Slices
```

#### Return Value

A sequence from `start` of `duration` length. Each value in the sequence is separated by `stride`.

#### Discussion

When you recognize audio with [`match(_:)`](shsession/match(_:).md),  signature duration should be between [`minimumQuerySignatureDuration`](shcatalog/minimumquerysignatureduration.md) and [`maximumQuerySignatureDuration`](shcatalog/maximumquerysignatureduration.md).  Use this method to slice signatures longer than the maximum duration.

Slicing allows you to test specific parts of the audio. If you know certain parts of an audio are clearer or more likely to have recognizable content, prioritize matching those slices.

The code below creates slices from a signature and uses the first three slices to find a match:

```swift
let signature = try await SHSignatureGenerator.signature(from: audioAsset)
let slices = try signature.slices(from: 2.0, duration: 10.0, stride: 5.0)

// Use the first 3 slices to find a match.
for try await slice in slices.prefix(3) {
   session.match(slice)
}
```

You can use AsyncSequence operators like [`prefix(_:)`](https://developer.apple.com/documentation/Swift/AsyncSequence/prefix(_:)) or [`first(where:)`](https://developer.apple.com/documentation/Swift/AsyncSequence/first(where:)) to choose which slices are processed.

The `stride` parameter controls overlap between slices. A smaller stride creates more slices with greater overlap, which increases the number of matching requests. Larger strides create fewer slices, however there are fewer matching requests.

For continuous matching as audio becomes available, use [`matchStreamingBuffer(_:at:)`](shsession/matchstreamingbuffer(_:at:).md), which automatically generates and matches signatures from audio buffers.

## Parameters

- `start`: The starting value to use for the sequence.
- `duration`: The desired duration of each sliced signature.
- `stride`: The amount to step by for each slice. Must be a non-zero positive value.

## See Also

- [SHSignature.Slices](shsignature/slices.md)
  A sequence of signature segments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature/slices(from:duration:stride:))*