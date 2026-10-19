# menuZone()

**Framework**: AppKit  
**Kind**: method

Returns the zone from which `NSMenu` objects should be allocated.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func menuZone() -> NSZone!
```

#### Return Value

The zone from which `NSMenu` objects should be allocated.

#### Discussion

This is left in for compatibility and always returns [`NSDefaultMallocZone`](https://developer.apple.com/documentation/foundation/nsdefaultmalloczone). It is not necessary to use this.

## See Also

- [func helpRequested(with: NSEvent)](nsmenu/helprequested(with:).md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menuzone())*