# Presenting the suggestions picker and processing a selection

**Framework**: Journaling Suggestions

Display the journaling suggestions picker and process a suggestion that someone chooses.

#### Overview

Present the [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md) to show people recent or important life events as suggestions, which include information about an event such as images, videos, locations, and so on. If a person selects a particular suggestion, the system provides you with the event details in the completion handler.

Start by choosing the text for the button in your app that presents the picker. When a person taps the text, the system presents the picker in a system process. The picker fills with suggestions that draw upon various personal experiences, such as a place someone visited, a person they connected with, a photo in their library, or a song that they often listened to.

When someone chooses a suggestion, the system makes high-level details about the event available to your app. Define the suggestion picker’s `onCompletion` closure to process the details, and incorporate them into your app’s creative workflow. A journaling app, for example, might display a visual suggestion in the format of a photo with placeholder text below it as the beginning of a new journal entry.

![A figure that features four iPhone device frames in an app workflow progressing from left to right. The first frame depicts a blank view and button that reads New Entry. A callout below reads Custom picker button. To the right, the next frame depicts several photos in a thumbnail view under text that reads Highlights from Photo Memories. A callout below reads Suggestions picker. The next frame to the right features the same photo thumbnails in a seletion list, with a thumbnail that featues a flower selected and a button below the list labeled Add to App 1. A callout below reads User selection. The final frame at the right depicts a detailed version of the same flower below user-defined text that reads Coastal Hike, followed by bars that represent a journal entry. A callout below reads Incorporated suggestion.](https://docs-assets.developer.apple.com/published/5a09b293a4ad55eb3bf8c334a37a9785/presenting-the-suggestions-picker-and-processing-a-selection-1%402x.png)

Journaling Suggestions gathers information from the system through built-in apps people use, such as Photos, Health, Fitness, Apple Podcasts, and Music. Suggestions can also come from third party apps that provide data through frameworks such as [`HealthKit`](https://developer.apple.com/documentation/HealthKit), [`CallKit`](https://developer.apple.com/documentation/CallKit), or [`SiriKit`](https://developer.apple.com/documentation/SiriKit).

#### Maintain User Privacy

Adopting Journaling Suggestions delivers an enhanced privacy experience in your app. When a person makes a selection in the picker, the system shares only the details of the chosen suggestion with your app. Thus, your app accesses only the suggestion data that a person explicitly authorizes.

When your app attempts to display the picker for the first time, a sheet appears that introduces Journaling Suggestions. If the person taps Turn On Journaling Suggestions, the picker displays, and includes an information privacy banner. The banner explains that your app only has access to the suggestions the person chooses to write about or saves to the app. The person can tap the X to close the banner, or they can tap Learn More, which presents a sheet that goes into more detail about Private Access.

> **Note**: The Journaling Suggestions consent sheet displays once per device, so it doesn’t appear if the person already viewed it, either by launching Journal, or by launching another app that uses Journaling Suggestions.

Suggestion data requires careful handling. To further preserve user privacy, follow the advice outlined in the [`Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/programs/apple-developer-program-license-agreement/#sensitive-content-analysis-framework).

#### Add the Journaling Suggestions Entitlement

To use Journaling Suggestions in your app, the  [`com.apple.developer.journal.allow`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.journal.allow) entitlement is required. The suggestions picker fails to present without it. You can can add this entitlement to your app by enabling the Journaling Suggestions capability in Xcode; see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

#### Name the Button That Opens the Suggestions Picker

The [`JournalingSuggestionsPicker`](journalingsuggestionspicker.md) initializers take an argument, `title`, for a button that people tap to display the picker.

```swift
let buttonTitle = "Show my personal events"
```

Choose a title that clearly describes the purpose of journaling suggestions in the context of your app. As an indication that personal moments are about to display, it’s important to set a person’s expectations about what the picker shows after they tap the text.

#### Declare and Present a Suggestions Picker

To present a suggestions picker, declare a view that displays a button title. When a person taps the button, the system presents the picker. Upon dismissal, the system invokes the completion handler you specify.

```swift
struct Example: View {
    var body: some View <-
        SuggestionsPicker {
            Text(buttonTitle)
        } onCompletion: { suggestion in
            // Parse the selected suggestion.
        }}}
```

#### Handle the Selected Suggestion Data

The picker fills with suggestions that include various types of personal experiences. When a person makes a selection, the system provides the chosen suggestion to your app’s `onCompletion` handler. Check the `suggestion` argument’s [`items`](journalingsuggestion/items.md) property to process the selection. Each [`JournalingSuggestion.ItemContent`](journalingsuggestion/itemcontent.md) item conforms to [`JournalingSuggestionAsset`](journalingsuggestionasset.md) and is one of following types:

| Type |  |
| --- | --- |
| [`JournalingSuggestion.Photo`](journalingsuggestion/photo.md) | An image from a person’s library, including the date captured. |
| [`JournalingSuggestion.Workout`](journalingsuggestion/workout.md) | Information about a workout that a person completes, including calories burnt, distance covered, a route they took, average heart rate, start and end time, and an icon for the type of workout. |
| [`JournalingSuggestion.Contact`](journalingsuggestion/contact.md) | An interaction a person has with someone in their contacts, including their name and Contact photo. |
| [`JournalingSuggestion.Location`](journalingsuggestion/location.md) | A place that a person visited, including its name, surrounding city, and geographic coordinates, if available. |
| [`JournalingSuggestion.Song`](journalingsuggestion/song.md) | The name of a song that a person plays, including the artist, album, and album artwork. |
| [`JournalingSuggestion.Podcast`](journalingsuggestion/podcast.md) | Information about a podcast that a person plays, including the show, artist, episode, and associated artwork. |
| [`JournalingSuggestion.Video`](journalingsuggestion/video.md) | A video from a person’s library, including the date captured. |
| [`JournalingSuggestion.LivePhoto`](journalingsuggestion/livephoto.md) | An image and short video that represents a live photo from a person’s library, including the date captured. |
| [`JournalingSuggestion.MotionActivity`](journalingsuggestion/motionactivity.md) | The number of steps a person takes in a motion event on iPhone, including an icon for the activity. |
| [`JournalingSuggestion.GenericMedia`](journalingsuggestion/genericmedia.md) | The media content a person listens to, including the information describing the media. |
| [`JournalingSuggestion.Reflection`](journalingsuggestion/reflection.md) | A reflection prompt that a person chooses. |
| [`JournalingSuggestion.StateOfMind`](journalingsuggestion/stateofmind.md) | The state of mind reflection in the Health app that describes a persons emotions and moods. |
| [`JournalingSuggestion.EventPoster`](journalingsuggestion/eventposter.md) | Details about a planned or attented event in Apple Invites. |

The following example demonstrates parsing a photo suggestion:

```swift
struct Example: View {
    @State var suggestionPhotos = [JournalingSuggestion.Photo]()
    @State var suggestionTitle: String? = nil
    var body: some View <-
        VStack {
            Spacer().frame(height: 25)
            SuggestionsPicker {
                Text(buttonTitle)
            } onCompletion: { suggestion in
                // Parse the suggestion details. 
                suggestionTitle = suggestion.title
                suggestionPhotos = await suggestion.content(forType: JournalingSuggestion.Photo.self)
            }
            // Display the suggestion details. 
            Spacer().frame(height: 25)
            Text(suggestionTitle ?? "")
            List {
                ForEach(suggestionPhotos, id: \.photo) { item in
                    AsyncImage(url: item.photo) { image in
                        image.image?
                            .resizable ()
                            .aspectRatio(contentMode: .fit)
                    }
                    .frame(maxHeight: 200)
                }}}}
```

The code displays the suggestion title, followed by a list of images that the person selected in the picker.

> **Note**: A person can control the types of suggestions available in the picker by tapping Customize in the consent sheet, or by adjusting Privacy & Security settings for Journaling Suggestions in the Settings app.

When your app parses a selected suggestion’s details, it organizes that information to serve as a base for creative expression. A journaling app, for example, might list the selected images in a journal entry.

## See Also

- [Journaling Suggestions updates](../Updates/JournalingSuggestions.md)
  Learn about important changes in Journaling Suggestions.
- [com.apple.developer.journal.allow](../BundleResources/Entitlements/com.apple.developer.journal.allow.md)
  The entitlement that enables an app to present the journaling suggestions picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/presenting-the-suggestions-picker-and-processing-a-selection)*