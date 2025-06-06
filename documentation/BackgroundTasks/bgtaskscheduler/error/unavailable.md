# unavailable

**Framework**: Background Tasks  
**Kind**: property

A task scheduling error indicating that the app or extension can’t schedule background work.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var unavailable: BGTaskScheduler.Error.Code { get }
```

#### Discussion

This error usually occurs for one of three reasons:

- The user has disabled background refresh in settings.
- The app is running on Simulator which doesn’t support background processing.
- The extension either hasn’t set [`RequestsOpenAccess`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/RequestsOpenAccess) to `YES` in [`The Info.plist File`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22), or the user hasn’t granted open access.

## See Also

- [BGTaskScheduler.Error.Code](bgtaskscheduler/error/code.md)
  An enumeration of the task scheduling errors.
- [static var notPermitted: BGTaskScheduler.Error.Code](bgtaskscheduler/error/notpermitted.md)
  A task scheduling error indicating the app isn’t permitted to launch the task.
- [static var tooManyPendingTaskRequests: BGTaskScheduler.Error.Code](bgtaskscheduler/error/toomanypendingtaskrequests.md)
  A task scheduling error indicating that there are too many pending tasks of the type requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/unavailable)*