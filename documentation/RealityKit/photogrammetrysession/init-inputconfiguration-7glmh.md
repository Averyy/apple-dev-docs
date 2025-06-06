# init(input:configuration:)

**Framework**: Realitykit  
**Kind**: init

Creates a session from a sequence of samples.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
convenience init<S>(input: S, configuration: PhotogrammetrySession.Configuration = Configuration()) throws where S : Sequence, S.Element == PhotogrammetrySample
```

#### Discussion

Creates a new session instance from a custom sequence of [`PhotogrammetrySample`](photogrammetrysample.md) objects by iterating over the provided  [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) object.

The constructor will only use `makeIterator()` on `input` and will then iterate through the sequence only once.  A provided iterator should be lazy, or a lazy  [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) and map used.

> **Note**: To minimize memory usage, use lazy sequences that only create a [`PhotogrammetrySample`](photogrammetrysample.md) as it iterates by making calls to `next()` on its associated [`IteratorProtocol`](https://developer.apple.com/documentation/Swift/IteratorProtocol).

## Parameters

- `input`: The input   that will be iterated once to yield all input data.
- `configuration`: The session-wide configuration to use for this session.

## See Also

- [convenience init(input: URL, configuration: PhotogrammetrySession.Configuration) throws](photogrammetrysession/init(input:configuration:)-wo4e.md)
  Creates a session from a specified directory of images.
- [static var isSupported: Bool](photogrammetrysession/issupported.md)
  Returns `true` if the current hardware supports Object Capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/init(input:configuration:)-7glmh)*