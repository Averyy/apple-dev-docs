# totalSampleDataLength

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The total number of bytes of sample data the track requires.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`totalSampleDataLength`](../avpartialasyncproperty/totalsampledatalength.md) asynchronously instead.

## Declaration

```swift
var totalSampleDataLength: Int64 { get }
```

```objc
@property (nonatomic, readonly) long long totalSampleDataLength;
```

#### Discussion

The value may be `0` if the framework can’t determine the total sample data length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/totalsampledatalength)*