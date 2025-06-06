# isHidden

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the system or the app presents the virtual interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

#### Discussion

To present your own virtual controller interface, set this property to [`true`](https://developer.apple.com/documentation/swift/true). Then when the state of controls in your interface changes, use the [`GCVirtualController`](gcvirtualcontroller.md) [`setValue(_:forButtonElement:)`](gcvirtualcontroller/setvalue(_:forbuttonelement:).md) and [`setPosition(_:forDirectionPadElement:)`](gcvirtualcontroller/setposition(_:fordirectionpadelement:).md) methods to update the corresponding elements.

The default value is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/configuration/ishidden)*