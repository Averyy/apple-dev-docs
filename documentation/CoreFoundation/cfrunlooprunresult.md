# CFRunLoopRunResult

**Framework**: Core Foundation  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CFRunLoopRunResult
```

```c
enum CFRunLoopRunResult : SInt32;
```

## Topics

### Constants
- [CFRunLoopRunResult.finished](./cfrunlooprunresult/finished.md)
  The running run loop mode has no sources or timers to process.
- [CFRunLoopRunResult.handledSource](./cfrunlooprunresult/handledsource.md)
  A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.
- [CFRunLoopRunResult.stopped](./cfrunlooprunresult/stopped.md)
  [`CFRunLoopStop(_:)`](./cfrunloopstop%28_%29.md) was called on the run loop.
- [CFRunLoopRunResult.timedOut](./cfrunlooprunresult/timedout.md)
  The specified time interval for running the run loop has passed.
### Initializers
- [init?(rawValue: Int32)](./cfrunlooprunresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [struct CFFileSecurityClearOptions](./cffilesecurityclearoptions.md)
- [struct CFISO8601DateFormatOptions](./cfiso8601dateformatoptions.md)
- [struct CFURLEnumeratorOptions](./cfurlenumeratoroptions.md)
  Options for controlling enumerator behavior.
- [enum CFURLEnumeratorResult](./cfurlenumeratorresult.md)
  Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](./cfurlenumeratorgetnexturl%28_,_,_%29.md) function.
- [enum CGRectEdge](./cgrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult)*