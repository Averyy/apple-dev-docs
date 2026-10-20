# setNeedsDisplay()

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Marks the layer’s contents as needing to be updated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setNeedsDisplay()
```

```objc
- (void) setNeedsDisplay;
```

#### Discussion

Calling this method causes the layer to recache its content. This results in the layer potentially calling either the [`display(_:)`](../calayerdelegate/display%28_%29.md) or [`draw(_:in:)`](../calayerdelegate/draw%28_,in%29.md) method of its delegate. The existing content in the layer’s [`contents`](./contents.md) property is removed to make way for the new content.

## See Also

### Updating layer display
- [func setNeedsDisplay(CGRect)](./setneedsdisplay%28_%29.md)
  Marks the region within the specified rectangle as needing to be updated.
- [var needsDisplayOnBoundsChange: Bool](./needsdisplayonboundschange.md)
  A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [func needsDisplay() -> Bool](./needsdisplay%28%29.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.
- [class func needsDisplay(forKey: String) -> Bool](./needsdisplay%28forkey%29.md)
  Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/setneedsdisplay())*