# helpRequested(with:)

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to implement specialized context-sensitive help behavior.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func helpRequested(with eventPtr: NSEvent)
```

#### Discussion

Subclasses in their implementation of this method should cause the Help Manager ([`NSHelpManager`](nshelpmanager.md)) to display the help associated with the menu. Never invoke this method directly.

##### Special Considerations

In macOS 10.6 and later this method has no effect. This method may be deprecated in a future release.

## Parameters

- `eventPtr`: An [`NSEvent`](nsevent.md) object representing the event associated with the help request.

## See Also

- [func showContextHelp(for: Any, locationHint: NSPoint) -> Bool](nshelpmanager/showcontexthelp(for:locationhint:).md)
  Displays the context-sensitive help for a given object at or near the point on the screen specified by a given point.
- [class func menuZone() -> NSZone!](nsmenu/menuzone.md)
  Returns the zone from which `NSMenu` objects should be allocated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/helprequested(with:))*