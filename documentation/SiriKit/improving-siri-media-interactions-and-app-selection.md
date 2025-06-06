# Improving Siri Media Interactions and App Selection

**Framework**: Sirikit

Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.

#### Overview

When the user interacts with Siri to request media, the system may send your app an intent that represents the user’s request. To effectively communicate the user’s request to your app, the system relies on the intents your app supports, the names of media items and performers, and the user’s listening habits. The system also uses this information to make proactive suggestions and provide relevant search results. Your app can contribute to this information with Core Spotlight and Intents to improve the accuracy, relevance, and convenience of playing media.

App Selection streamlines voice-driven interactions. As the system learns about the user’s listening habits, it intelligently predicts when the user intends for your app to handle a request, even if the user didn’t mention your app by name. By adopting these Intents and Core Spotlight APIs, your app also helps refine App Selection’s predictions.

For information about how Apple protects user privacy when your app shares information with the system, see the Siri section of [`Privacy - Features`](https://developer.apple.comhttps://www.apple.com/privacy/features/).

> **Note**:  Session 10073: [`Empower Your Intents`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10073/) Session 10087: [`Design for Intelligence: Make Friends with “The System”`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10087/) Session 10060: [`Design High Quality Siri Media Interactions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10060/)

##### Support Media Intents

Use [`INPlayMediaIntent`](https://developer.apple.com/documentation/intents/inplaymediaintent) to receive media intents from Siri and Shortcuts. Support other system-defined media intents, such as [`INUpdateMediaAffinityIntent`](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintent) or [`INAddMediaIntent`](https://developer.apple.com/documentation/intents/inaddmediaintent), that reflect interactions the user can perform directly in your app.

> 💡 **Tip**:  In iOS 14 and later, you can set up handling for [`INPlayMediaIntent`](https://developer.apple.com/documentation/intents/inplaymediaintent) directly in your app. To continue supporting earlier versions of iOS, resolve and confirm the intent in an extension, then respond with [`INPlayMediaIntentResponseCode.continueInApp`](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/continueinapp) or [`INPlayMediaIntentResponseCode.handleInApp`](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/handleinapp) so the system sends the intent to the app to play the media.

Tell the system what types of media your app supports in Xcode’s Project editor. In the Supported Intents section of the Project editor, select each Media Category that describes your app’s content. Select `General` if your app plays media that doesn’t fit any of the other categories, like spooky sound effects or white noise. To opt in to Siri media control, you must choose at least one category for your app. With the settings shown here, users can say “Play some music in ControlAudio” to play music in the ControlAudio app. When App Selection is available, they can simply say “Play some music” and Siri intelligently picks the user’s preferred music app with App Selection.

![A screenshot of Xcode’s Project editor with the General pane active and the Supported Intents section expanded. The table of supported intents lists INPlayMediaIntent and INAddMediaIntent. In the Media Categories list, the checkbox for Music is selected.](https://docs-assets.developer.apple.com/published/61965f0c6d6005f3713a3045d16ab5c1/media-3670928%402x.png)

When a user searches for a musician or band on iOS 15 or later, Spotlight may include a suggestion to start listening to content from that artist. To include your app in the list of apps available to listen on, support [`INSearchForMediaIntent`](https://developer.apple.com/documentation/intents/insearchformediaintent). If the user chooses your app from the list, or if your app is the user’s preferred music app, the system sends your app an intent so you can display content by that artist.

The system can also use your app’s [`INPlayMediaIntent`](https://developer.apple.com/documentation/intents/inplaymediaintent) donations to offer personalized audio suggestions on Lock Screen, in Control Center, and in the Home app. To opt-in to these suggestions, you need to explicitly indicate that your app can play media container intents with no additional parameters. If you haven’t already customized the PlayMedia system intent, follow these steps to set that up:

1. If your project doesn’t already have an `.intentDefinition` file, use File > New File and then choose SiriKit Intent Definition File to add one to your project.
2. Open your `.intentDefinition` file.
3. Choose Customize System Intent > Media > Play Media from the + menu at the bottom of the intent definition editor.

Once you have the PlayMedia system intent in a SiriKit Intent Definition file, make sure that its list of Supported Combinations includes the entry with “mediaContainer” as the only parameter.

![The Suggestions section of Xcode’s intent definition editor. In the Supported Combinations list, the item “mediaContainer” is selected.](https://docs-assets.developer.apple.com/published/68807656b0f6a3c420711706f00b6dcb/media-3686892%402x.png)

> **Note**:  The system offers the user audio suggestions based on donations the system can play in an audio-only situation. The system excludes the following media types when generating audio suggestions: [`INMediaItemType.news`](https://developer.apple.com/documentation/intents/inmediaitemtype/news), [`INMediaItemType.musicVideo`](https://developer.apple.com/documentation/intents/inmediaitemtype/musicvideo), [`INMediaItemType.movie`](https://developer.apple.com/documentation/intents/inmediaitemtype/movie), [`INMediaItemType.tvShow`](https://developer.apple.com/documentation/intents/inmediaitemtype/tvshow), [`INMediaItemType.tvShowEpisode`](https://developer.apple.com/documentation/intents/inmediaitemtype/tvshowepisode), and [`INMediaItemType.unknown`](https://developer.apple.com/documentation/intents/inmediaitemtype/unknown).

##### Donate Interactions

Improve App Selection, Shortcuts, and Shortcut Suggestions by donating interactions from your app. Each time the user starts playing media directly in your app, create and donate an [`INInteraction`](https://developer.apple.com/documentation/intents/ininteraction) containing an [`INPlayMediaIntent`](https://developer.apple.com/documentation/intents/inplaymediaintent) to tell the system what the user is listening to. Provide as much detail as possible in each donation to help the system interact more accurately with the user in the future. If the user starts a playlist or radio station, donate that information instead of each individual song.

> ❗ **Important**:  Suggestions improve as the system accumulates donated interactions. If some media becomes irrelevant or unavailable, use [`delete(with:completion:)`](https://developer.apple.com/documentation/intents/ininteraction/delete(with:completion:)-2d1gs) to remove interactions associated with those specific media items. Don’t call [`deleteAll(completion:)`](https://developer.apple.com/documentation/intents/ininteraction/deleteall(completion:)) unless you really mean to reset what the system has learned about the way the user interacts with your app.

##### Set the Current User Context

When your app launches, create an [`INMediaUserContext`](https://developer.apple.com/documentation/intents/inmediausercontext), add the user’s information, and make the context current. The system uses this information to optimize the user experience for App Selection. The following code listing shows how to set the current context for a user with a paid subscription and a few hundred items in their library:

```swift
let context = INMediaUserContext()
context.numberOfLibraryItems = 345
context.subscriptionStatus = .subscribed
context.becomeCurrent()
```

##### Populate the Spotlight Database

Add metadata about playlists and individual media items from the user’s local library to the Core Spotlight database. When the user searches for the item, the system can offer to play the media in your app alongside any other search results.

For Swift, choose the [`completeUntilFirstUserAuthentication`](https://developer.apple.com/documentation/foundation/fileprotectiontype/1616633-completeuntilfirstuserauthentica) level of protection for your Spotlight database so the system can access this information even when your app isn’t running. In Objective-C, choose the [`NSFileProtectionCompleteUntilFirstUserAuthentication`](https://developer.apple.com/documentation/foundation/nsfileprotectioncompleteuntilfirstuserauthentication) level of protection for your Spotlight database so the system can access this information even when your app isn’t running.

```swift
let attributes = CSSearchableItemAttributeSet(contentType: .audio)
attributes.title = "Some Cool Song Title"
attributes.artist = "Hot New Artist"
attributes.album = "Hot New Artist's Exclusive Album"
attributes.genre = "Pop"
attributes.playCount = 5
attributes.lastUsedDate = Date()

let item = CSSearchableItem(uniqueIdentifier: "<identifier>", domainIdentifier: domain, attributeSet: attributes)

CSSearchableIndex.default().indexSearchableItems([item]) { ... }

```

> ⚠️ **Warning**:  If you need to delete items from the index, use [`deleteSearchableItems(withDomainIdentifiers:completionHandler:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex/deleteSearchableItems(withDomainIdentifiers:completionHandler:)). Calling [`deleteAllSearchableItems(completionHandler:)`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex/deleteAllSearchableItems(completionHandler:)) deletes not only the searchable items you’ve added directly to the searchable index, but also every [`INInteraction`](https://developer.apple.com/documentation/intents/ininteraction) your app has donated or Siri has donated on behalf of your app.

##### Define Relevant Vocabulary

Define vocabulary for Siri, both specific to the individual user and relevant for all users but exclusive to your app. Providing vocabulary helps Siri match a user’s request to media items you’ve added to the Spotlight database or included in donated intents and interactions. Take care to include terms that include numbers or have other unusual spellings. There are two ways to provide vocabulary, and each one helps Siri interpret and route user requests:

- Global vocabulary relevant to all users of your app.
- User-specific vocabulary that you update as the user interacts with your app.

Define general terms in the [`Global Vocabulary Reference`](global-vocabulary-reference.md). Add an `AppIntentVocabulary.plist` file to your project and provide any vocabulary that’s unique to your app but relevant for all users in the [`Parameter Vocabularies`](parameter-vocabularies.md) section. For more details, see [`Registering Custom Vocabulary with SiriKit`](registering-custom-vocabulary-with-sirikit.md).

Provide additional vocabulary programmatically with [`INVocabulary`](https://developer.apple.com/documentation/intents/invocabulary), like names that are unique or particularly important to the user, such as playlist titles. Put terms that are most important for this user or that Siri most often misunderstands first. You should update the vocabulary as needed, such as when the user renames or deletes a playlist, or begins listening to a particular artist more frequently.

## See Also

- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Deleting Donated Shortcuts](deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Dispatching intents to handlers](dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving interactions between Siri and your messaging app](improving-interactions-between-siri-and-your-messaging-app.md)
  Donate app-specific content, use Siri’s contact suggestions, and adopt the latest platform features to create a more consistent messaging experience.
- [Registering Custom Vocabulary with SiriKit](registering-custom-vocabulary-with-sirikit.md)
  Register your app’s custom terminology, and provide sample phrases for how to use your app with Siri.
- [Confirming the Details of an Intent](confirming-the-details-of-an-intent.md)
  Perform final validation of the intent parameters and verify that your services are ready to fulfill the intent.
- [Handling an Intent](handling-an-intent.md)
  Fulfill the intent and provide feedback to SiriKit about what you did.
- [Resolving the Parameters of an Intent](resolving-the-parameters-of-an-intent.md)
  Validate the parameters of an intent and make sure that you have the information you need to continue.
- [Generating a List of Ride Options](generating-a-list-of-ride-options.md)
  Generate ride options for Maps to display to the user.
- [Handling the Ride-Booking Intents](handling-the-ride-booking-intents.md)
  Support the different intent-handling sequences for booking rides with Shortcuts or Maps.
- [Displaying Shortcut Information in a Siri Watch Face Card](displaying-shortcut-information-in-a-siri-watch-face-card.md)
  Display and customize watch-specific shortcut information with a default card template.
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SiriKit/improving-siri-media-interactions-and-app-selection)*