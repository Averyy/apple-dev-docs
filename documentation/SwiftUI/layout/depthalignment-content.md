# depthAlignment(_:content:)

**Framework**: SwiftUI  
**Kind**: method

Creates a layout view with the specified depth alignment.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func depthAlignment<Content>(_ alignment: DepthAlignment, @ViewBuilder content: () -> Content) -> some View where Content : View
```

#### Discussion

Use `depthAlignment(_:content:)` to specify a depth guide for aligning subviews of this layout.

In the example below, the button to play the robot animation is aligned to the `.front` of the `HStack`.

```swift
   HStackLayout().depthAlignment(.front) {
       RobotModel()
       Button("Play animation") {
           playRobotAnimation()
       }
       .glassBackgroundEffect()
   }
```

## Parameters

- `alignment`: A   value to use for aligning layout’s   subviews


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/depthalignment(_:content:))*