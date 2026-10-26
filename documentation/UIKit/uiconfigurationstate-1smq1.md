# UIConfigurationState

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The requirements for an object that encapsulates a view’s state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UIConfigurationState <NSObject, NSCopying, NSSecureCoding>
```

#### Overview

This protocol provides a blueprint for a configuration state object, which encompasses a trait collection along with all of the common states that affect a view’s appearance. A configuration state encapsulates the inputs that configure a view for any possible state or combination of states. You use a configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [`updateConfiguration(using:)`](./uicollectionviewcell/updateconfiguration%28using%29.md) method in your view subclass and use the state parameter. Outside of this method, you can get a view’s configuration state by using its [`configurationState`](./uicollectionviewcell/configurationstate-4u37h.md) property.

For more information, see [`UIViewConfigurationState`](./uiviewconfigurationstate-c.class.md) and [`UICellConfigurationState`](./uicellconfigurationstate-c.class.md).

## Topics

### Managing configuration states
- [traitCollection](./uiconfigurationstate-1smq1/traitcollection.md)
  The traits that describe the current layout environment of the view, such as the user interface style and layout direction.
- [- customStateForKey:](./uiconfigurationstate-1smq1/customstateforkey_.md)
  Retrieves the custom state for the specified custom state key.
- [- setCustomState:forKey:](./uiconfigurationstate-1smq1/setcustomstate_forkey_.md)
  Sets the custom state for the specified custom state key.
- [- objectForKeyedSubscript:](./uiconfigurationstate-1smq1/objectforkeyedsubscript_.md)
  Retrieves the object for the specified custom state key.
- [- setObject:forKeyedSubscript:](./uiconfigurationstate-1smq1/setobject_forkeyedsubscript_.md)
  Sets the object for the specified custom state key.
### Creating a configuration state manually
- [- initWithTraitCollection:](./uiconfigurationstate-1smq1/initwithtraitcollection_.md)
  Creates a configuration state with the specified trait collection.

## Relationships

### Inherits From
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
### Conforming Types
- [UIContentUnavailableConfigurationState](./uicontentunavailableconfigurationstate-c.class.md)
- [UIViewConfigurationState](./uiviewconfigurationstate-c.class.md)

## See Also

### Configuration states
- [UIViewConfigurationState](./uiviewconfigurationstate-c.class.md)
  A structure that encapsulates a view’s state.
- [UICellConfigurationState](./uicellconfigurationstate-c.class.md)
  An object that encapsulates a cell’s state.
- [struct UIConfigurationStateCustomKey](./uiconfigurationstatecustomkey.md)
  A key that defines a custom state for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationstate-1smq1)*