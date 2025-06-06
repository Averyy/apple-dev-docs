# programIsOpaque(_:)

**Framework**: SceneKit  
**Kind**: method

Asks the delegate whether fragments rendered by a program are opaque.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func programIsOpaque(_ program: SCNProgram) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if all fragments rendered by the program are opaque; [`false`](https://developer.apple.com/documentation/swift/false) if the program renders fragments whose alpha value is less than `1.0`.

## Parameters

- `program`: The queried program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/programisopaque(_:))*