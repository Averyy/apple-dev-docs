# didLoad(_:)

**Framework**: SpriteKit  
**Kind**: method

A method called by SpriteKit after the reference node’s contents are loaded.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func didLoad(_ node: SKNode?)
```

#### Discussion

This method is called after the referenced content is added as a child of the reference node. Override this method in a subclass to implement custom loading behavior.

## Parameters

- `node`: The deserialized content’s root node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skreferencenode/didload(_:))*