# notPermitted

**Framework**: Background Tasks  
**Kind**: property

A task scheduling error indicating the app isn’t permitted to launch the task.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static var notPermitted: BGTaskScheduler.Error.Code { get }
```

#### Discussion

There are two causes for this error:

- The app doesn’t set the appropriate mode in the [`UIBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes) array.
- The task identifier of the submitted task wasn’t in the [`BGTaskSchedulerPermittedIdentifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BGTaskSchedulerPermittedIdentifiers) array in [`The Info.plist File`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22).

## See Also

- [BGTaskScheduler.Error.Code](bgtaskscheduler/error/code.md)
  An enumeration of the task scheduling errors.
- [static var tooManyPendingTaskRequests: BGTaskScheduler.Error.Code](bgtaskscheduler/error/toomanypendingtaskrequests.md)
  A task scheduling error indicating that there are too many pending tasks of the type requested.
- [static var unavailable: BGTaskScheduler.Error.Code](bgtaskscheduler/error/unavailable.md)
  A task scheduling error indicating that the app or extension can’t schedule background work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/error/notpermitted)*