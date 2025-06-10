# recoverableErrorCount

**Framework**: AVFoundation  
**Kind**: property

Returns the total count of recoverable errors encountered during the download. If no errors were encountered, returns 0.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var recoverableErrorCount: Int { get }
```

#### Discussion

Error counts may not be consistent across OS versions. Comparisons should be made within a given OS version, as error reporting is subject to change with OS updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricdownloadsummaryevent/recoverableerrorcount)*