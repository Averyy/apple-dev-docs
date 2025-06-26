# BGTaskScheduler.Error.Code.unavailable

**Framework**: Background Tasks  
**Kind**: case

A task scheduling error that indicates the app or extension can’t schedule background work.

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

This error usually occurs for one of three reasons:

- A person disabled background refresh in settings.
- The app runs on Simulator which doesn’t support background processing.
- The extension either didn’t set [`RequestsOpenAccess`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/RequestsOpenAccess) to `YES` in [`The Info.plist File`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22), or a person didn’t grant open access.

## See Also

- [BGTaskScheduler.Error.Code.notPermitted](bgtaskscheduler/error/code/notpermitted.md)
  A task scheduling error that indicates the app isn’t permitted to launch the task.
- [BGTaskScheduler.Error.Code.tooManyPendingTaskRequests](bgtaskscheduler/error/code/toomanypendingtaskrequests.md)
  A task scheduling error that indicates there are too many pending tasks of the type requested.
- [BGTaskScheduler.Error.Code.immediateRunIneligible](bgtaskscheduler/error/code/immediaterunineligible.md)
  A task scheduling error that indicates a task request didn’t run immediately due to system conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/code/unavailable)*