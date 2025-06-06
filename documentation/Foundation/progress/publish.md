# publish()

**Framework**: Foundation  
**Kind**: method

Publishes the progress object for other processes to observe it.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func publish()
```

#### Discussion

Entries in the user info dictionary determine whether another process can discover the progress object to observe it, and how it does that. For example, a [`fileURLKey`](progressuserinfokey/fileurlkey.md) entry makes a progress object discoverable by corresponding invokers of [`addSubscriber(forFileURL:withPublishingHandler:)`](progress/addsubscriber(forfileurl:withpublishinghandler:).md). The system constrains access to the published progress URL with your app sandbox. If you can’t see the file due to the app’s sandbox restrictions, you can’t observe the progress on it.

When you make a progress object observable by other processes, you must ensure that at least [`localizedDescription`](progress/localizeddescription.md), [`isIndeterminate`](progress/isindeterminate.md), and [`fractionCompleted`](progress/fractioncompleted.md) always work when you send proxies of your progress object in other processes. You make [`isIndeterminate`](progress/isindeterminate.md) and [`fractionCompleted`](progress/fractioncompleted.md) work by accurately setting the total and completed unit counts of the progress. You make [`localizedDescription`](progress/localizeddescription.md) work by setting the value of the kind property to something valid, like [`file`](progresskind/file.md), and then fulfilling the requirements for that kind of progress.

You can instead set the value of [`localizedDescription`](progress/localizeddescription.md) directly, but that’s not perfectly reliable because other processes might be using a different localization than yours.

You can publish an instance of [`Progress`](progress.md) one time only.

## See Also

- [func unpublish()](progress/unpublish.md)
  Removes a progress object from publication, making it unobservable by other processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progress/publish())*