# URLError.BackgroundTaskCancelledReason.insufficientSystemResources

**Framework**: Foundation  
**Kind**: case

A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case insufficientSystemResources
```

#### Discussion

This error results from factors including (but not limited to) battery capacity, thermal condition, network connectivity, and cellular data plan.

## See Also

- [URLError.BackgroundTaskCancelledReason.backgroundUpdatesDisabled](urlerror/backgroundtaskcancelledreason-swift.enum/backgroundupdatesdisabled.md)
  A reason that indicates the system canceled the background task because background tasks are disabled.
- [URLError.BackgroundTaskCancelledReason.userForceQuitApplication](urlerror/backgroundtaskcancelledreason-swift.enum/userforcequitapplication.md)
  A reason that indicates the system canceled the background task because the user force-quit the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.enum/insufficientsystemresources)*