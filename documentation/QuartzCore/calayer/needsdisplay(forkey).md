# needsDisplay(forKey:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (BOOL) needsDisplayForKey:(NSString *) key;
```

#### Return Value

[`true`](../../Swift/true.md) if the layer requires a redisplay.

#### Discussion

Subclasses can override this method and return [`true`](../../Swift/true.md) if the layer should be redisplayed when the value of the specified attribute changes. Animations changing the value of the attribute also trigger redisplay.

The default implementation of this method returns [`false`](../../Swift/false.md).

## Parameters

- `key`: A string that specifies an attribute of the layer.

## See Also

### Related Documentation
- [class func defaultAction(forKey: String) -> (any CAAction)?](./defaultaction%28forkey%29.md)
  Returns the default action for the current class.
- [class func defaultValue(forKey: String) -> Any?](./defaultvalue%28forkey%29.md)
  Specifies the default value associated with the specified key.
### Updating layer display
- [func setNeedsDisplay()](./setneedsdisplay%28%29.md)
  Marks the layer’s contents as needing to be updated.
- [func setNeedsDisplay(CGRect)](./setneedsdisplay%28_%29.md)
  Marks the region within the specified rectangle as needing to be updated.
- [var needsDisplayOnBoundsChange: Bool](./needsdisplayonboundschange.md)
  A Boolean indicating whether the layer contents must be updated when its bounds rectangle changes.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Initiates the update process for a layer if it is currently marked as needing an update.
- [func needsDisplay() -> Bool](./needsdisplay%28%29.md)
  Returns a Boolean indicating whether the layer has been marked as needing an update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/needsdisplay(forkey:))*