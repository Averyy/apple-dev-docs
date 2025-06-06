# system

**Framework**: AppKit  
**Kind**: property

Returns the system-wide status bar located in the menu bar.

**Availability**:
- macOS ?+

## Declaration

```swift
class var system: NSStatusBar { get }
```

#### Return Value

The shared status bar object.

#### Discussion

The status bar begins at the right side of the menu bar (to the left of Menu Extras and the menu bar clock) and grows to the left as `NSStatusItem` objects are added to it.

## See Also

- [Status Bar Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/StatusBar/StatusBar.html#//apple_ref/doc/uid/10000073i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusbar/system)*