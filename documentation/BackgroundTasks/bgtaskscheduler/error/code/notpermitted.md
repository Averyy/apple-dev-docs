# BGTaskScheduler.Error.Code.notPermitted

**Framework**: Background Tasks  
**Kind**: case

A task scheduling error indicating the app isn’t permitted to schedule the task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case notPermitted
```

#### Discussion

There are two causes for this error:

- The app doesn’t set the appropriate mode in the [`UIBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes) array.
- The task identifier of the submitted task wasn’t in the [`BGTaskSchedulerPermittedIdentifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BGTaskSchedulerPermittedIdentifiers) array in [`the Info.plist File`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22).

## See Also

- [BGTaskScheduler.Error.Code.tooManyPendingTaskRequests](bgtaskscheduler/error/code/toomanypendingtaskrequests.md)
  A task scheduling error indicating that there are too many pending tasks of the type requested.
- [BGTaskScheduler.Error.Code.unavailable](bgtaskscheduler/error/code/unavailable.md)
  A task scheduling error indicating that the app or extension can’t schedule background work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code/notpermitted)*