# FileWrapper.WritingOptions

**Framework**: Foundation  
**Kind**: struct

Writing options that can be set by the [`write(to:options:originalContentsURL:)`](filewrapper/write(to:options:originalcontentsurl:).md) method.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct WritingOptions
```

## Topics

### Constants
- [static var atomic: FileWrapper.WritingOptions](filewrapper/writingoptions/atomic.md)
  Whether writing is done atomically.
- [static var withNameUpdating: FileWrapper.WritingOptions](filewrapper/writingoptions/withnameupdating.md)
  Whether descendant file wrappers’[`filename`](filewrapper/filename.md) properties are set if the writing succeeds.
### Initializers
- [init(rawValue: UInt)](filewrapper/writingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [FileWrapper.ReadingOptions](filewrapper/readingoptions.md)
  Reading options that can be set by the [`init(url:options:)`](filewrapper/init(url:options:)-70161.md) and [`read(from:options:)`](filewrapper/read(from:options:).md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/writingoptions)*