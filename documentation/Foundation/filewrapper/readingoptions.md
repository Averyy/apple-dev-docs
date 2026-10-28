# FileWrapper.ReadingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Reading options that can be set by the [`init(url:options:)`](./init%28url,options%29-70161.md) and [`read(from:options:)`](./read%28from,options%29.md) methods.

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
struct ReadingOptions
```

```c
enum NSFileWrapperReadingOptions : NSUInteger;
```

## Overview

You can use the `NSFileWrapperReadingImmediate` and `NSFileWrapperReadingWithoutMapping` reading options together to take an exact snapshot of a file-system hierarchy that is safe from all errors (including the ones mentioned above) once reading has succeeded. If reading with both options succeeds, then subsequent invocations of the methods listed in the comment for the `NSFileWrapperReadingImmediate` reading option to the receiver and all its descendant file wrappers will never fail. However, note that reading with both options together is expensive in terms of both I/O and memory for large files, or directories containing large files, or even directories containing many small files.

## Topics

### Constants
- [static var immediate: FileWrapper.ReadingOptions](./readingoptions/immediate.md)
  The option to read files immediately after creating a file wrapper.
- [static var withoutMapping: FileWrapper.ReadingOptions](./readingoptions/withoutmapping.md)
  Whether file mapping for regular file wrappers is disallowed.
### Initializers
- [init(rawValue: UInt)](./readingoptions/init%28rawvalue%29.md)

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
- [FileWrapper.WritingOptions](./writingoptions.md)
  Writing options that can be set by the [`write(to:options:originalContentsURL:)`](./write%28to,options,originalcontentsurl%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filewrapper/readingoptions)*