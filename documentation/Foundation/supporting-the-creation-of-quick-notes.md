# Supporting the creation of Quick Notes

**Framework**: Foundation

Support the creation of notes that include your app’s content.

#### Overview

People use Quick Notes on macOS and iOS to quickly add app-specific content to the Notes app. When someone activates Quick Notes from your app, the system displays an interface for creating the note content. If your app has a properly configured activity, the system also includes a link to that activity in the note. Someone viewing the note later can use that link to open your app and perform the activity. For example, someone activating Quick Note while viewing a photo an use the link to view that photo again.

##### Configure a User Activity Object with Your Content

Apps can provide the initial content for a Quick Note using an [`NSUserActivity`](nsuseractivity.md) object. When your app has a current activity object, the Quick Note system adds a link to the activity in the new note. However, the system creates this link only if your activity object provides a value in its [`webpageURL`](nsuseractivity/webpageurl.md), [`persistentIdentifier`](nsuseractivity/persistentidentifier.md), or [`targetContentIdentifier`](nsuseractivity/targetcontentidentifier.md) property. The system relies on these properties because they typically contain information that persists for a long time:

- The [`webpageURL`](nsuseractivity/webpageurl.md) property contains a URL with the `https:` scheme.
- The [`persistentIdentifier`](nsuseractivity/persistentidentifier.md) property contains a unique identifier for the activity object.
- The [`targetContentIdentifier`](nsuseractivity/targetcontentidentifier.md) property contains a unique identifier for part of your app’s content.

The URL or identifier you provide needs to remain stable and consistent so you can use it to perform the activity again on different devices. People can view notes on any of their devices, and they can share notes with other people. If you use a URL, consider using universal links to provide a consistent location for items in your app.  If you use an activity or content identifier, make sure the identifier is unique within your app but the same on all of the person’s devices. If the content’s location changes for any reason, handle the change gracefully by navigating automatically to the new location. If the content is no longer available, display a message in your app’s interface to inform the person that the content is no longer available.

In addition to providing stable identifiers for your content, provide a descriptive noun phrase in the [`title`](nsuseractivity/title.md) property of your activity object. When displaying the note, the Notes app uses the text in that property as part of the link to your item. Provide a noun phrase that conveys helpful informaton about the content. For example, a photo app might set the title of a photo-viewing activity to something like “Photo taken on December 28, 2025”.

##### Keep Your Activity Objects Up to Date

To make your content available to Quick Notes, call the [`becomeCurrent()`](nsuseractivity/becomecurrent().md) method of your activity object. The Quick Notes system pulls content only from your app’s current activity object. You can change this object at any time to reflect changes in your app’s interface. For example, if someone is browsing a catalog of items, change the activity object each time they focus on a different item. If your app isn’t reflecting any content that is suitable for inclusion in a note, you can clear the current activity object by calling its [`resignCurrent()`](nsuseractivity/resigncurrent().md) method.

## See Also

- [Creating a user activity object](creating-a-user-activity-object.md)
  Identify key user interactions and include the information to restore them later.
- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)
  Create, send, and receive user activities directly.
- [Continuing User Activities with Handoff](continuing-user-activities-with-handoff.md)
  Define and manage which of your app’s activities can be continued between devices.
- [Increasing App Usage with Suggestions Based on User Activities](increasing-app-usage-with-suggestions-based-on-user-activities.md)
  Provide a continuous user experience by capturing information from your app and displaying this information as proactive suggestions across the system.
- [class NSUserActivity](nsuseractivity.md)
  A representation of the state of your app at a moment in time.
- [protocol NSUserActivityDelegate](nsuseractivitydelegate.md)
  The interface through which a user activity instance notifies its delegate of updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/supporting-the-creation-of-quick-notes)*