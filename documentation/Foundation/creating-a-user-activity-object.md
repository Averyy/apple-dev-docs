# Creating a user activity object

**Framework**: Foundation

Identify key user interactions and include the information to restore them later.

#### Overview

Create [`NSUserActivity`](nsuseractivity.md) objects at key moments that a person might want to continue later or on another device, and register them with the system. For example, you might create a user activity object when a person opens a web page, plays a song, or performs a significant task in your app. You can also use them to provide better Spotlight search results. User activity objects, however, aren’t intended as a way to track every task in your app, or for small edits or minor changes.

When you create an [`NSUserActivity`](nsuseractivity.md) object, you specify a string that identifies the type of the activity. Activity type strings are typically in reverse-DNS format. For example, when a person opens a web page, you might specify an activity string such as `com.myCompany.myApp.OpenWebPage`. Declare the activity types that your app supports by including the [`NSUserActivityTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserActivityTypes) key in its [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List) file. The system uses the information in that key to determine whether your app is capable of handling a given user activity object.

##### Define Activities

When defining a user activity object, do the following:

1. Create and initialize the user activity object with an appropriate activity type. (You define the activity types your app supports.)
2. Set the [`title`](nsuseractivity/title.md) of the user activity object.
3. Configure the tasks for which the object is eligible by enabling one or more of the following properties: [`isEligibleForHandoff`](nsuseractivity/iseligibleforhandoff.md), [`isEligibleForSearch`](nsuseractivity/iseligibleforsearch.md), and [`isEligibleForPublicIndexing`](nsuseractivity/iseligibleforpublicindexing.md).
4. Configure the properties of this object that relate to a person’s current activity.
5. For user activity objects configured for search or public indexing, configure the [`contentAttributeSet`](nsuseractivity/contentattributeset.md), [`keywords`](nsuseractivity/keywords.md), or [`webpageURL`](nsuseractivity/webpageurl.md) properties so that Spotlight can index the object.
6. Call the [`becomeCurrent()`](nsuseractivity/becomecurrent().md) method to register the user activity object with the system.

##### Associate Activity Identifiers with Your Apps

The system associates user activity objects from your app with your developer Team ID. When continuing an activity, the system looks for an app that supports the given activity type and has the same developer Team ID as the activity’s source app. Tying activity objects to your developer Team ID ensures that a competitor’s app can’t intercept the activities you create. To associate your Team ID with your apps, distribute your apps through the App Store or sign them with your developer ID.

## See Also

- [init(activityType: String)](nsuseractivity/init(activitytype:).md)
  Creates a user activity object with the specified type.
- [convenience init()](nsuseractivity/init.md)
  Creates a user activity object using the first activity type declared in the app’s information property list file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/creating-a-user-activity-object)*