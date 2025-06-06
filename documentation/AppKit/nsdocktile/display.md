# display()

**Framework**: AppKit  
**Kind**: method

Redraws the dock tile’s content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func display()
```

#### Discussion

If a custom content view is provided, Cocoa calls the `drawRect:` method of that view (and its subviews) to draw the tile’s content.

You can call this method to force the redrawing of the dock tile contents. You might do this if the contents of the underlying application or window change in a way that would require a refreshing of the tile. Some types of system activity, such as resizing the dock, may trigger automatic redraws of the tile. In most cases, however, your application is responsible for triggering redraws.

Cocoa does not automatically redraw the contents of your dock tile. Instead, your application must explicitly send `display` messages to the dock tile object whenever the contents of your view change and need to be redrawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocktile/display())*