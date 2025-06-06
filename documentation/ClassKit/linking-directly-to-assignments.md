# Linking directly to assignments

**Framework**: Classkit

Make it easy for teachers to guide students to specific content.

#### Overview

ClassKit lets you deep link to assignable content so that when a student taps an assigned activity in the Schoolwork app, they go directly to the corresponding content in your app. This helps teachers guide students to an activity.

You can implement this kind of linking through URL requests or user activity. Your choice may depend on what your app already does.

> **Note**:  If you change the structure of your context hierarchy in an app update, be sure to account for the old structure in your link handling so that legacy links continue to produce meaningful behavior.

##### Reuse Existing Url Support

If your app supports custom URLs to provide deep links to specific content—for example, because you already support linking from push notifications—you can easily reuse that infrastructure with your contexts. Briefly, supporting custom URLs means that you’ve defined a URL type in your app’s `Info.plist` file with a custom URL scheme, and have implemented the [`application(_:open:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:open:options:)) method in your app delegate to handle incoming requests with this scheme.

To reuse this scheme with ClassKit, when you create contexts, assign the corresponding URL of each context’s [`universalLinkURL`](clscontext/universallinkurl.md) property. The Schoolwork app uses one of these URLs to issue a request to your app when the student taps an assignment in Schoolwork. The request activates your app and gives you the chance to load the appropriate view.

As an example, consider a play reader that provides links to individual scenes with a URL of the form `play-reader://{play}/{act}/{scene}`. When creating the context for Hamlet, Act 3, Scene 1, you simply include the assignment:

```swift
// Act 3, Scene 1: To be, or not to be...
context.universalLinkURL = URL(string: "play-reader://Hamlet/3/1")
```

You add similar URLs to each assignable context, including parent contexts, such as the one for the play as a whole (`play-reader://Hamlet`). Support a link to any task that the teacher might assign as a unit (which typically means each context that you define).

If you support universal links, as described in [`Support Universal Links`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html), you can assign those URLs to the [`universalLinkURL`](clscontext/universallinkurl.md) property instead.

##### Handle Incoming User Activity

If you don’t already handle custom URL requests or universal links in your app, you can alternatively support deep links by handling incoming user activities, represented by instances of the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) class. You do this by implementing the [`application(_:continue:restorationHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:continue:restorationHandler:)) method in your app delegate, much like you would to support handoff. See [`Index Activities and Navigation Points`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/Activities.html) for a general discussion.

ClassKit extends the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) class with two properties that help you manage the activity in your handler. First, it adds the [`isClassKitDeepLink`](https://developer.apple.com/documentation/foundation/nsuseractivity/2953056-isclasskitdeeplink) Boolean to indicate if the user activity is related to ClassKit. Second, it provides the [`contextIdentifierPath`](https://developer.apple.com/documentation/foundation/nsuseractivity/2866826-contextidentifierpath) array to indicate the context that the user selected, which you use to decide what view to show.

```swift
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([Any]?) -> Void) -> Bool {

    // Get the identifier path
    if userActivity.isClassKitDeepLink,
        let identifierPath = userActivity.contextIdentifierPath {

        // Navigate to the given location in the view hierarchy
        // ...

        // Indicate that we handled the continuation
        return true
    }

    // We did not handle the continuation
    return false
}
```

Supporting deep links this way is actually simpler than using custom URL requests, because you don’t have to define a custom URL scheme, and you don’t have to set any properties on the context itself. As long as a context’s [`universalLinkURL`](clscontext/universallinkurl.md) is `nil`—which it is by default—then instead of generating a URL request, the Schoolwork app automatically sends your app an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) instance when the student taps an assigned activity.

## See Also

- [var universalLinkURL: URL?](clscontext/universallinkurl.md)
  A URL that leads to the content in your app associated with the current context.
- [var isClassKitDeepLink: Bool](../foundation/nsuseractivity/2953056-isclasskitdeeplink.md)
  A Boolean value that indicates whether a user activity represents a ClassKit context.
- [var contextIdentifierPath: [String]?](../foundation/nsuseractivity/2866826-contextidentifierpath.md)
  The identifier path associated with a user activity generated by an app that adopts ClassKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ClassKit/linking-directly-to-assignments)*