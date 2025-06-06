# localVelocity

**Framework**: SwiftUI  
**Kind**: property

The represented gesture recognizer’s current velocity in the coordinate space of the SwiftUI view it’s attached to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
var localVelocity: CGPoint? { get }
```

#### Discussion

If the gesture recognizer does not implement a `velocityInView:` method, returns nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uigesturerecognizerrepresentablecoordinatespaceconverter/localvelocity)*