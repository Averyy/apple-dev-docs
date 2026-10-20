# menuZone()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the zone from which `NSMenu` objects should be allocated.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

## Declaration

```swift
class func menuZone() -> NSZone!
```

```objc
+ (NSZone *) menuZone;
```

#### Return Value

The zone from which `NSMenu` objects should be allocated.

#### Discussion

This is left in for compatibility and always returns [`NSDefaultMallocZone`](../../Foundation/nsdefaultmalloczone.md). It is not necessary to use this.

## See Also

### Deprecated methods
- [func helpRequested(with: NSEvent)](./helprequested%28with%29.md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menuzone())*