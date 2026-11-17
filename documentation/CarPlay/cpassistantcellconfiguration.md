# CPAssistantCellConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that configures a special row in for performing app-related actions using Siri.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
class CPAssistantCellConfiguration
```

```objc
@interface CPAssistantCellConfiguration : NSObject
```

## Overview

The `CPAssistantCellConfiguration` type tells CarPlay how to display the *assistant cell* in a list interface. The assistant cell is a system-provided row that allows people to play audio or video content or start a call using Siri. If you’re building an audio, video, or communication app, you can add this cell to your list to give people the ability a hands-free way to perform these actions.

> ❗ **Important**: The assistant cell is available only in audio, video, and communication apps. Trying to display it in other app types generates a build-time error.

To add an assistant cell to your app’s interface, create a `CPAssistantCellConfiguration` type and configure it with the type of action to perform and the placement of the cell in your list. When your [`CPListTemplate`](./cplisttemplate.md) object contains a cell configuration, the list displays an extra row with instructions on how to perform the action you specified. A person can then use Siri to complete the action and deliver details back to your app.

CarPlay reports Siri-based interactions to your app’s Intents extension, which you implement using [SiriKit](../SiriKit/SiriKit.md). To play a media file from your audio or video app, CarPlay expects this extension to implement the [`INPlayMediaIntent`](../Intents/inplaymediaintent.md) type. To start a call, CarPlay expects the extension to implement the [`INStartCallIntent`](../Intents/instartcallintent.md) type. If your app extension doesn’t implement the expected type, CarPlay raises an exception. For more information about how to implement an Intents extension, see [Creating an Intents App Extension](../SiriKit/creating-an-intents-app-extension.md).

## Topics

### Creating an assistant cell configuration
- [init(position: CPListItem.AssistantCellPosition, visibility: CPListItem.AssistantCellVisibility, assistantAction: CPAssistantCellActionType)](./cpassistantcellconfiguration/init%28position,visibility,assistantaction%29.md)
  Creates a configuration object with the specified position, visibility, and action.
- [init?(coder: NSCoder)](./cpassistantcellconfiguration/init%28coder%29.md)
### Getting the configuration attributes
- [var assistantAction: CPAssistantCellActionType](./cpassistantcellconfiguration/assistantaction.md)
  The action that Siri performs when the user selects the assistant cell.
- [var position: CPListItem.AssistantCellPosition](./cpassistantcellconfiguration/position.md)
  The position of the assistant cell in the list template.
- [var visibility: CPListItem.AssistantCellVisibility](./cpassistantcellconfiguration/visibility.md)
  The visibility of the assistant cell in the list template.
- [enum CPAssistantCellActionType](./cpassistantcellactiontype.md)
  The supported actions of the assistant cell.
- [CPListItem.AssistantCellPosition](./cplistitem/assistantcellposition.md)
  The supported placement options for the assistant cell.
- [CPListItem.AssistantCellVisibility](./cplistitem/assistantcellvisibility.md)
  The visibility options for the assistant cell.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Headers and special cells
- [class CPListTemplateDetailsHeader](./cplisttemplatedetailsheader.md)
  A header section that displays rich media content and action buttons above a list of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellconfiguration)*