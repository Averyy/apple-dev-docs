# serverSideProcessingTimeout

**Framework**: Matter  
**Kind**: property

Controls how much time, in seconds, we will allow for the server to process the command.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
@NSCopying
var serverSideProcessingTimeout: NSNumber? { get set }
```

#### Discussion

The command will then time out if that much time, plus an allowance for retransmits due to network failures, passes.

If nil, the framework will try to select an appropriate timeout value itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotasoftwareupdaterequestorclusterannounceotaproviderparams-1ucwe/serversideprocessingtimeout)*