# activityIdentifier

**Framework**: Group Activities  
**Kind**: property  
**Required**: Yes

An app-defined string that uniquely identifies the activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var activityIdentifier: String { get }
```

## Mentions

- [Defining your app’s SharePlay activities](defining-your-apps-shareplay-activities.md)
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Discussion

Implement this property and return a value that uniquely identifies the activity within your app. An app may support multiple activities, and each activity requires a unique identifier string. Use reverse-DNS notation for your identifier strings. For example, supply a string like `"com.mycompany.myapp.watchmovie"` for a movie-watching activity.

If you don’t implement this property yourself, the default implementation composes an activity identifier using your app’s bundle identifier and the current class or struct name. For example, if the app’s bundle identifier is `"com.mycompany.myapp"` and your activity type name is `MovieActivity`, the resulting identifier string is `"com.mycompany.myapp.MovieActivity"`.

## See Also

- [var metadata: GroupActivityMetadata](groupactivity/metadata.md)
  A description of the activity, and optional image to display to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivity/activityidentifier)*