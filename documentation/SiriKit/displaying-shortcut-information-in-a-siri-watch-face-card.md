# Displaying Shortcut Information in a Siri Watch Face Card

**Framework**: SiriKit  
**Role**: Article

Display and customize watch-specific shortcut information with a default card template.

**Availability**:
- watchOS 5.0+ - Deprecated in 11.0

## Overview

The Siri watch face displays a relevant shortcut in a card that can provide the following information:

- App icon and name (supplied by the system)
- Title, subtitle, and custom image (supplied by the intent or user activity used to create the shortcut, or by an [`INDefaultCardTemplate`](../Intents/indefaultcardtemplate.md) object)

> ❗ **Important**: The Siri Watch Face is available in watchOS 11 and earlier. To make content available in the Smart Stack on Apple Watch using widgets, refer to [WidgetKit](../WidgetKit/WidgetKit.md), [Increasing the visibility of widgets in Smart Stacks](../WidgetKit/widget-suggestions-in-smart-stacks.md), and [App Intents](../AppIntents/AppIntents.md). For more information about migrating your SiriKit code to App Intents, refer to [Migrating widgets from SiriKit Intents to App Intents](../WidgetKit/migrating-from-sirikit-intents-to-app-intents.md) and [Soup Chef with App Intents: Migrating custom intents](./soup-chef-with-app-intents-migrating-custom-intents.md).

### Display Intent-Based Shortcuts

When your app uses an [`INIntent`](../Intents/inintent.md) object to create the shortcut, the system retrieves the intent’s title and subtitle from the intent settings defined in the intent definition file. To include an image, call [`setImage:forParameterNamed:`](../Intents/inintent/setimage_forparameternamed_.md) on the intent and pass in an [`INImage`](../Intents/inimage.md).

The listing below sets the image for a order soup intent in the Soup Chef sample app.

```swift
orderSoupIntent.setImage(INImage(named: menuItem.iconImageName), forParameterNamed: \OrderSoupIntent.soup)
```

### Display User Activity-Based Shortcuts

When your app uses an [`NSUserActivity`](../Foundation/nsuseractivity.md) object to create the shortcut, the system retrieves the title from the title property of the user activity. To specify a subtitle, create an [`CSSearchableItemAttributeSet`](../CoreSpotlight/cssearchableitemattributeset.md) with the content type of `kUTTypeItem`, and set the [`contentDescription`](../CoreSpotlight/cssearchableitemattributeset/contentdescription.md) property. To include an image, set the [`thumbnailData`](../CoreSpotlight/cssearchableitemattributeset/thumbnaildata.md) on the attribute set.

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

### Use Card Templates

If you want to show a UI specific to the watch—for example, to display a shortcut’s title that is shorter than the one Siri displays on the user’s iPhone or iPad—provide the relevant shortcut a default card template by setting the [`watchTemplate`](../Intents/inrelevantshortcut/watchtemplate.md) property. The template allows your app to customize the [`title`](../Intents/indefaultcardtemplate/title.md), [`subtitle`](../Intents/indefaultcardtemplate/subtitle.md), and [`image`](../Intents/indefaultcardtemplate/image.md). (You cannot change or remove the app icon and name shown in the card.)

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

The code above creates the Siri watch face card shown in the figure below. To download the complete sample code, see [Soup Chef: Accelerating App Interactions with Shortcuts](./soup-chef-accelerating-app-interactions-with-shortcuts.md).

![A screenshot of the Siri watch face suggesting the order lunch relevant shortcut.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3030287@2x.png)

The system displays the information in one of four layouts based on the information your app provides in the card template. For instance, if you don’t provide an image, the system uses a layout that displays only the title and subtitle fields. And if you provide only the title, the system uses a layout that can wrap the title on two lines.

![An image showing four layouts for a Siri watch face card. The first layouts shows a title, subtitle, and image. The second layout shows a title and subtitle. The third layout shows a title and image. The fourth layout shows the title only, wrapping to two lines.](https://developer.apple.com/tutorials/images/com.apple.sirikit/media-3030290@2x.png)

## See Also

### Related Documentation
- [Soup Chef: Accelerating App Interactions with Shortcuts](./soup-chef-accelerating-app-interactions-with-shortcuts.md)
  Make it easy for people to use Siri with your app by providing shortcuts to your app’s actions.
### Siri watch face
- [class INDefaultCardTemplate](../Intents/indefaultcardtemplate.md)
  A card template for customizing the Siri watch face for a shortcut.
- [Defining Relevant Shortcuts for the Siri Watch Face](./defining-relevant-shortcuts-for-the-siri-watch-face.md)
  Inform Siri when your app’s shortcuts may be useful to the user.
- [class INRelevantShortcut](../Intents/inrelevantshortcut.md)
  An object that defines a shortcut and its relevance to the user.
- [class INRelevantShortcutStore](../Intents/inrelevantshortcutstore.md)
  An object that saves relevant shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/displaying-shortcut-information-in-a-siri-watch-face-card)*