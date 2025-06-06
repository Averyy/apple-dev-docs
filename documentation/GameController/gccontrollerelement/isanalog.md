# isAnalog

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the element provides analog data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isAnalog: Bool { get }
```

## Mentions

- [Letting players use their second-generation Siri Remote as a game controller](letting-players-use-their-second-generation-siri-remote-as-a-game-controller.md)

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/swift/true), the input value defined by the element can return a range (from a minimum to maximum) of possible values. For example, this element might be a pressure-sensitive button or an axis of a thumbstick that allows for a range of physical movement. If this property is [`false`](https://developer.apple.com/documentation/swift/false), the input value is a discrete value, such as `0` if the element is off, and `1` if the element is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/isanalog)*