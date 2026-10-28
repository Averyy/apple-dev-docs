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

> **Note**:  The Siri assistant cell is only available in audio and communication apps.

Your app doesn’t receive a callback when the user selects the assistant cell. Instead, you configure an Intents Extension to handle the type of intent you specify in the cell’s configuration; audio apps must support [`INPlayMediaIntent`](../../Intents/inplaymediaintent.md) and communication apps must support [`INStartCallIntent`](../../Intents/instartcallintent.md).

If you update this property’s value, CarPlay automatically refreshes your app’s interface to reflect the changes.

## See Also

### Managing the Assistant Cell
- [class CPAssistantCellConfiguration](../cpassistantcellconfiguration.md)
  An object that provides the configuration attributes for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/assistantcellconfiguration)*