# encoderExecutionStatus

**Framework**: Metal  
**Kind**: property

An option that instructs a command buffer to save additional details about a GPU runtime error.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static var encoderExecutionStatus: MTLCommandBufferErrorOption { get }
```

#### Discussion

You can set this option to a command buffer descriptor’s [`errorOptions`](mtlcommandbufferdescriptor/erroroptions.md) property.

> **Note**:  Enabling this option can slightly reduce your app’s CPU runtime performance.

 Enabling this option can slightly reduce your app’s CPU runtime performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererroroption/encoderexecutionstatus)*