# CFRunLoopRunResult

**Framework**: Core Foundation  
**Kind**: enum

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFRunLoopRunResult
```

## Topics

### Constants
- [CFRunLoopRunResult.finished](cfrunlooprunresult/finished.md)
  The running run loop mode has no sources or timers to process.
- [CFRunLoopRunResult.handledSource](cfrunlooprunresult/handledsource.md)
  A source has been processed. This value is returned only if the run loop was told to run only until a source was processed.
- [CFRunLoopRunResult.stopped](cfrunlooprunresult/stopped.md)
  [`CFRunLoopStop(_:)`](cfrunloopstop(_:).md) was called on the run loop.
- [CFRunLoopRunResult.timedOut](cfrunlooprunresult/timedout.md)
  The specified time interval for running the run loop has passed.
### Initializers
- [init?(rawValue: Int32)](cfrunlooprunresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CFFileSecurityClearOptions](cffilesecurityclearoptions.md)
- [struct CFISO8601DateFormatOptions](cfiso8601dateformatoptions.md)
- [struct CFURLEnumeratorOptions](cfurlenumeratoroptions.md)
  Options for controlling enumerator behavior.
- [enum CFURLEnumeratorResult](cfurlenumeratorresult.md)
  Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function.
- [enum CGRectEdge](cgrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooprunresult)*