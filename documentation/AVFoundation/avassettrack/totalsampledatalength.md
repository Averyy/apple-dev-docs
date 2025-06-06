# totalSampleDataLength

**Framework**: AVFoundation  
**Kind**: property

The total number of bytes of sample data the track requires.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var totalSampleDataLength: Int64 { get }
```

#### Discussion

The value may be `0` if the framework can’t determine the total sample data length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/totalsampledatalength)*