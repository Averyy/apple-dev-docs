# watchTemplate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The template that the Siri watch face uses to display the relevant shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var watchTemplate: INDefaultCardTemplate? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) INDefaultCardTemplate * watchTemplate;
```

*macOS*

```objc
@property (atomic, copy, nullable) INDefaultCardTemplate * watchTemplate;
```

## Mentions

- [Displaying Shortcut Information in a Siri Watch Face Card](../../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)

## Discussion

Provide a template when you want to customize the appearance of the relevant shortcut card displayed on the Siri watch face.

The listing below sets the watch template for a relevant shortcut in the Soup Chef sample app.

```swift
let suggestedShortcut = INRelevantShortcut(shortcut: shortcut)

let localizedTitle = NSString.deferredLocalizedIntentsString(with: "ORDER_LUNCH_TITLE") as String
let template = INDefaultCardTemplate(title: localizedTitle)
// Need a different string for the subtitle because of capitalization difference.
template.subtitle = NSString.deferredLocalizedIntentsString(with: menuItem.shortcutNameKey + "_SUBTITLE") as String
template.image = INImage(named: menuItem.iconImageName)

suggestedShortcut.watchTemplate = template
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcut/watchtemplate)*