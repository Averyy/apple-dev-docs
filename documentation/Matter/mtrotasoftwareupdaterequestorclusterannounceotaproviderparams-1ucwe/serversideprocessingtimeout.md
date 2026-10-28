# serverSideProcessingTimeout

**Framework**: Matter  
**Kind**: property  
**Role**: Instance Property

Controls how much time, in seconds, we will allow for the server to process the command.

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use MTROTASoftwareUpdateRequestorClusterAnnounceOTAProviderParams

## Declaration

```swift
@NSCopying
var serverSideProcessingTimeout: NSNumber? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSNumber * serverSideProcessingTimeout;
```

## Discussion

The command will then time out if that much time, plus an allowance for retransmits due to network failures, passes.

If nil, the framework will try to select an appropriate timeout value itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrotasoftwareupdaterequestorclusterannounceotaproviderparams-1ucwe/serversideprocessingtimeout)*