# serverSideProcessingTimeout

**Framework**: Matter  
**Kind**: property

Controls how much time, in seconds, we will allow for the server to process the command.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
@NSCopying
var serverSideProcessingTimeout: NSNumber? { get set }
```

#### Discussion

The command will then time out if that much time, plus an allowance for retransmits due to network failures, passes.

If nil, the framework will try to select an appropriate timeout value itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrtimesynchronizationclustersettimezoneparams/serversideprocessingtimeout)*