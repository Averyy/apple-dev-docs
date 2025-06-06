# Outline View Button Keys

**Framework**: AppKit

These keys are used by the outline view to create disclosure buttons that collapse and expand items.

#### Overview

The outline view creates these buttons by calling its inherited [`makeView(withIdentifier:owner:)`](nstableview/makeview(withidentifier:owner:).md) method, passing in the key as the identifier and the delegate as the owner.

> **Note**:  These keys are backwards compatible to OS X v10.7, however, the symbol is not exported prior to v10.9 and the string value (`@"NSOutlineViewDisclosureButtonKey"`) must be used.

 These keys are backwards compatible to OS X v10.7, however, the symbol is not exported prior to v10.9 and the string value (`@"NSOutlineViewDisclosureButtonKey"`) must be used.

## Topics

### Constants
- [class let disclosureButtonIdentifier: NSUserInterfaceItemIdentifier](nsoutlineview/disclosurebuttonidentifier.md)
  The normal triangle disclosure button.
- [class let showHideButtonIdentifier: NSUserInterfaceItemIdentifier](nsoutlineview/showhidebuttonidentifier.md)
  The Show/Hide button.

## See Also

- [Drop on Item Index](drop-on-item-index.md)
  This constant defines an index that allows you to drop an item directly on a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/outline-view-button-keys)*