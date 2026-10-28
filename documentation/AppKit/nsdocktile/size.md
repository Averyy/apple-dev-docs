# size

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the tile.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var size: NSSize { get }
```

```objc
@property (readonly) NSSize size;
```

## Discussion

This corresponds to the size of the backing store in the dock, which may be bigger than the actual tile displayed on the screen.

## See Also

### Getting the Tile Information
- [var owner: AnyObject?](./owner.md)
  The object represented by the dock tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocktile/size)*