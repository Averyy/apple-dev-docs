# CPAssistantCellConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

An object that provides the configuration attributes for the assistant cell.

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

An audio or communication CarPlay app can choose to display an *assistant cell* in a list template that allows the user to interact with the app using Siri. You create an instance of this configuration object that describes the position, visibility, and supported Siri intent, and provide that to your app’s list template using the [`init(title:sections:assistantCellConfiguration:)`](./cplisttemplate/init%28title,sections,assistantcellconfiguration%29.md) initializer or the [`assistantCellConfiguration`](./cplisttemplate/assistantcellconfiguration.md) property.

Your app must include an Intents Extension that handles the intent corresponding to the action you specify in the [`assistantAction`](./cpassistantcellconfiguration/assistantaction.md) property; audio apps must support [`INPlayMediaIntent`](../Intents/inplaymediaintent.md) and communication apps must support [`INStartCallIntent`](../Intents/instartcallintent.md). For more information, see [Creating an Intents App Extension](../SiriKit/creating-an-intents-app-extension.md).

## Topics

### Creating an Assistant Cell Configuration
- [init(position: CPListItem.AssistantCellPosition, visibility: CPListItem.AssistantCellVisibility, assistantAction: CPAssistantCellActionType)](./cpassistantcellconfiguration/init%28position,visibility,assistantaction%29.md)
  Creates a configuration object with the specified position, visibility, and action.
### Getting the Configuration Attributes
- [var position: CPListItem.AssistantCellPosition](./cpassistantcellconfiguration/position.md)
  The position of the assistant cell in the list template.
- [var visibility: CPListItem.AssistantCellVisibility](./cpassistantcellconfiguration/visibility.md)
  The visibility of the assistant cell in the list template.
- [var assistantAction: CPAssistantCellActionType](./cpassistantcellconfiguration/assistantaction.md)
  The action that Siri performs when the user selects the assistant cell.
- [enum CPAssistantCellActionType](./cpassistantcellactiontype.md)
  The supported Siri actions of the assistant cell.
### Initializers
- [init?(coder: NSCoder)](./cpassistantcellconfiguration/init%28coder%29.md)

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

### Managing the Assistant Cell
- [var assistantCellConfiguration: CPAssistantCellConfiguration?](./cplisttemplate/assistantcellconfiguration.md)
  The object that provides the configuration attributes for the assistant cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpassistantcellconfiguration)*