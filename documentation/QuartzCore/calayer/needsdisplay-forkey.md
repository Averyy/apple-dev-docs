# needsDisplay(forKey:)

**Framework**: Core Animation  
**Kind**: method

Returns a Boolean indicating whether changes to the specified key require the layer to be redisplayed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func needsDisplay(forKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the layer requires a redisplay.

#### Discussion

Subclasses can override this method and return [`true`](https://developer.apple.com/documentation/swift/true) if the layer should be redisplayed when the value of the specified attribute changes. Animations changing the value of the attribute also trigger redisplay.

The default implementation of this method returns [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `key`: A string that specifies an attribute of the layer.

## See Also

- [class func defaultAction(forKey: String) -> (any CAAction)?](calayer/defaultaction(forkey:).md)
  Returns the default action for the current class.
- [class func defaultValue(forKey: String) -> Any?](calayer/defaultvalue(forkey:).md)
  Specifies the default value associated with the specified key.
- [func setNeedsDisplay()](calayer/setneedsdisplay.md)
  Marks the layer’s contents as needing to be updated.
- [func setNeedsDisplay(CGRect)](calayer/setneedsdisplay(_:).md)
  Marks the region within the specified rectangle as needing to be updated.
- [var needsDisplayOnBoundsChange: Bool](calayer/needsdisplayonboundschange.md)
  A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [func displayIfNeeded()](calayer/displayifneeded.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [func needsDisplay() -> Bool](calayer/needsdisplay.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/needsdisplay(forkey:))*