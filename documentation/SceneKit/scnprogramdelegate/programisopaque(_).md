# programIsOpaque(_:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether fragments rendered by a program are opaque.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use the [`isOpaque`](../scnprogram/isopaque.md) property of the [`SCNProgram`](../scnprogram.md) object instead.

## Declaration

```swift
optional func programIsOpaque(_ program: SCNProgram) -> Bool
```

```objc
- (BOOL) programIsOpaque:(SCNProgram *) program;
```

## Return Value

[`true`](../../Swift/true.md) if all fragments rendered by the program are opaque; [`false`](../../Swift/false.md) if the program renders fragments whose alpha value is less than `1.0`.

## Parameters

- `program`: The queried program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/programisopaque(_:))*