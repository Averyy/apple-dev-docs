# fetchActivity(for:completion:)

**Framework**: ClassKit  
**Kind**: method

Fetches an activity for a given document so you can record progress on the associated task.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func fetchActivity(for url: URL) async throws -> CLSActivity
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func fetchActivity(for url: URL) async throws -> CLSActivity
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to get a [`CLSActivity`](clsactivity.md) instance for a task that’s associated with a particular document, as specified by its file URL. If the activity doesn’t exist, ClassKit creates one for you. You can use the activity instance provided in the completion handler to start recording progress:

```swift
CLSDataStore.shared.fetchActivity(for: url) { currentActivity, error in
    guard let activity = currentActivity else { return }

    // Start tracking time.
    activity.start()

    CLSDataStore.shared.save { error in
        // Handle errors.
    }
}
```

ClassKit provides activities for documents that a teacher attaches to an assignment in the Schoolwork app. When the student receives the assignment and opens the attached document in your app, you can use the file URL of the document to fetch the associated activity.

Don’t store a reference to the activity in your app. Always ask ClassKit for the activity when you need it. For example, to record progress and stop tracking time, ask for the activity again:

```swift
CLSDataStore.shared.fetchActivity(for: url) { currentActivity, error in
    guard let activity = currentActivity else { return }

    // Report the number of pages read so far.
    let pageCount = activity.primaryActivityItem as? CLSQuantityItem
        ?? CLSQuantityItem(identifier: "page_count", title: "Page Count")
    pageCount.quantity = 6 
    activity.primaryActivityItem = pageCount

    // Report progress through the task.
    activity.progress = 0.75

    // Stop tracking time, always done last.
    activity.stop()

    CLSDataStore.shared.save { error in
        // Handle errors.
    }
}
```

As the example above shows, always call the [`stop()`](clsactivity/stop().md) method last, after setting progress or adding activity items.

To determine the file permissions of a document attached to an assignment in the Schoolwork app, open the file with [`UIApplication.OpenURLOptionsKey`](https://developer.apple.com/documentation/UIKit/UIApplication/OpenURLOptionsKey) set to true. You then check the URL resource key [`ubiquitousSharedItemCurrentUserPermissionsKey`](https://developer.apple.com/documentation/Foundation/URLResourceKey/ubiquitousSharedItemCurrentUserPermissionsKey). The resource key value, [`URLUbiquitousSharedItemPermissions`](https://developer.apple.com/documentation/Foundation/URLUbiquitousSharedItemPermissions), indicates whether the file has read and write or read-only permissions.

Use these permissions to determine whether your UI needs to be editable or view only.

## Parameters

- `url`: The file URL of the document for which you want to fetch a   instance. A teacher must have previously attached the document to an assignment in the Schoolwork app.
- `completion`: A handler that the method calls to return an activity if possible, and an optional error that describes the reason for a failure.

## See Also

- [var mainAppContext: CLSContext](clsdatastore/mainappcontext.md)
  The app’s top-level context.
- [var activeContext: CLSContext?](clsdatastore/activecontext.md)
  The currently active context.
- [var runningActivity: CLSActivity?](clsdatastore/runningactivity.md)
  The currently running activity within the currently active context.
- [func completeAllAssignedActivities(matching: [String])](clsdatastore/completeallassignedactivities(matching:).md)
  Marks all of the assigned and active activities for the given context path as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/fetchactivity(for:completion:))*