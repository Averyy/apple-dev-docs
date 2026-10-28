# float2(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Returns an argument value representing the MSL value `float2(vector.dx, vector.dy)`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func float2(_ vector: CGVector) -> Shader.Argument
```

**Other overloads**:

```swift
@export(implementation)
static func float2(_ point: CGPoint) -> Shader.Argument
```

```swift
@export(implementation)
static func float2(_ size: CGSize) -> Shader.Argument
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shader/argument/float2(_:)-5hfgy)*