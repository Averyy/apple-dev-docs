---
url: https://developer.apple.com/design/human-interface-guidelines/path-controls
framework: HIG
---

# Path controls

**Type:** article

**Platforms:** macos

A path control shows the file system path of a selected file or folder.

![A stylized representation of a path control for a HIG Design document showing its root disk, parent folder, and selected item. The image is tinted red to subtly reflect the red in the original six-color Apple logo.](/images/com.apple.HIG/components-path-control-intro~dark@2x.png)
For example, choosing View > Show Path Bar in the Finder displays a path bar at the bottom of the window. It shows the path of the selected item, or the path of the window’s folder if nothing is selected.
There are two styles of path control.
![A screenshot of a Finder path bar that displays a hierarchy of four locations.](/images/com.apple.HIG/path-controls-standard~dark@2x.png)
**Standard.** A linear list that includes the root disk, parent folders, and selected item. Each item appears with an icon and a name. If the list is too long to fit within the control, it hides names between the first and last items. If you make the control editable, people can drag an item onto the control to select the item and display its path in the control.
![A screenshot of a path control showing a folder icon and a pop-up control.](/images/com.apple.HIG/path-controls-popup~dark@2x.png)
**Pop up.** A control similar to a [pop-up button](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons) that shows the icon and name of the selected item. People can click the item to open a menu containing the root disk, parent folders, and selected item. If you make the control editable, the menu contains an additional Choose command that people can use to select an item and display it in the control. They can also drag an item onto the control to select it and display its path.

## Best practices
**Use a path control in the window body, not the window frame.** Path controls aren’t intended for use in toolbars or status bars. Note that the path control in the Finder appears at the bottom of the window body, not in the status bar.

## Platform considerations
*Not supported in iOS, iPadOS, tvOS, visionOS, or watchOS.*

## Resources

#### Related
[File management](file-management.md)

#### Developer documentation
[NSPathControl](../appkit/nspathcontrol.md) — AppKit



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/path-controls](https://developer.apple.com/design/human-interface-guidelines/path-controls)*
