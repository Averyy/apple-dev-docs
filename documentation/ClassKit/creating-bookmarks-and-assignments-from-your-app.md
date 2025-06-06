# Creating bookmarks and assignments from your app

**Framework**: ClassKit

Make it easier for teachers to find and assign your content.

#### Overview

Once you adopt ClassKit and declare your app’s assignable content, teachers can use Apple’s Schoolwork app to assign your content to students. They do this by creating a new Assignment in Schoolwork.

![Screenshot showing the New Assignment view in the Schoolwork app, highlighting the button you tap to open the view, and the button within the view that you tap to add activities.](https://docs-assets.developer.apple.com/published/3714bcb1ab602692f6e0d3a13480fea8/media-3119327%402x.png)

From the New Assignment view, the teacher taps Add Activities to choose items to add to the Assignment. The popover that appears has an App Activities option that provides access to the content in apps like yours. The popover also has options for adding other supporting material to the assignment, like files, links, photos, or videos.

![Screenshot showing the popover that appears when you tap the Add Activities button in a Create new Assignment view.](https://docs-assets.developer.apple.com/published/03c991d2438f1db4c00f33bc0db7bfb1/media-3016828%402x.png)

You can make it easier for teachers to find your app’s content in Schoolwork by letting them bookmark it as they encounter the content in your app. The bookmarks they create from within your app appear under the Bookmarks entry in the Add Activity popover shown above.

To enable bookmarks, you provide a ClassKit context ([`CLSContext`](clscontext.md)) to an activity view controller as described below. When you do this, Schoolwork offers a bookmark creation action extension in the activity view. Inside the same activity view, Schoolwork also offers a share extension that provides a shortcut to Assignment creation. This allows teachers to create assignments without leaving your app.

##### Associate Action Buttons with Content

To provide a point from which to launch an activity view in your app, add one or more [`UIBarButtonItem.SystemItem.action`](https://developer.apple.com/documentation/UIKit/UIBarButtonItem/SystemItem/action) buttons to your interface. Users know that tapping an action button typically reveals a modal activity view with share and action extensions that are relevant to the current task, as described in [`Activity Views`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/views/activity-views/). Add action buttons to your app’s UI in places that correspond to activities that a teacher might want to assign right away or to bookmark for later assignment.

![Screenshot showing an action button that appears in the navigation bar in the Great Plays sample app.](https://docs-assets.developer.apple.com/published/e764a4625e9d435042806818f68e780c/media-3021754%402x.png)

When deciding where to place action buttons in your UI, choose locations that clearly correspond to an assignable task. For example, in a play reader like the Great Plays sample app (see [`Incorporating ClassKit into an Educational App`](incorporating-classkit-into-an-educational-app.md)), users would expect an action button that appears with a play’s table of contents, as shown in the figure above, to apply to the play as a whole. On the other hand, an action button that appears as part of a quiz should apply specifically to that quiz.

##### Initialize and Present an Activity View

For each action button you add to your UI, add a corresponding method that’s called when the user taps the button. Use this method to initialize and present an instance of a [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController). Initialize the activity view with the [`CLSContext`](clscontext.md) corresponding to the assignable task the user would expect, given the state of your app at the time. For example, if the user taps the action button on the table of contents shown in the previous section, provide the play context as the activity item:

```swift
 let activityView = UIActivityViewController(activityItems: [playContext, self],
                                                        applicationActivities: nil)
```

Then present the activity view. On iPad, you present an activity view as a popover, typically originating from the tapped action button.

```swift
 activityView.modalPresentationStyle = .popover
 activityView.popoverPresentationController?.permittedArrowDirections = .any
 activityView.popoverPresentationController?.barButtonItem = actionButtonItem
 activityView.excludedActivityTypes = [ UIActivity.ActivityType.message, UIActivity.ActivityType.mail]
 self.present(activityView, animated: true)
```

##### Update Activity View Metadata

To provide context to the user about the information in the activity view, add the meta data describing the information they’re sharing by conforming your view controller to the [`UIActivityItemSource`](https://developer.apple.com/documentation/UIKit/UIActivityItemSource) protocol.

```swift
import LinkPresentation

class ActsTableViewController: UITableViewController, UIActivityItemSource 
```

The [`activityViewControllerLinkMetadata(_:)`](https://developer.apple.com/documentation/UIKit/UIActivityItemSource/activityViewControllerLinkMetadata(_:)) delegate method provides the [`LPLinkMetadata`](https://developer.apple.com/documentation/LinkPresentation/LPLinkMetadata) to the activity view for the icon and title. This provides context to the user for the shared information. In the below example, the Hamlet Play title and icon indicate the context of the information shared with Schoolwork.

```swift
func activityViewControllerLinkMetadata(_ activityViewController: UIActivityViewController) -> LPLinkMetadata? {
        guard let image = UIImage(named: "IconImage") else {return nil}
        let imageProvider = NSItemProvider(object: image)
        let metadata = LPLinkMetadata()
        metadata.iconProvider = imageProvider
        if let title = play?.title {
            metadata.title = "\(title) Play"
        }
        return metadata
}
```

The system recognizes ClassKit context activity items as relevant to the Schoolwork app and offers the two extensions Schoolwork provides in the activity view.

![Screenshot showing the activity view that appears when you tap the action button in the Great Plays sample code app, highlighting the two extensions provided by Schoolwork.](https://docs-assets.developer.apple.com/published/49022f08c77d3ed4fcd561f3feee96dc/media-4305224%402x.png)

If the user taps the first of these extensions, titled Schoolwork, Schoolwork initiates the New Assignment view with the given context right inside your app. The context is already populated in the Assignment:

![Screenshot showing the New Assignment view that appears inside your app when the user taps the Schoolwork icon in the activity view.](https://docs-assets.developer.apple.com/published/7c430d642a080cabcf4c925e41a46868/media-4305226%402x.png)

If the user taps the second share extension icon, titled Save to Schoolwork, Schoolwork creates a bookmark of the corresponding context without any additional UI.

![Screenshot showing Add to Bookmarks view that appears in your app when the users taps on Save To Schoolwork icon in an activity view.](https://docs-assets.developer.apple.com/published/ecabdae1458ac36dbc602810840b6b11/media-4305228%402x.png)

The teacher can later find the bookmarked content in Schoolwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/creating-bookmarks-and-assignments-from-your-app)*