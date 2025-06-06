# BGTaskScheduler.Error.Code.unavailable

**Framework**: Background Tasks  
**Kind**: case

A task scheduling error indicating that the app or extension can’t schedule background work.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case unavailable
```

#### Discussion

This error usually occurs for one of following reasons:

- The user has disabled background refresh in settings.
- The app is running on Simulator which doesn’t support background processing.
- The keyboard extension either hasn’t set [`RequestsOpenAccess`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/RequestsOpenAccess) to `YES` in [`The Info.plist File`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22), or the user hasn’t granted open access.
- The extension type isn’t able to schedule background tasks.

## See Also

- [BGTaskScheduler.Error.Code.notPermitted](bgtaskscheduler/error/code/notpermitted.md)
  A task scheduling error indicating the app isn’t permitted to schedule the task.
- [BGTaskScheduler.Error.Code.tooManyPendingTaskRequests](bgtaskscheduler/error/code/toomanypendingtaskrequests.md)
  A task scheduling error indicating that there are too many pending tasks of the type requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code/unavailable)*