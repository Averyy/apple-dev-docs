# direction

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The directional input, if any, that a physical input source involves.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var direction: GCPhysicalInputSourceDirection { get }
```

```objc
@property (readonly) GCPhysicalInputSourceDirection direction;
```

## Discussion

If this property is `nil`, the physical input source doesn’t involve directional input.

## See Also

### Getting directions
- [struct GCPhysicalInputSourceDirection](../gcphysicalinputsourcedirection.md)
  The directions that a physical input source involves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputsource/direction)*