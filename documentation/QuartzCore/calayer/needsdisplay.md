# needsDisplay()

**Framework**: Core Animation  
**Kind**: method

Returns a Boolean indicating whether the layer has been marked as needing an update.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func needsDisplay() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the layer needs to be updated.

## See Also

- [func setNeedsDisplay()](calayer/setneedsdisplay.md)
  Marks the layer’s contents as needing to be updated.
- [func setNeedsDisplay(CGRect)](calayer/setneedsdisplay(_:).md)
  Marks the region within the specified rectangle as needing to be updated.
- [var needsDisplayOnBoundsChange: Bool](calayer/needsdisplayonboundschange.md)
  A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [func displayIfNeeded()](calayer/displayifneeded.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [class func needsDisplay(forKey: String) -> Bool](calayer/needsdisplay(forkey:).md)
  Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/needsdisplay())*