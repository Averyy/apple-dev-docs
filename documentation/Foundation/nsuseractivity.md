# NSUserActivity

**Framework**: Foundation  
**Kind**: class

A representation of the state of your app at a moment in time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSUserActivity
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)
- [Creating a user activity object](creating-a-user-activity-object.md)
- [Supporting the creation of Quick Notes](supporting-the-creation-of-quick-notes.md)

#### Overview

The `NSUserActivity` class is a lightweight type that encapsulates the state of an activity you perform in your app. When someone performs a relevant action in your app, create an instance of this class to capture that activity. The system uses the user activity objects you provide to facilitiate features like Handoff and Quick Notes. For example, Handoff sends your user activity object to the person’s other devices so your app can replicate the activity there.

Create an `NSUserActivity` object and initialize it with the [`activityType`](nsuseractivity/activitytype.md) string for that particular activity. You define the activity types your app supports and create reverse-DNS strings for each one in your code. Typically, activities correspond to actions that a person takes in your app’s interface. For example, you might create one activity for viewing items and a separate activity for completing edits to an item.

Add enough information to your user activity object to recreate the activity in your app at a later time. If your activity has an associated URL, place it in the [`webpageURL`](nsuseractivity/webpageurl.md) property. If your user activity object refers to a specific piece of your app’s content, specify the identifier for that content using the [`targetContentIdentifier`](nsuseractivity/targetcontentidentifier.md), [`appEntityIdentifier`](nsuseractivity/appentityidentifier.md), or [`externalMediaContentIdentifier`](nsuseractivity/externalmediacontentidentifier.md) property. Place any other app-specific data in the [`userInfo`](nsuseractivity/userinfo.md) dictionary. Provide a human-readable [`title`](nsuseractivity/title.md) for the activity, and enable the features your activity supports such as Handoff and Spotlight indexing. Fill in other properties as needed for your specific activity type.

Create user activity objects in response to specific interactions with your app’s interface. When someone performs a significant task in your interface, create a user activity object and call its [`becomeCurrent()`](nsuseractivity/becomecurrent().md) method to make it your app’s current activity. For example, you might do this when someone opens a new document in your app. Handoff and other features operate on the current activity and use it as context for their behavior. In the case of opening a document, Handoff indicates that the person can open that document on their other devices. When the person stops the activity in your interface, or the activity is no longer relevant, call the [`resignCurrent()`](nsuseractivity/resigncurrent().md) or [`invalidate()`](nsuseractivity/invalidate().md) method, or create a new user activity object and make it the current one.

