# init(iconRef:)

**Framework**: AppKit  
**Kind**: init

Initializes the image object with a Carbon-style icon resource.

**Availability**:
- macOS 10.5+

## Declaration

```swift
convenience init(iconRef: IconRef)
```

#### Return Value

An initialized `NSImage` object.

#### Discussion

Creates one or more bitmap image representations, one for each size icon contained in the `IconRef` data structure. This initialization method automatically retains the data in the `iconRef` parameter and loads the bitmaps from that data file lazily.

## Parameters

- `iconRef`: A reference to a Carbon icon resource.

## See Also

- [func lockFocus()](nsimage/lockfocus.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](nsimage/lockfocusflipped(_:).md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](nsimage/unlockfocus.md)
  Removes the focus from the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(iconref:))*