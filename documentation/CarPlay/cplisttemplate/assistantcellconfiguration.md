# assistantCellConfiguration

**Framework**: CarPlay  
**Kind**: property

The object that provides the configuration attributes for the assistant cell.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var assistantCellConfiguration: CPAssistantCellConfiguration? { get set }
```

#### Discussion

> **Note**:  The Siri assistant cell is only available in audio and communication apps.

 The Siri assistant cell is only available in audio and communication apps.

Your app doesn’t receive a callback when the user selects the assistant cell. Instead, you configure an Intents Extension to handle the type of intent you specify in the cell’s configuration; audio apps must support doc://com.apple.documentation/documentation/sirikit/inplaymediaintent and communication apps must support doc://com.apple.documentation/documentation/sirikit/instartcallintent.

If you update this property’s value, CarPlay automatically refreshes your app’s interface to reflect the changes.

## See Also

- [class CPAssistantCellConfiguration](cpassistantcellconfiguration.md)
  An object that provides the configuration attributes for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/assistantcellconfiguration)*