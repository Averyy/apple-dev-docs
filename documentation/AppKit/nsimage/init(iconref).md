# init(iconRef:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes the image object with a Carbon-style icon resource.

**Availability**:
- macOS 10.5+ - Deprecated in 11.0

> **Deprecated**: Use -[NSWorkspace iconForFile:], -[NSWorkspace iconForFiles:], -[NSWorkspace iconForFileType:], or +[NSImage imageNamed:] instead.

## Declaration

```swift
convenience init(iconRef: IconRef)
```

```objc
- (instancetype) initWithIconRef:(IconRef) iconRef;
```

#### Return Value

An initialized `NSImage` object.

#### Discussion

Creates one or more bitmap image representations, one for each size icon contained in the `IconRef` data structure. This initialization method automatically retains the data in the `iconRef` parameter and loads the bitmaps from that data file lazily.

## Parameters

- `iconRef`: A reference to a Carbon icon resource.

## See Also

### Deprecated instance methods
- [func lockFocus()](./lockfocus%28%29.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](./lockfocusflipped%28_%29.md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Removes the focus from the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(iconref:))*