# setValue(_:)

**Framework**: Game Controller  
**Kind**: method

Sets the pressure value of a snapshot of a button.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setValue(_ value: Float)
```

#### Discussion

This method does nothing if the associated controller isn’t a snapshot (its [`isSnapshot`](gccontroller/issnapshot.md) property is [`false`](https://developer.apple.com/documentation/Swift/false)`)`.

## Parameters

- `value`: A normalized number between   (minimum pressure) and   (maximum pressure).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerbuttoninput/setvalue(_:))*