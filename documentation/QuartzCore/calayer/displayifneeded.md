# displayIfNeeded()

**Framework**: Core Animation  
**Kind**: method

Initiates the update process for a layer if it is currently marked as needing an update.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func displayIfNeeded()
```

#### Discussion

You can call this method as needed to force an update to your layer’s contents outside of the normal update cycle. Doing so is generally not needed, though. The preferred way to update a layer is to call [`setNeedsDisplay()`](calayer/setneedsdisplay().md) and let the system update the layer during the next cycle.

## See Also

- [func setNeedsDisplay()](calayer/setneedsdisplay.md)
  Marks the layer’s contents as needing to be updated.
- [func setNeedsDisplay(CGRect)](calayer/setneedsdisplay(_:).md)
  Marks the region within the specified rectangle as needing to be updated.
- [var needsDisplayOnBoundsChange: Bool](calayer/needsdisplayonboundschange.md)
  A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [func needsDisplay() -> Bool](calayer/needsdisplay.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.
- [class func needsDisplay(forKey: String) -> Bool](calayer/needsdisplay(forkey:).md)
  Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/displayifneeded())*