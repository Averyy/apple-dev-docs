# ABActionDelegate

**Framework**: Address Book

Implement an Address Book action plug-in to support the display of rollover menus on top of custom items.

#### Overview

The `ABActionDelegate` informal protocol allows you to populate the rollover menus of Address Book with custom items. You do this by implementing an Address Book action plug-in. The plug-in’s [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) must implement doc://com.apple.documentation/documentation/objectivec/nsobject/1411302-actionproperty, doc://com.apple.documentation/documentation/objectivec/nsobject/1411304-title, and doc://com.apple.documentation/documentation/objectivec/nsobject/1411298-performaction.

Each action plug-in can implement only one action. Actions can only apply to items with labels. An action can display a simple window inside the Address Book application; if your action actions needs to do anything else, it should launch your own application to perform the action.

Use Xcode to create Address Book action plug-ins. Place action plug-ins in `~/Library/Address Book Plug-Ins` or `/Library/Address Book Plug-Ins`, depending on the scope you want for the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abactiondelegate)*