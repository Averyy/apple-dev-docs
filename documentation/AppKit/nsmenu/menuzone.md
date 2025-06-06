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

This is left in for compatibility and always returns doc://com.apple.documentation/documentation/foundation/1539819-nsdefaultmalloczone. It is not necessary to use this.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/menuzone())*