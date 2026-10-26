# configureForResumableExportWithCompletionHandler:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Attempts to configure the export session into resumption mode.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (void) configureForResumableExportWithCompletionHandler:(void (^)(AVAssetExportSessionResumptionState *resumptionState)) handler;
```

#### Discussion

For select encoders, an export can be performed in temporal segments, and then stitched together at the end.

You are responsible for configuring the export session identically for subsequent sessions, if the export is to be resumed from partial results from a previous run.

> ❗ **Important**: [`directoryForTemporaryFiles`](./directoryfortemporaryfiles.md) must be specified for resumable exports. This directory holds the temporary files for resumable exports, which allows the export to resume on a subsequent instantiation. You are responsible for making the [`directoryForTemporaryFiles`](./directoryfortemporaryfiles.md) unique and deterministic across app launches or device reboots if the session is intended to be resumable after such events. You must ensure that it doesn’t re-use a temporary directory corresponding to a different resumable export session, or the contents between different exports may be erroneously combined.

This method validates that the currently configured export properties allow resumption, and interrogates the contents of [`directoryForTemporaryFiles`](./directoryfortemporaryfiles.md) to determine whether this is a resuming session or a new one. As such, call this method after all settings are finalized for this export session, that is, just prior to [`exportAsynchronously(completionHandler:)`](./exportasynchronously%28completionhandler%29.md).

`resumptionState` details the currently configured resumption state of the export session. Even if resumptionState indicates that not all conditions for resumption are met, you may still call [`exportAsynchronously(completionHandler:)`](./exportasynchronously%28completionhandler%29.md) using the current session, and the export proceeds in the default, non-resuming manner.

This method cannot be called after the export has started.

Call [`cancelExport()`](./cancelexport%28%29.md) if an in-flight export needs to be interrupted. The export maintains the partial results.

You are responsible for deleting the temporary directory and its contents if the export will never be resumed.

Because intermediate files are written to support the resume functionality, resumable exports typically double the NAND accesses, because the samples need to be written to disk twice.

## Parameters

- `handler`: A callback that receives the resumption configuration state. If configuration fails, the system might call the handler synchronously.

## See Also

### Configuring resumable export
- [AVAssetExportSessionResumptionState](../avassetexportsessionresumptionstate.md)
  The current resumption state of the export session.
- [AVAssetExportSession.ResumptionFailureReason](./resumptionfailurereason.md)
  The reason that configuring the export session for resumption failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/configureforresumableexportwithcompletionhandler:)*