# depthAlignment(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the depth alignment for this layout.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
func depthAlignment(_ alignment: DepthAlignment) -> some Layout
```

#### Discussion

Use `depthAlignment(_:)` to specify a depth guide for aligning subviews of this layout.

In the example below, the button to play the robot animation is aligned to the `.front` of the `HStack`.

```swift
   let depthStack = HStackLayout().depthAlignment(.front)
   depthStack {
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/layout/depthalignment(_:))*