For features like Handoff to work, the system needs to know which types of activities it can deliver to your app. To specify the activity types you support, add the [`NSUserActivityTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSUserActivityTypes) key to your app’s `Info.plist` file. Configure this key using the Info tab of your Xcode project, and set its value to an array of strings. For each string, specify one of the activity types you use to create your `NSUserActivity` objects. You can specify all of your app’s activity types or only a subset.

System features like Siri and Apple Intelligence use contextual information from your app’s interface to improve their responses. Assign [`AppEntity`](https://developer.apple.com/documentation/AppIntents/AppEntity) types directly to your views when possible, but you can also assign a user activity object to your view as needed. In SwiftUI, create and configure this user activity object using the [`userActivity(_:element:_:)`](https://developer.apple.com/documentation/SwiftUI/View/userActivity(_:element:_:)) modifier. In UIKit and AppKit, assign the user activity object to the [`userActivity`](https://developer.apple.com/documentation/UIKit/UIResponder/userActivity) property of a responder object in your interface. Use the [`appEntityIdentifier`](nsuseractivity/appentityidentifier.md) property of your user activity object to provide the entity for your view.

## Topics

### Creating a user activity object
- [init(activityType: String)](nsuseractivity/init(activitytype:).md)
  Creates a user activity object with the specified type.
### Monitoring activity-related behaviors
- [var delegate: (any NSUserActivityDelegate)?](nsuseractivity/delegate.md)
  The user activity object’s delegate.
- [protocol NSUserActivityDelegate](nsuseractivitydelegate.md)
  The interface through which a user activity instance notifies its delegate of updates.
### Describing the activity
- [var activityType: String](nsuseractivity/activitytype.md)
  The user activity object’s activity type.
- [var title: String?](nsuseractivity/title.md)
  An optional, user-visible title for this activity, such as a document name or web page title.
- [var keywords: Set<String>](nsuseractivity/keywords.md)
  A set of localized keywords that can help users find the activity in search results.
- [var persistentIdentifier: NSUserActivityPersistentIdentifier?](nsuseractivity/persistentidentifier.md)
  A unique and persistent value you use to identify the activity.
- [typealias NSUserActivityPersistentIdentifier](nsuseractivitypersistentidentifier.md)
  The type that defines a persistent identifier value for an activity.
- [var contentAttributeSet: CSSearchableItemAttributeSet?](nsuseractivity/contentattributeset.md)
  A set of properties that describe the activity.
### Enabling system behaviors
- [var isEligibleForHandoff: Bool](nsuseractivity/iseligibleforhandoff.md)
  A Boolean value that indicates whether the activity can continue on another device using Handoff.
- [var isEligibleForSearch: Bool](nsuseractivity/iseligibleforsearch.md)
  A Boolean value that indicates whether to add the activity to the on-device index.
- [var isEligibleForPublicIndexing: Bool](nsuseractivity/iseligibleforpublicindexing.md)
  A Boolean value that indicates whether the activity is publicly accessible by all iOS users.
- [var isEligibleForPrediction: Bool](nsuseractivity/iseligibleforprediction.md)
  A Boolean value that determines whether Siri can suggest the activity as a shortcut.
- [var expirationDate: Date?](nsuseractivity/expirationdate.md)
  The date after which the activity is no longer eligible for Handoff or indexing.
### Specifying app identifiers
- [var appEntityIdentifier: EntityIdentifier?](nsuseractivity/appentityidentifier.md)
  The identifier of an app entity that you associate with the user activity.
- [var targetContentIdentifier: String?](nsuseractivity/targetcontentidentifier.md)
  A string that identifies the user activity’s content.
- [var externalMediaContentIdentifier: String?](nsuseractivity/externalmediacontentidentifier.md)
  A unique identifier from the app’s media content catalog for the currently displayed media item.
### Browsing the web
- [var webpageURL: URL?](nsuseractivity/webpageurl.md)
  The URL of the webpage to load in a browser to continue the activity.
- [var referrerURL: URL?](nsuseractivity/referrerurl.md)
  The URL of the webpage that linked to the webpage URL.
- [let NSUserActivityTypeBrowsingWeb: String](nsuseractivitytypebrowsingweb.md)
  An activity that continues from Handoff or a universal link.
- [let TVUserActivityTypeBrowsingChannelGuide: String](../TVServices/TVUserActivityTypeBrowsingChannelGuide.md)
  An activity for viewing your app’s channel guide.
### Specifying activity-related data
- [var userInfo: [AnyHashable : Any]?](nsuseractivity/userinfo.md)
  A dictionary containing app-specific state information needed to continue an activity on another device.
- [func addUserInfoEntries(from: [AnyHashable : Any])](nsuseractivity/adduserinfoentries(from:).md)
  Adds the contents of the specified dictionary to the user info dictionary.
- [var requiredUserInfoKeys: Set<String>?](nsuseractivity/requireduserinfokeys.md)
  A set of keys that represent the minimal information about the activity that should be stored for later restoration.
### Accessing feature-specific data
- [var appClipActivationPayload: APActivationPayload?](nsuseractivity/appclipactivationpayload.md)
  An object containing the payload information that launches an App Clip.
- [var detectedBarcodeDescriptor: CIBarcodeDescriptor?](nsuseractivity/detectedbarcodedescriptor.md)
  The barcode that the system scanner passes in.
- [var mapItem: MKMapItem!](nsuseractivity/mapitem.md)
  Attaches the specified map item to a user activity object.
- [var ndefMessagePayload: NFCNDEFMessage](nsuseractivity/ndefmessagepayload.md)
  The NDEF message read by the system in the background.
- [var isClassKitDeepLink: Bool](nsuseractivity/isclasskitdeeplink.md)
  A Boolean value that indicates whether a user activity represents a ClassKit context.
- [var contextIdentifierPath: [String]?](nsuseractivity/contextidentifierpath.md)
  The identifier path associated with a user activity generated by an app that adopts ClassKit.
- [func widgetConfigurationIntent<Intent>(of: Intent.Type) -> Intent?](nsuseractivity/widgetconfigurationintent(of:).md)
### Registering and invalidating activities
- [func becomeCurrent()](nsuseractivity/becomecurrent.md)
  Marks the activity as currently in use by the user.
- [func resignCurrent()](nsuseractivity/resigncurrent.md)
  Marks this activity object as inactive without invalidating it.
- [func invalidate()](nsuseractivity/invalidate.md)
  Invalidates an activity and marks it as no longer eligible for continuation.
- [var needsSave: Bool](nsuseractivity/needssave.md)
  A Boolean value that indicates whether the state of the activity needs to be updated.
- [class func deleteAllSavedUserActivities(completionHandler: () -> Void)](nsuseractivity/deleteallsaveduseractivities(completionhandler:).md)
  Deletes all user activities created by your app.
- [class func deleteSavedUserActivities(withPersistentIdentifiers: [NSUserActivityPersistentIdentifier], completionHandler: () -> Void)](nsuseractivity/deletesaveduseractivities(withpersistentidentifiers:completionhandler:).md)
  Deletes user activities created by your app that have the specified persistent identifiers.
### Managing type-safe access to user info
- [func setTypedPayload<T>(T) throws](nsuseractivity/settypedpayload(_:).md)
  Encodes the specified payload into the user activity’s user info dictionary.
- [func typedPayload<T>(T.Type) throws -> T](nsuseractivity/typedpayload(_:).md)
  Decodes the user activity’s user info dictionary as an instance of the specified type.
- [NSUserActivity.TypedPayloadError](nsuseractivity/typedpayloaderror.md)
  An enumeration that describes the error types for getting and setting a typed payload.
### Working with continuation streams
- [var supportsContinuationStreams: Bool](nsuseractivity/supportscontinuationstreams.md)
  A Boolean value that determines whether the continuing app can request streams to be opened back to the originating app.
- [func getContinuationStreams(completionHandler: (InputStream?, OutputStream?, (any Error)?) -> Void)](nsuseractivity/getcontinuationstreams(completionhandler:).md)
  Requests streams back to the originating app.
### Providing SiriKit with activity details
- [var interaction: INInteraction?](nsuseractivity/interaction.md)
  The SiriKit interaction object to use when configuring your app.
- [var suggestedInvocationPhrase: String?](nsuseractivity/suggestedinvocationphrase.md)
  A phrase suggested to the user when they create a shortcut.
- [var shortcutAvailability: INShortcutAvailabilityOptions](nsuseractivity/shortcutavailability.md)
  A set of defined contexts in which an intent or activity might be relevant to a user.
### Reporting errors
- [var NSUserActivityConnectionUnavailableError: Int](nsuseractivityconnectionunavailableerror-swift.var.md)
  The user activity couldn’t be continued because a required connection wasn’t available.
- [var NSUserActivityErrorMaximum: Int](nsuseractivityerrormaximum-swift.var.md)
  The end of the range of error codes reserved for user activity errors.
- [var NSUserActivityErrorMinimum: Int](nsuseractivityerrorminimum-swift.var.md)
  The start of the range of error codes reserved for user activity errors.
- [var NSUserActivityHandoffFailedError: Int](nsuseractivityhandofffailederror-swift.var.md)
  The data for the user activity wasn’t available.
- [var NSUserActivityHandoffUserInfoTooLargeError: Int](nsuseractivityhandoffuserinfotoolargeerror-swift.var.md)
  The user info dictionary was too large to receive.
- [var NSUserActivityRemoteApplicationTimedOutError: Int](nsuseractivityremoteapplicationtimedouterror-swift.var.md)
  The remote application failed to send data within the specified time.
### Deprecated
- [convenience init()](nsuseractivity/init.md)
  Creates a user activity object using the first activity type declared in the app’s information property list file.
### Default Implementations
- [AppEntityAnnotatable Implementations](nsuseractivity/appentityannotatable-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [AppEntityAnnotatable](../AppIntents/AppEntityAnnotatable.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [NSItemProviderReading](nsitemproviderreading.md)
- [NSItemProviderWriting](nsitemproviderwriting.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSUserActivityDelegate](nsuseractivitydelegate.md)
  The interface through which a user activity instance notifies its delegate of updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity)*