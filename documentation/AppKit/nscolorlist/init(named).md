# init(named:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Searches the available color lists array and returns the color list with the specified name.

**Availability**:
- macOS

## Declaration

```swift
init?(named name: NSColorList.Name)
```

```objc
+ (NSColorList *) colorListNamed:(NSColorListName) name;
```

#### Return Value

The color list with the specified name or `nil` if no such color list exists.

## Parameters

- `name`: The name of the color list to retrieve. This name must not include the “`.clr`” suffix.

## See Also

### Related Documentation
- [var name: NSColorList.Name?](./name-swift.property.md)
  The name of the color list.
### Getting Lists of Colors
- [class var availableColorLists: [NSColorList]](./availablecolorlists.md)
  Returns an array of all color lists found in the standard color list directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/init(named:))*