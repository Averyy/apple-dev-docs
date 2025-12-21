# wantsPriorityOverSystemBehavior

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the key command takes precedence over text input or focus movements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var wantsPriorityOverSystemBehavior: Bool { get set }
```

#### Discussion

In iOS 15 and later, the system delivers physical keyboard events to the text input or focus systems first. If those systems don’t handle the keyboard input, the system delivers the events to your app’s key commands. This delivery order lets the system handle keyboard events that might affect other parts of the user experience. If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the system reverses that order and delivers events to your key commands first and then to the text input and focus systems. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

Prior to iOS 15, the system delivered keyboard events to your key command objects first, and then to the text input or focus systems. If your app links against iOS 14 SDK or earlier, your app retains that behavior, even when running on iOS 15 or later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeycommand/wantspriorityoversystembehavior)*