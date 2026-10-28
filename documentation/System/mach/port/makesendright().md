# makeSendRight()

**Framework**: System  
**Kind**: method  
**Role**: Instance Method

Create a send right for a given receive right.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
func makeSendRight() -> Mach.Port<Mach.SendRight>
```

Available when `RightType` is `Mach.ReceiveRight`.

## Discussion

This increments the makeSendCount of the receive right.

This function will abort if the right could not be created. Callers may assert that a valid right is always returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/port/makesendright())*