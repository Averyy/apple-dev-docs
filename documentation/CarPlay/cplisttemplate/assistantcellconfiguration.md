# assistantCellConfiguration

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The object that provides the configuration attributes for the assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var assistantCellConfiguration: CPAssistantCellConfiguration? { get set }
```

```objc
@property (nonatomic, strong, nullable) CPAssistantCellConfiguration * assistantCellConfiguration;
```

## Discussion

In an audio, video, or communication app, this property tells CarPlay whether to configure an additional row with a Siri action. The object in this property tells CarPlay the type of action to perform and where to display the row in your list interface. If you’re not creating an audio, video, or communication app, leave the value of this property set to `nil`.

An audio or video app uses this cell to play media files, and a communication app uses this cell to initiate a call using Siri. CarPlay handles all interactions with the cell and reports results to your Intents extension using one of the following SiriKit intents:

The [`INPlayMediaIntent`](../../Intents/inplaymediaintent.md) type tells your audio or video app to play the specified media file. The [`INStartCallIntent`](../../Intents/instartcallintent.md) type tells your communication app to start a call.

If you modify this property when the list is visible, CarPlay automatically refreshes your app’s interface to reflect the new value.

## See Also

### Managing the supplemental content
- [var title: String?](./title.md)
  The title to display in the navigation bar when the list is visible.
- [var listHeader: CPListTemplateDetailsHeader?](./listheader.md)
  An optional header to display between the navigation bar and first section of content.
- [var headerGridButtons: [CPGridButton]?](./headergridbuttons.md)
  Buttons to display in the header area above the list content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/assistantcellconfiguration)*