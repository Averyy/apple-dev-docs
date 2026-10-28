# configurationFailureReason

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The reason that the export session couldn’t be configured as resumable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (readonly, nullable) AVAssetExportSessionResumptionFailureReason configurationFailureReason;
```

## Discussion

This value is valid only when [`resumptionConfigured`](./resumptionconfigured.md) is `false`.

## See Also

### Inspecting the resumption state
- [resumptionConfigured](./resumptionconfigured.md)
  A Boolean value that indicates whether the export session is configured as resumable.
- [resumingFromPreviousState](./resumingfrompreviousstate.md)
  A Boolean value that indicates whether or not a resuming export is continuing from a previous state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsessionresumptionstate/configurationfailurereason)*