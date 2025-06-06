# SLComposeSheetConfigurationItem

**Framework**: Social  
**Kind**: class

An object that provides additional configuration details to use when configuring a composition interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class SLComposeSheetConfigurationItem
```

#### Overview

The [`SLComposeSheetConfigurationItem`](slcomposesheetconfigurationitem.md) class gives users a way to configure the properties of a post before posting it. For example, you can use these objects to let users choose an account from which to post, an album to which to post, or a location to add to a post.

To provide support for post configurations in your [`SLComposeServiceViewController`](slcomposeserviceviewcontroller.md) view, create as many configuration items as you need, place them in an array, and return the array in your implementation of `configurationItems`. Note that only one configuration item can be displayed at a time.

## Topics

### Creating a Configuration Item
- [init!()](slcomposesheetconfigurationitem/init.md)
  Returns a configuration item.
### Responding to User Interaction
- [var tapHandler: SLComposeSheetConfigurationItemTapHandler!](slcomposesheetconfigurationitem/taphandler.md)
  A custom tap handler block that handles user interaction with a configuration item.
- [typealias SLComposeSheetConfigurationItemTapHandler](slcomposesheetconfigurationitemtaphandler.md)
  The method signature for a configuration item’s tap handler block.
### Specifying Configuration Information
- [var title: String!](slcomposesheetconfigurationitem/title.md)
  The name of the configuration item stored as a localized string.
- [var value: String!](slcomposesheetconfigurationitem/value.md)
  The current value or setting of the configuration item.
- [var valuePending: Bool](slcomposesheetconfigurationitem/valuepending.md)
  A Boolean value that indicates whether the configuration item’s value is ready for display.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func configurationItems() -> [Any]!](slcomposeserviceviewcontroller/configurationitems.md)
  Returns configuration items to display in the compose view.
- [func reloadConfigurationItems()](slcomposeserviceviewcontroller/reloadconfigurationitems.md)
  Reloads the list of configuration items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/social/slcomposesheetconfigurationitem)*