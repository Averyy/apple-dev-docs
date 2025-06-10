# serverSideProcessingTimeout

**Framework**: Matter  
**Kind**: property

Controls how much time, in seconds, we will allow for the server to process the command.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.0+
- watchOS 10.2+

## Declaration

```swift
@NSCopying
var serverSideProcessingTimeout: NSNumber? { get set }
```

#### Discussion

The command will then time out if that much time, plus an allowance for retransmits due to network failures, passes.

If nil, the framework will try to select an appropriate timeout value itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersetutctimeparams-1ru2r/serversideprocessingtimeout)*