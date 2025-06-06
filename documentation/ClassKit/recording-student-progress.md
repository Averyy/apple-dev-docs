# Recording student progress

**Framework**: ClassKit

Create an activity to record student progress through an assignment.

#### Overview

While contexts describe what tasks a teacher can assign in your app, such as reading a chapter in a book, activities report on student progress as they work through those tasks. An activity measures duration—the length of time a user spends on a task—based on when you tell the activity to start and stop. It also records how far a user has progressed through the task as a percentage of completion, based on updates you supply. It’s up to you to define progress depending on the particulars of your app.

##### Retrieve the Context

An activity is always tied to a particular context. In fact, you create a new [`CLSActivity`](clsactivity.md) instance by asking the context whose task you are measuring to do so on your behalf. The newly created activity becomes the context’s current activity, which you access later through the context’s [`currentActivity`](clscontext/currentactivity.md) property.

Begin by retrieving the relevant context with a call to the [`descendant(matchingIdentifierPath:completion:)`](clscontext/descendant(matchingidentifierpath:completion:).md) method. You’ll operate on the context from within the completion handler.

```swift
let identifierPath = <# The path to some context #>

CLSDataStore.shared.mainAppContext.descendant(matchingIdentifierPath: identifierPath) { context, _ in
    // Operate on the context here...
}
```

Look up a context like this every time you need it, rather than storing a reference to it. The underlying instance may change from time to time as a result of network synchronization. If you always look up the context, you can be sure that you’re working with the right instance.

##### Create and Start an Activity

From within the [`descendant(matchingIdentifierPath:completion:)`](clscontext/descendant(matchingidentifierpath:completion:).md) method’s completion handler, activate the context, and then create the activity. Typically, you’ll also start the activity right after creating it:

```swift
// You typically activate the context when you start an activity.
context?.becomeActive()
    
// Create and start a new activity.
context?.createNewActivity().start()
```

Then, while still inside the completion handler, save the changes to record them in the framework’s database and share them with the teacher:

```swift
CLSDataStore.shared.save { error in
    // Handle the error
}
```

For privacy reasons, only users logged in with managed student accounts who have received an assignment for a given context can save activities in that context to the database. This operation silently fails for other users (including both teachers and unmanaged users, and even students who have not yet received an assignment).

When you create and start an activity as shown above, you indicate that the user has begun an attempt at the task represented by the given context. This code runs each time a student attempts a task. For example, within the context of a book chapter, the app may create a reading activity that measures progress through the material. If the user abandons the task, then the next time they attempt it, create a new activity to record the new attempt as a new task. What it means to abandon a task (as opposed to pausing it) depends on your app’s usage model.

