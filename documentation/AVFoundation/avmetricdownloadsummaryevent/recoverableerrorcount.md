# recoverableErrorCount

**Framework**: AVFoundation  
**Kind**: property

Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var recoverableErrorCount: Int { get }
```

#### Discussion

Error counts may not be consistent across OS versions. Comparisons should be made within a given OS version, as error reporting is subject to change with OS updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent/recoverableerrorcount)*