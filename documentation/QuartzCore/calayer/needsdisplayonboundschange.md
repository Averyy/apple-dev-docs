# needsDisplayOnBoundsChange

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL needsDisplayOnBoundsChange;
```

## Discussion

When this property is set to [`true`](../../Swift/true.md), the layer automatically calls its [`setNeedsDisplay()`](./setneedsdisplay%28%29.md) method whenever its [`bounds`](./bounds.md) property changes. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Updating layer display
- [func setNeedsDisplay()](./setneedsdisplay%28%29.md)
  Marks the layer’s contents as needing to be updated.
- [func setNeedsDisplay(CGRect)](./setneedsdisplay%28_%29.md)
  Marks the region within the specified rectangle as needing to be updated.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [func needsDisplay() -> Bool](./needsdisplay%28%29.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.
- [class func needsDisplay(forKey: String) -> Bool](./needsdisplay%28forkey%29.md)
  Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/needsdisplayonboundschange)*