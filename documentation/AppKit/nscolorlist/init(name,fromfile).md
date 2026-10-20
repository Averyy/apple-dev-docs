# init(name:fromFile:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a color list from the specified file, registering it under the specified name if it isn’t in use already.

**Availability**:
- macOS

## Declaration

```swift
init?(name: NSColorList.Name, fromFile path: String?)
```

```objc
- (instancetype) initWithName:(NSColorListName) name fromFile:(NSString *) path;
```

#### Discussion

Note that this method does not add the color list to [`availableColorLists`](./availablecolorlists.md) until the color list is saved into the user’s path with [`write(toFile:)`](./write%28tofile%29.md) with a value of `nil`.

## Parameters

- `name`: The name of the file for the color list (minus the `“.clr”` extension). Specify `@””` if you don’t want a name.
- `path`: The full path to the file for the color list. A `nil` path indicates the color list should be initialized with no colors.

## See Also

### Creating Lists of Colors
- [init(name: NSColorList.Name)](./init%28name%29.md)
  Initializes and returns a color list, registering it under the specified name if it isn’t in use already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/init(name:fromfile:))*