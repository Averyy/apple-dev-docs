# openAppWhenRun

**Framework**: Swift  
**Kind**: property

A boolean property that tells the system to consider the app intent even if its app is not in the foreground.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var openAppWhenRun: Bool { get }
```

#### Discussion

This property is deprecated, use [`supportedModes`](never/supportedmodes.md) instead. For backward compatibility, provide `openAppWhenRun` in an extension, for example:

```swift
@available(*, deprecated)
extension OrderSoupIntent {
    static var openAppWhenRun: Bool { true }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/never/openappwhenrun)*