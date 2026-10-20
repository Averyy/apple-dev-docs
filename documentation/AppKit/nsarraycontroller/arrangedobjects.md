# arrangedObjects

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the receiver’s content objects arranged using [`arrange(_:)`](./arrange%28_%29.md).

**Availability**:
- macOS

## Declaration

```swift
var arrangedObjects: Any { get }
```

```objc
@property (strong, readonly) id arrangedObjects;
```

#### Discussion

This property is observable using key-value observing.

## See Also

### Arranging Objects
- [func arrange([Any]) -> [Any]](./arrange%28_%29.md)
  Returns a given array, appropriately sorted and filtered.
- [func rearrangeObjects()](./rearrangeobjects%28%29.md)
  Triggers filtering of the receiver’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsarraycontroller/arrangedobjects)*