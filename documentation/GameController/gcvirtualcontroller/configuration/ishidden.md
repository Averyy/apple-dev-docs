# isHidden

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system or the app presents the virtual interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, getter=isHidden) BOOL hidden;
```

## Discussion

To present your own virtual controller interface, set this property to [`true`](../../../Swift/true.md). Then when the state of controls in your interface changes, use the [`GCVirtualController`](../../gcvirtualcontroller.md) [`setValue(_:forButtonElement:)`](../setvalue%28_,forbuttonelement%29.md) and [`setPosition(_:forDirectionPadElement:)`](../setposition%28_,fordirectionpadelement%29.md) methods to update the corresponding elements.

The default value is [`false`](../../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcvirtualcontroller/configuration/ishidden)*