# NSColorList

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An ordered list of color objects, identified by keys.

**Availability**:
- macOS

## Declaration

```swift
class NSColorList
```

```objc
@interface NSColorList : NSObject
```

## Overview

A color list manages a list of [`NSColor`](./nscolor.md) objects, each of which has an associated name. The [`NSColorPanel`](./nscolorpanel.md) list mode color picker uses instances of [`NSColorList`](./nscolorlist.md) to represent any lists of colors that come with the system, as well as any lists the user creates. An app can use a color list to manage document-specific color lists.

## Topics

### Creating Lists of Colors
- [init(name: NSColorList.Name)](./nscolorlist/init%28name%29.md)
  Initializes and returns a color list, registering it under the specified name if it isn’t in use already.
- [init?(name: NSColorList.Name, fromFile: String?)](./nscolorlist/init%28name,fromfile%29.md)
  Initializes and returns a color list from the specified file, registering it under the specified name if it isn’t in use already.
### Getting Lists of Colors
- [class var availableColorLists: [NSColorList]](./nscolorlist/availablecolorlists.md)
  Returns an array of all color lists found in the standard color list directories.
- [init?(named: NSColorList.Name)](./nscolorlist/init%28named%29.md)
  Searches the available color lists array and returns the color list with the specified name.
### Getting Information About Lists of Colors
- [var name: NSColorList.Name?](./nscolorlist/name-swift.property.md)
  The name of the color list.
- [NSColorList.Name](./nscolorlist/name-swift.typealias.md)
  The name assigned to a color list.
- [var isEditable: Bool](./nscolorlist/iseditable.md)
  A Boolean value that indicates whether the color list can be modified.
### Managing Colors By Key
- [var allKeys: [NSColor.Name]](./nscolorlist/allkeys.md)
  An array of the keys by which the color objects are stored in the color list.
- [func color(withKey: NSColor.Name) -> NSColor?](./nscolorlist/color%28withkey%29.md)
  Returns the color object associated with the specified key.
- [func insertColor(NSColor, key: NSColor.Name, at: Int)](./nscolorlist/insertcolor%28_,key,at%29.md)
  Inserts the specified color at the specified location in the color list.
- [func removeColor(withKey: NSColor.Name)](./nscolorlist/removecolor%28withkey%29.md)
  Removes the color associated with the specified key from the color list.
- [func setColor(NSColor, forKey: NSColor.Name)](./nscolorlist/setcolor%28_,forkey%29.md)
  Associates the specified color object with the specified key.
### Writing and Removing Color List Files
- [func write(to: URL?) throws](./nscolorlist/write%28to%29.md)
  Saves the color list to the file at the specified URL.
- [func removeFile()](./nscolorlist/removefile%28%29.md)
  Removes the file from which the list was created, if the file is in a standard search path and owned by the user.
- [func write(toFile: String?) -> Bool](./nscolorlist/write%28tofile%29.md)
  Saves the color list to the file at the specified path.
### Notifications
- [class let didChangeNotification: NSNotification.Name](./nscolorlist/didchangenotification.md)
  Posted whenever a color list changes.
### Structures
- [NSColorList.DidChangeMessage](./nscolorlist/didchangemessage.md)
### Initializers
- [init?(coder: NSCoder)](./nscolorlist/init%28coder%29.md)

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

### Colors
- [class NSColor](./nscolor.md)
  An object that stores color data and sometimes opacity (alpha value).
- [class NSColorSpace](./nscolorspace.md)
  An object that represents a custom color space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist)*