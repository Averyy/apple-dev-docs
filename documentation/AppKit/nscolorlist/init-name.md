# init(name:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns a color list, registering it under the specified name if it isn’t in use already.

**Availability**:
- macOS ?+

## Declaration

```swift
init(name: NSColorList.Name)
```

#### Return Value

The initialized color list.

#### Discussion

This method invokes [`init(name:fromFile:)`](nscolorlist/init(name:fromfile:).md) with a `fromFile:` argument of `nil`, indicating that the color list doesn’t need to be initialized from a file. Note that this method does not add the color list to [`availableColorLists`](nscolorlist/availablecolorlists.md) until the color list is saved into the user’s path with [`write(toFile:)`](nscolorlist/write(tofile:).md) with a value of `nil`.

## Parameters

- `name`: The name under which to register the color list. Specify   if you don’t want a name.

## See Also

- [Color Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html#//apple_ref/doc/uid/10000082i)
- [init?(name: NSColorList.Name, fromFile: String?)](nscolorlist/init(name:fromfile:).md)
  Initializes and returns a color list from the specified file, registering it under the specified name if it isn’t in use already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/init(name:))*