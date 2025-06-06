# backgroundColor

**Framework**: AppKit  
**Kind**: property

The receiver’s background color.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: NSColor? { get set }
```

#### Discussion

By default, the background is set to a light blue color for `NSPathStyleStandard` and `nil` for the other styles. You can use `[NSColor clearColor]` to make the background transparent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/backgroundcolor)*