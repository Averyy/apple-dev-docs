# snapshot(saveToHDR:completion:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Takes a screenshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency func snapshot(saveToHDR: Bool, completion: @escaping (ARView.Image?) -> Void)
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func snapshot(saveToHDR: Bool, completion: @escaping (ARView.Image?) -> Void)
```

## See Also

### Taking a snapshot
- [func snapshot(saveToHDR: Bool, completion: (ARView.Image?) -> Void)](./snapshot%28savetohdr,completion%29-66jzu.md)
  Takes a screenshot.
- [typealias Image](./image.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/snapshot(savetohdr:completion:)-91ifk)*