# Displaying Shortcut Information in a Siri Watch Face Card

**Framework**: SiriKit

Display and customize watch-specific shortcut information with a default card template.

#### Overview

The Siri watch face displays a relevant shortcut in a card that can provide the following information:

- App icon and name (supplied by the system)
- Title, subtitle, and custom image (supplied by the intent or user activity used to create the shortcut, or by an [`INDefaultCardTemplate`](https://developer.apple.com/documentation/intents/indefaultcardtemplate) object)

##### Display Intent Based Shortcuts

When your app uses an [`INIntent`](https://developer.apple.com/documentation/intents/inintent) object to create the shortcut, the system retrieves the intent’s title and subtitle from the intent settings defined in the intent definition file. To include an image, call [`setImage:forParameterNamed:`](https://developer.apple.com/documentation/intents/inintent/setimage:forparameternamed:) on the intent and pass in an [`INImage`](https://developer.apple.com/documentation/intents/inimage).

The listing below sets the image for a order soup intent in the Soup Chef sample app.

```swift
orderSoupIntent.setImage(INImage(named: menuItem.iconImageName), forParameterNamed: \OrderSoupIntent.soup)
```

##### Display User Activity Based Shortcuts

When your app uses an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object to create the shortcut, the system retrieves the title from the title property of the user activity. To specify a subtitle, create an [`CSSearchableItemAttributeSet`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet) with the content type of `kUTTypeItem`, and set the [`contentDescription`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/contentDescription) property. To include an image, set the [`thumbnailData`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableItemAttributeSet/thumbnailData) on the attribute set.

The listing below sets the title, subtitle, and image for the NSUserActivity object.

```swift
import CoreSpotlight
import MobileCoreServices

let userActivity = NSUserActivity(activityType: "com.myapp.myactivity")
userActivity.title = "Title"

let attributes = CSSearchableItemAttributeSet(itemContentType: kUTTypeItem as String)
attributes.contentDescription = "Subtitle"
attributes.thumbnailData =  imageLiteral(resourceName: "custom-image").pngData()

userActivity.contentAttributeSet = attributes
```

##### Use Card Templates

If you want to show a UI specific to the watch—for example, to display a shortcut’s title that is shorter than the one Siri displays on the user’s iPhone or iPad—provide the relevant shortcut a default card template by setting the [`watchTemplate`](https://developer.apple.com/documentation/intents/inrelevantshortcut/watchtemplate) property. The template allows your app to customize the [`title`](https://developer.apple.com/documentation/intents/indefaultcardtemplate/title), [`subtitle`](https://developer.apple.com/documentation/intents/indefaultcardtemplate/subtitle), and [`image`](https://developer.apple.com/documentation/intents/indefaultcardtemplate/image). (You cannot change or remove the app icon and name shown in the card.)

The listing below sets the template for an order intent in the Soup Chef sample app.

```swift
let order = Order(quantity: 1, menuItem: menuItem, menuItemOptions: [])
let orderIntent = order.intent

guard let shortcut = INShortcut(intent: orderIntent) else { return nil }

let suggestedShortcut = INRelevantShortcut(shortcut: shortcut)

let localizedTitle = NSString.deferredLocalizedIntentsString(with: "ORDER_LUNCH_TITLE") as String
let template = INDefaultCardTemplate(title: localizedTitle)
template.subtitle = NSString.deferredLocalizedIntentsString(with: menuItem.shortcutNameKey + "_SUBTITLE") as String
template.image = INImage(named: menuItem.iconImageName)

suggestedShortcut.watchTemplate = template
```

The code above creates the Siri watch face card shown in the figure below. To download the complete sample code, see [`Soup Chef: Accelerating App Interactions with Shortcuts`](soup-chef-accelerating-app-interactions-with-shortcuts.md).

![A screenshot of the Siri watch face suggesting the order lunch relevant shortcut.](https://docs-assets.developer.apple.com/published/05c57f334872b722b691792ac99c2b55/media-3030287%402x.png)

The system displays the information in one of four layouts based on the information your app provides in the card template. For instance, if you don’t provide an image, the system uses a layout that displays only the title and subtitle fields. And if you provide only the title, the system uses a layout that can wrap the title on two lines.

![An image showing four layouts for a Siri watch face card. The first layouts shows a title, subtitle, and image. The second layout shows a title and subtitle. The third layout shows a title and image. The fourth layout shows the title only, wrapping to two lines.](https://docs-assets.developer.apple.com/published/623ee5303c999daaaba2eea9398f6fb9/media-3030290%402x.png)

## See Also

- [Soup Chef: Accelerating App Interactions with Shortcuts](soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
- [Adding User Interactivity with Siri Shortcuts and the Shortcuts App](adding-user-interactivity-with-siri-shortcuts-and-the-shortcuts-app.md)
  Add custom intents and parameters to help users interact more quickly and effectively with Siri and the Shortcuts app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Deleting Donated Shortcuts](deleting-donated-shortcuts.md)
  Remove your donations from Siri.
- [Dispatching intents to handlers](dispatching-intents-to-handlers.md)
  Provide SiriKit with an intent handler capable of handling a specific intent.
- [Improving Siri Media Interactions and App Selection](improving-siri-media-interactions-and-app-selection.md)
  Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
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
- [Donating Reservations](donating-reservations.md)
  Inform Siri of reservations made from your app.
- [Defining Relevant Shortcuts for the Siri Watch Face](defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [Specifying Synonyms for Your App Name](specifying-synonyms-for-your-app-name.md)
  Provide alternative names for your app that are more familiar or easier for users to speak.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/displaying-shortcut-information-in-a-siri-watch-face-card)*