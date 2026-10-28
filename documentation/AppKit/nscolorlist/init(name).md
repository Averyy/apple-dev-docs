# init(name:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a color list, registering it under the specified name if it isn’t in use already.

**Availability**:
- macOS

## Declaration

```swift
init(name: NSColorList.Name)
```

```objc
- (instancetype) initWithName:(NSColorListName) name;
```

## Return Value

The initialized color list.

## Discussion

This method invokes [`init(name:fromFile:)`](./init%28name,fromfile%29.md) with a `fromFile:` argument of `nil`, indicating that the color list doesn’t need to be initialized from a file. Note that this method does not add the color list to [`availableColorLists`](./availablecolorlists.md) until the color list is saved into the user’s path with [`write(toFile:)`](./write%28tofile%29.md) with a value of `nil`.

## Parameters

- `name`: The name under which to register the color list. Specify `@””` if you don’t want a name.

## See Also

### Related Documentation
- [init?(name: NSColorList.Name, fromFile: String?)](./init%28name,fromfile%29.md)
  Initializes and returns a color list from the specified file, registering it under the specified name if it isn’t in use already.
### Creating Lists of Colors
- [init?(name: NSColorList.Name, fromFile: String?)](./init%28name,fromfile%29.md)
  Initializes and returns a color list from the specified file, registering it under the specified name if it isn’t in use already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorlist/init(name:))*