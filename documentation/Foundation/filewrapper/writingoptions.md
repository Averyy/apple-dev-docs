# FileWrapper.WritingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Writing options that can be set by the [`write(to:options:originalContentsURL:)`](./write%28to,options,originalcontentsurl%29.md) method.

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

```c
enum NSFileWrapperWritingOptions : NSUInteger;
```

## Topics

### Constants
- [static var atomic: FileWrapper.WritingOptions](./writingoptions/atomic.md)
  Whether writing is done atomically.
- [static var withNameUpdating: FileWrapper.WritingOptions](./writingoptions/withnameupdating.md)
  Whether descendant file wrappers’[`filename`](./filename.md) properties are set if the writing succeeds.
### Initializers
- [init(rawValue: UInt)](./writingoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [FileWrapper.ReadingOptions](./readingoptions.md)
  Reading options that can be set by the [`init(url:options:)`](./init%28url,options%29-70161.md) and [`read(from:options:)`](./read%28from,options%29.md) methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/writingoptions)*