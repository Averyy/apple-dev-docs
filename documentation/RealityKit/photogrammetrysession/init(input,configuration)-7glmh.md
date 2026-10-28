# init(input:configuration:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

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

**Other overloads**:

```swift
convenience init(input: URL, configuration: PhotogrammetrySession.Configuration = Configuration()) throws
```

## Discussion

Creates a new session instance from a custom sequence of [`PhotogrammetrySample`](../photogrammetrysample.md) objects by iterating over the provided  [`Sequence`](../../Swift/sequence.md) object.

The constructor will only use `makeIterator()` on `input` and will then iterate through the sequence only once.  A provided iterator should be lazy, or a lazy  [`Sequence`](../../Swift/sequence.md) and map used.

> **Note**: To minimize memory usage, use lazy sequences that only create a [`PhotogrammetrySample`](../photogrammetrysample.md) as it iterates by making calls to `next()` on its associated [`IteratorProtocol`](../../Swift/iteratorprotocol.md).

## Parameters

- `input`: The input `Sequence` that will be iterated once to yield all input data.
- `configuration`: The session-wide configuration to use for this session.

## See Also

### Creating the session
- [convenience init(input: URL, configuration: PhotogrammetrySession.Configuration) throws](./init%28input,configuration%29-wo4e.md)
  Creates a session from a specified directory of images.
- [static var isSupported: Bool](./issupported.md)
  Returns `true` if the current hardware supports Object Capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/init(input:configuration:)-7glmh)*