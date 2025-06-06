# NSAccessibilityGroup

**Framework**: AppKit  
**Kind**: protocol

A role-based protocol that declares the minimum interface necessary to act as a container for other user interface elements.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSAccessibilityGroup : NSAccessibilityElementProtocol
```

#### Overview

Visual users often know that sets of controls go together due to their proximity on the screen. However, you must explicitly define these relationships before assistive apps can use them as well. Use this protocol when you want to logically group a collection of accessibility elements. A view that adopts this protocol indicates that an assistive app should treat its content as a group of controls.

You can further enhance the adopting element by implementing any of the information properties or action methods that the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol declares.

> **Note**:  Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

 Any class that adopts this protocol must implement all of its methods, and the required methods of any protocol it inherits from. The compiler may require you to override some methods that your ancestors have already implemented. Simply follow the compiler’s warnings, and reimplement these methods as necessary.

## Relationships

### Inherits From
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSAccessibilityLayoutArea](nsaccessibilitylayoutarea.md)
- [NSAccessibilityLayoutItem](nsaccessibilitylayoutitem.md)
- [NSAccessibilityList](nsaccessibilitylist.md)
- [NSAccessibilityOutline](nsaccessibilityoutline.md)
- [NSAccessibilityProgressIndicator](nsaccessibilityprogressindicator.md)
- [NSAccessibilityRow](nsaccessibilityrow.md)
- [NSAccessibilityTable](nsaccessibilitytable.md)
### Conforming Types
- [NSOutlineView](nsoutlineview.md)
- [NSProgressIndicator](nsprogressindicator.md)
- [NSTableRowView](nstablerowview.md)
- [NSTableView](nstableview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitygroup)*