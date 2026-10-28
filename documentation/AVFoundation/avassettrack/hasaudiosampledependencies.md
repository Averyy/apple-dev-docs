# hasAudioSampleDependencies

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track has sample dependencies.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 13.0
- tvOS 13.0+ - Deprecated in 16.0
- watchOS 6.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`hasAudioSampleDependencies`](../avpartialasyncproperty/hasaudiosampledependencies.md) asynchronously instead.

## Declaration

```swift
var hasAudioSampleDependencies: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasAudioSampleDependencies;
```

## Discussion

The value is always [`false`](../../Swift/false.md) for nonaudible media.

## See Also

### Accessing audible characteristics
- [preferredVolume](./preferredvolume.md)
  The track’s volume preference for playing its audible media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/hasaudiosampledependencies)*