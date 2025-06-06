# needsDisplayOnBoundsChange

**Framework**: Core Animation  
**Kind**: property

A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var needsDisplayOnBoundsChange: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the layer automatically calls its [`setNeedsDisplay()`](calayer/setneedsdisplay().md) method whenever its [`bounds`](calayer/bounds.md) property changes. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func setNeedsDisplay()](calayer/setneedsdisplay.md)
  Marks the layer’s contents as needing to be updated.
- [func setNeedsDisplay(CGRect)](calayer/setneedsdisplay(_:).md)
  Marks the region within the specified rectangle as needing to be updated.
- [func displayIfNeeded()](calayer/displayifneeded.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [func needsDisplay() -> Bool](calayer/needsdisplay.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.
- [class func needsDisplay(forKey: String) -> Bool](calayer/needsdisplay(forkey:).md)
  Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/needsdisplayonboundschange)*