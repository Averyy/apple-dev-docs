# custom(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a content brightness with a custom value.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func custom(_ value: Double) -> ImmersiveContentBrightness
```

## Parameters

- `value`: The value of the brightness. Provide a value between 0 and 1. Larger values correspond to a brighter environment.

## See Also

### Getting brightness levels
- [static let automatic: ImmersiveContentBrightness](./automatic.md)
  The default content brightness.
- [static let dark: ImmersiveContentBrightness](./dark.md)
  A dark content brightness.
- [static let dim: ImmersiveContentBrightness](./dim.md)
  A dimmed content brightness.
- [static let bright: ImmersiveContentBrightness](./bright.md)
  A bright content brightness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivecontentbrightness/custom(_:))*