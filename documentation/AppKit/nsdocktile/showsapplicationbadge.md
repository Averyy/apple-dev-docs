# showsApplicationBadge

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean showing whether the tile is badged with the application’s icon

**Availability**:
- macOS 10.5+

## Declaration

```swift
var showsApplicationBadge: Bool { get set }
```

```objc
@property BOOL showsApplicationBadge;
```

## Discussion

Miniaturized windows include the application badge by default to convey the associated application to the user. In macOS 10.5 and later, application tiles do not support the application badge. A miniaturized window with a custom view does not draw the application badge.

The application icon is positioned automatically in the tile by the [`NSDockTile`](../nsdocktile.md) object.

## See Also

### Applying Badge Icons to the Tile
- [var badgeLabel: String?](./badgelabel.md)
  The string to be displayed in the tile’s badging area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocktile/showsapplicationbadge)*