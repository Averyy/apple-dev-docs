# NSColorList

**Framework**: AppKit  
**Kind**: class

An ordered list of color objects, identified by keys.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSColorList
```

#### Overview

A color list manages a list of [`NSColor`](nscolor.md) objects, each of which has an associated name. The [`NSColorPanel`](nscolorpanel.md) list mode color picker uses instances of [`NSColorList`](nscolorlist.md) to represent any lists of colors that come with the system, as well as any lists the user creates. An app can use a color list to manage document-specific color lists.

## Topics

### Creating Lists of Colors
- [init(name: NSColorList.Name)](nscolorlist/init(name:).md)
  Initializes and returns a color list, registering it under the specified name if it isn’t in use already.
- [init?(name: NSColorList.Name, fromFile: String?)](nscolorlist/init(name:fromfile:).md)
  Initializes and returns a color list from the specified file, registering it under the specified name if it isn’t in use already.
### Getting Lists of Colors
- [class var availableColorLists: [NSColorList]](nscolorlist/availablecolorlists.md)
  Returns an array of all color lists found in the standard color list directories.
- [init?(named: NSColorList.Name)](nscolorlist/init(named:).md)
  Searches the available color lists array and returns the color list with the specified name.
### Getting Information About Lists of Colors
- [var name: NSColorList.Name?](nscolorlist/name-swift.property.md)
  The name of the color list.
- [NSColorList.Name](nscolorlist/name-swift.typealias.md)
  The name assigned to a color list.
- [var isEditable: Bool](nscolorlist/iseditable.md)
  A Boolean value that indicates whether the color list can be modified.
### Managing Colors By Key
- [var allKeys: [NSColor.Name]](nscolorlist/allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func color(withKey: NSColor.Name) -> NSColor?](nscolorlist/color(withkey:).md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](nscolorlist/insertcolor(_:key:at:).md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](nscolorlist/removecolor(withkey:).md)
  Removes the color associated with the specified key from the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](nscolorlist/setcolor(_:forkey:).md)
  Associates the specified color object with the specified key.
### Writing and Removing Color List Files
- [func write(to: URL?) throws](nscolorlist/write(to:).md)
  Saves the color list to the file at the specified URL.
- [func removeFile()](nscolorlist/removefile.md)
  Removes the file from which the list was created, if the file is in a standard search path and owned by the user.
- [func write(toFile: String?) -> Bool](nscolorlist/write(tofile:).md)
  Saves the color list to the file at the specified path.
### Notifications
- [class let didChangeNotification: NSNotification.Name](nscolorlist/didchangenotification.md)
  Posted whenever a color list changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSColor](nscolor.md)
  An object that stores color data and sometimes opacity (alpha value).
- [class NSColorSpace](nscolorspace.md)
  An object that represents a custom color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist)*