# resumptionConfigured

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the export session is configured as resumable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@property (readonly, getter=isResumptionConfigured) BOOL resumptionConfigured;
```

#### Discussion

If `true`, the export session is configured as resumable. If `false`, the export session will remain as non-resumable (default). You can still call [`exportAsynchronously(completionHandler:)`](../avassetexportsession/exportasynchronously%28completionhandler%29.md) when this property is `false`.

## See Also

### Inspecting the resumption state
- [resumingFromPreviousState](./resumingfrompreviousstate.md)
  A Boolean value that indicates whether or not a resuming export is continuing from a previous state.
- [configurationFailureReason](./configurationfailurereason.md)
  The reason that the export session couldn’t be configured as resumable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsessionresumptionstate/resumptionconfigured)*