# gpu

**Framework**: Background Tasks  
**Kind**: property

An option that indicates a long-running task requires the GPU.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
static var gpu: BGContinuedProcessingTaskRequest.Resources { get }
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

The system requires your app to have the [`Background GPU Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.background-tasks.continued-processing.gpu) entitlement with a value of `true` to use the GPU in the background. To do that, enable the Background GPU Access capability on your app’s target. For more information about capabilities in Xcode, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

Not all devices support background GPU use. For more information, see [`Performing long-running tasks on iOS and iPadOS`](performing-long-running-tasks-on-ios-and-ipados.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources/gpu)*