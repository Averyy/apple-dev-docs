# Defining your app’s SharePlay activities

**Framework**: Group Activities

Configure your app’s SharePlay support and define the activities that people can perform from your app.

#### Overview

SharePlay activities are an organic way to create experiences that people can enjoy together. When you add the Group Activities framework to your app, you gain the ability to share your app’s features over FaceTime, Messages, and AirDrop. Some examples of experiences people can share together include:

- Watching or listening to content
- Participating in an online fitness class
- Creating content on a shared whiteboard or painter’s canvas
- Shopping for food, clothes, or other online products
- Planning a trip or browsing the web
- Reading a book or taking an online class

Consider the preceding list of activities, and any other activities your app supports, and build SharePlay support for them. Think about how people might enjoy those activities if they were together in the same physical space. Consider the types of interactions that can occur in the real world, and build support for those interactions into your activities. For example, a movie-watching app needs to pause playback for all participants when one person hits the pause button. A shared whiteboard app needs to transmit newly drawn content to other participants, and send all of the content to someone who arrives late.

> **Note**: Make activities available on all the platforms your app supports to ensure people can join from any device. Customize the experience as needed for each platform to give it a more intuitive feel.

Make activities available on all the platforms your app supports to ensure people can join from any device. Customize the experience as needed for each platform to give it a more intuitive feel.

##### Configure the Shareplay Entitlements

