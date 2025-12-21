# ABActionDelegate

**Framework**: Address Book

Implement an Address Book action plug-in to support the display of rollover menus on top of custom items.

#### Overview

The `ABActionDelegate` informal protocol allows you to populate the rollover menus of Address Book with custom items. You do this by implementing an Address Book action plug-in. The plug-in’s [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) must implement [`actionProperty()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/actionProperty()), [`title(for:identifier:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/title(for:identifier:)), and [`performAction(for:identifier:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/performAction(for:identifier:)).

Each action plug-in can implement only one action. Actions can only apply to items with labels. An action can display a simple window inside the Address Book application; if your action actions needs to do anything else, it should launch your own application to perform the action.

Use Xcode to create Address Book action plug-ins. Place action plug-ins in `~/Library/Address Book Plug-Ins` or `/Library/Address Book Plug-Ins`, depending on the scope you want for the action.

## Topics

### Performing actions
- [func performAction(for: ABPerson!, identifier: String!)](../ObjectiveC/NSObject-swift.class/performAction(for:identifier:).md)
  Sent to the delegate to perform the action.
### Querying
- [func actionProperty() -> String!](../ObjectiveC/NSObject-swift.class/actionProperty.md)
  Sent to the delegate to request the property the action applies to.
- [func shouldEnableAction(for: ABPerson!, identifier: String!) -> Bool](../ObjectiveC/NSObject-swift.class/shouldEnableAction(for:identifier:).md)
  Sent to the delegate to determine whether the action should be enabled.
- [func title(for: ABPerson!, identifier: String!) -> String!](../ObjectiveC/NSObject-swift.class/title(for:identifier:).md)
  Sent to the delegate to request the title of the menu item for the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abactiondelegate)*