> **Note**:  In some cases, the user might only pause the task—for example, to review something that appears in an earlier chapter. In that case, when the user resumes the current task, don’t create a new activity. Instead, restart the existing one. See [`Pause an activity when the user interrupts a task briefly`](recording-student-progress#Pause-an-activity-when-the-user-interrupts-a-task-briefly.md) for more details.

 In some cases, the user might only pause the task—for example, to review something that appears in an earlier chapter. In that case, when the user resumes the current task, don’t create a new activity. Instead, restart the existing one. See [`Pause an activity when the user interrupts a task briefly`](recording-student-progress#Pause-an-activity-when-the-user-interrupts-a-task-briefly.md) for more details.

##### Update Progress Periodically

An activity measures duration as the time interval between when you call its [`start()`](clsactivity/start().md) and [`stop()`](clsactivity/stop().md) methods. But the concept of progress depends entirely on what your app does, so you supply additional information in the form of progress updates.

To provide updates, you periodically call the activity’s [`addProgressRange(fromStart:toEnd:)`](clsactivity/addprogressrange(fromstart:toend:).md) method at intervals that make sense for your app. For a book reader, you might define progress in terms of how many pages the user has read, calling for an update every time the user turns a page:

```swift
// Progress defined as the current page as a fraction of the total pages.
let progress = Double(max(0, min(1, currentPage / totalPages)))

CLSDataStore.shared.mainAppContext.descendant(matchingIdentifierPath: identifierPath) { context, _ in

    // Ensure we have a started activity.
    guard let activity = context?.currentActivity,
        activity.isStarted else { return }

    activity.addProgressRange(fromStart: 0, toEnd: progress)
}
```

Another app that presents content in a scroll view might define progress as the current position relative to the bottom of the view, to be updated in the [`scrollViewDidScroll(_:)`](https://developer.apple.com/documentation/UIKit/UIScrollViewDelegate/scrollViewDidScroll(_:)) callback of the [`UIScrollViewDelegate`](https://developer.apple.com/documentation/UIKit/UIScrollViewDelegate) protocol:

```swift
let position = scrollView.contentOffset.y + scrollView.frame.size.height
let total = scrollView.contentSize.height
let progress = Double(max(0, min(1, position / total)))
```

You can call the data store’s [`save(completion:)`](clsdatastore/save(completion:).md) method every time you add a progress update to ensure your changes are reported to the teacher. And for certain long-running activities with infrequent updates, this might make sense. But for performance reasons, in most cases it’s best to wait until the activity ends, after which you save all the updates in one shot. This is particularly true if you generate frequent progress updates, as you might from the [`scrollViewDidScroll(_:)`](https://developer.apple.com/documentation/UIKit/UIScrollViewDelegate/scrollViewDidScroll(_:)) method.

##### Stop an Activity When the User Ends the Attempt

When the user aborts or completes a task, for example by navigating away from the chapter they’ve been reading, or by answering all the questions on a quiz, mark the activity as stopped:

```swift
CLSDataStore.shared.mainAppContext.descendant(matchingIdentifierPath: identifierPath) { context, _ in
    guard let activity = context?.currentActivity else { return }

    activity.stop()

    // Typically, you deactive the context at this point as well.
    context?.resignActive()

    CLSDataStore.shared.save { error in
        // Handle the error
    }
}
```

Call the data store’s [`save(completion:)`](clsdatastore/save(completion:).md) method at this point to ensure your accumulated progress updates and state changes synchronize to the network.

> **Note**:  Because data must be synchronized across the network, expect some delay in a production environment between when you record results in your app, and when the teacher actually sees the results in Schoolwork.

 Because data must be synchronized across the network, expect some delay in a production environment between when you record results in your app, and when the teacher actually sees the results in Schoolwork.

##### Pause an Activity When the User Interrupts a Task Briefly

You can also use the [`stop()`](clsactivity/stop().md) method to pause an activity. For example, if you’re measuring progress through a game and the user taps the pause button, you may want to tell the corresponding activity to stop. Resume a paused activity with another call to the [`start()`](clsactivity/start().md) method. You can stop and start repeatedly, but once you create a new activity in a given context using a call to the [`createNewActivity()`](clscontext/createnewactivity().md) method, the previous activity becomes final, and can no longer be accessed from your app.

Whether pausing makes sense depends on the particulars of your app. Typically, you pause when the user interrupts a task with the expectation of continuing after a brief delay, but create a new activity when the user makes a fresh attempt at a task.

> **Note**:  The framework automatically pauses a running activity if your app enters the background, and resumes the same activity when your app returns to the foreground.

 The framework automatically pauses a running activity if your app enters the background, and resumes the same activity when your app returns to the foreground.

##### Optionally Mark an Assignment As Done

For each assignment, the Schoolwork app displays a per-student Done indicator to teachers. Students self-report this status by tapping a button in their own instance of Schoolwork. To do the same thing programmatically from your app, call the [`completeAllAssignedActivities(matching:)`](clsdatastore/completeallassignedactivities(matching:).md) method.

```swift
CLSDataStore.shared.completeAllAssignedActivities(matching: ["chapter-1", "quiz-1"])
```

You can do this automatically for tasks that have a well-defined end point, like a timed quiz. After time runs out, the student isn’t allowed to make any further changes, so your app marks the task as done. For a task without a strict time limit, but that ends with a submission of an artifact, like a drawing or a poem, you can call the completion method as part of the submission flow. If you already have a done button of some kind in your interface, you can call the method from that button’s handler.

> **Note**:  A task’s progress isn’t connected to its Done indicator. For example, setting the [`progress`](clsactivity/progress.md) property to 1 doesn’t automatically force the Done indicator to true. Use progress to give teachers an idea of which parts of a task the student has attempted. Use the Done indicator to indicate that the student plans no further action for the activity.

 A task’s progress isn’t connected to its Done indicator. For example, setting the [`progress`](clsactivity/progress.md) property to 1 doesn’t automatically force the Done indicator to true. Use progress to give teachers an idea of which parts of a task the student has attempted. Use the Done indicator to indicate that the student plans no further action for the activity.

##### Record Progress at Multiple Levels of Hierarchy

If you group contexts into a hierarchy, you might want to record progress at multiple levels of the hierarchy concurrently. This lets you measure progress through a small, indivisible task, like reading a chapter in a book, while simultaneously recording progress through the larger, enclosing task, like reading the whole book in which that chapter appears. Do this by running more than one activity at a time.

For example, when the user begins reading Chapter 1 of a book, you start an activity in the Chapter 1 context and another in the book context. You set progress independently for each, while each maintains its own duration measurement. When the user begins reading Chapter 2, you stop the Chapter 1 activity and then create and start a new activity in Chapter 2. The book activity continues running through the chapter change.

So the duration of time spent working on the book automatically becomes the cumulative duration of reading all the chapters. On the other hand, it’s up to you to report progress in the book context in a way that’s meaningful. For instance, if the chapters are all about the same length, you might set book progress simply as the fraction of the number of chapters read. But if they aren’t, you might need to account for the relative size of each chapter in setting book progress.

You can nest activities like this to the full depth of your context hierarchy. For example, the chapters might each contain multiple sections, in which case you run the book, a chapter, and a particular section activity all at the same time.

When you do run more than one activity at a time, the data store’s [`runningActivity`](clsdatastore/runningactivity.md) property reports only the most recently started activity.

> ❗ **Important**:  Recording at multiple levels of hierarchy is available in iOS 11.4 or later. In iOS 11.3, you can only run one activity at a time, so starting an activity when one is already running implicitly forces the running one to stop.

 Recording at multiple levels of hierarchy is available in iOS 11.4 or later. In iOS 11.3, you can only run one activity at a time, so starting an activity when one is already running implicitly forces the running one to stop.

## See Also

- [class CLSActivity](clsactivity.md)
  A representation of user interaction with a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/recording-student-progress)*