Before you start adding SharePlay support to your app, add the [`com.apple.developer.group-session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.group-session) entitlement to your Xcode project. Because SharePlay involves communication with other devices, you need this entitlement to support activities. To add the entitlement to your app:

1. Open your Xcode project.
2. Select your app target.
3. Go to the Signing & Capabilities pane.
4. Add the Group Activities capability to the target.

Configure this entitlement only for app targets. When you add the Group Activities capability, Xcode adds the necessary entitlements to your app and updates its provisioning profile.

##### Turn an Existing App Feature Into an Activity

Turn one of your app’s features into a SharePlay experience by adopting the [`GroupActivity`](groupactivity.md) protocol in the appropriate place in your code. This protocol provides the basic definition of a SharePlay activity. When you adopt it in one of your app’s existing types, that type provides the information that SharePlay needs to promote that activity to participants. If you prefer to keep the activity separate from your app data structures, define a new type and add any app-specific data you need to manage the activity.

Most of the content in a [`GroupActivity`](groupactivity.md) type is the data you use to support the activity itself. Include data that is critical for performing the activity, such as the URL of the movie in a movie-watching activity. Also, include information to support the overall experience, such as the name of the movie and an image to display in the SharePlay UI. Store as little data as possible to support the activity, and share state information instead of detailed changes wherever possible. For example, store a link to the movie instead of the movie file itself. The following example defines a `Movie` type that stores information about a movie to watch, and a group activity to share the experience:

```swift
struct Movie: Codable{
    var title : String
    var movieURL : URL

    // Codable support...
}

struct WatchTogether: GroupActivity {
    // The movie to watch together.
    var movie: Movie
   
    init(movie: Movie) {
        self.movie = movie
    }
}
```

##### Customize the Unique Identifier for Your Activity

To differentiate one activity from another, each [`GroupActivity`](groupactivity.md) type must have a unique string in its [`activityIdentifier`](groupactivity/activityidentifier.md) property. The default implementation of this property combines your app’s bundle identifier with the name of your custom [`GroupActivity`](groupactivity.md) type. This string is sufficient for most activity types, but you can also specify a custom value if you prefer.

If you specify a custom string, include your company name in reverse-DNS format along with any other information you need to distinguish the activity from others in your app. The following code adds a custom identifier for the `WatchTogether` activity:

```swift
struct WatchTogether: GroupActivity {
    // Specify the activity type to the system.
    static let activityIdentifier = "com.example.myapp.watch-movie-together"

    // The movie to watch together.
    var movie: Movie

    init(movie: Movie) {
        self.movie = movie
    }
}
```

Make activity identifiers as granular as needed to differentiate the activities within your app. Don’t create one activity type that serves multiple purposes. Instead, define separate types and give them unique activity identifiers. For example, if your video player supports playing both movies and television shows, create separate activities for each.

##### Provide Descriptive Information About the Activity

Each activity contains a [`GroupActivityMetadata`](groupactivitymetadata.md) type that stores descriptive information about the activity. When inviting people to join the activity, the system incorporates this metadata into the system UI. A concise title, a short description of the activity, and an image help people understand which activity they’re joining. You can also provide additional details, such as a fallback URL that someone can use to join the activity from a web browser.

Create a [`GroupActivityMetadata`](groupactivitymetadata.md) type dynamically from your activity, and populate it with activity-related details. Fill in as much of the information as possible, and make your descriptions concise and clear. People need to quickly identify the purpose of the activity and whether it’s one they want to join, so make sure your descriptions are clear enough for someone to make a decision. The following example creates the metadata for the `WatchTogether` activity and populates it with the movie details. Use the [`fallbackURL`](groupactivitymetadata/fallbackurl.md) property to provide a URL to the content in case a participant doesn’t have the app.

```swift
extension WatchTogether {
    // Provide information about the activity.
    var metadata: GroupActivityMetadata {
        var metadata = GroupActivityMetadata()
        metadata.type = .watchTogether
        metadata.title = "\(movie.title)"
        metadata.fallbackURL = movie.movieURL
        metadata.supportsContinuationOnTV = true

        return metadata
    }
}
```

Classify your app’s activities by specifying an appropriate value for the [`type`](groupactivitymetadata/type.md) property of [`GroupActivityMetadata`](groupactivitymetadata.md). In the SharePlay banner, the system displays an icon that matches the type of the activity. The icon provides an additional visual cue about what people can expect from the activity.

##### Include a Transferable Representation of Your Activity

The Core Transferable framework helps you build data types that you can easily transfer between different processes or devices. In particular, the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol makes it easy to support pasteboard operations and drag and drop. The Group Activities framework supports this protocol by letting you associate a [`GroupActivity`](groupactivity.md) with one of your transferable types. SwiftUI and SharePlay via AirDrop also take advantage of this association to present possible activities from your UI.

If you initialize an activity using one of your app’s data types, adopt the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol in that data type and include a transfer representation for the activity. Implement the [`transferRepresentation`](https://developer.apple.com/documentation/CoreTransferable/Transferable/transferRepresentation) property of the protocol, and include a [`GroupActivityTransferRepresentation`](groupactivitytransferrepresentation.md) structure in addition to any representations you use to support the pasteboard. Use the [`GroupActivityTransferRepresentation`](groupactivitytransferrepresentation.md) structure to initialize an activity using the current data type. For example, the following code creates an activity to watch a movie for a custom `Movie` type:

```swift
struct Movie: Transferable, Codable{
    var title : String
    var movieURL : URL
    
    /// A transferable version of the movie URL and group activity.
    static var transferRepresentation: some TransferRepresentation {
        ProxyRepresentation(exporting: \.movieURL)
        
        GroupActivityTransferRepresentation { movie in
            WatchTogether(movie: movie)
        }
    }

    // Codable support...
}
```

When you include a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view in your SwiftUI interface, you can specify your transferable data type as the shareable item from that view. When someone taps or clicks the link, the system displays a share sheet with options for sharing the data. If you include a [`GroupActivityTransferRepresentation`](groupactivitytransferrepresentation.md) type, the sheet includes an option to start the associated activity. The following example creates a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view using the `Movie` data type:

```swift
struct MovieDetailView: View {
    let movie: Movie

    var body: some View {
        ShareLink(
            item: movie, 
            preview: SharePreview(
                movie.title))
    }
}
```

For more information on displaying a share sheet or supporting SharePlay via AirDrop, see [`Presenting SharePlay activities from your app’s UI`](promoting-shareplay-activities-from-your-apps-ui.md).

## See Also

- [Supporting Coordinated Media Playback](../AVFoundation/supporting-coordinated-media-playback.md)
  Create synchronized media experiences that enable users to watch and listen across devices.
- [protocol GroupActivity](groupactivity.md)
  A type that can advertise your app’s activities to other participants.
- [struct GroupActivityMetadata](groupactivitymetadata.md)
  Text and image content that describes an activity to potential participants.
- [enum GroupActivityActivationResult](groupactivityactivationresult.md)
  The result of preparing to start a custom activity.
- [struct GroupActivityTransferRepresentation](groupactivitytransferrepresentation.md)
  A type that lets you start a group activity from a known context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/defining-your-apps-shareplay-activities)*