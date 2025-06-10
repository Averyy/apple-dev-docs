# Background GPU Access

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement the system requires for a continuous background task to use the GPU.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

#### Discussion

This entitlement works with [`BGContinuedProcessingTask`](https://developer.apple.com/documentation/BackgroundTasks/BGContinuedProcessingTask), which allows your app’s critical work to complete even when the app goes into the background before the task finishes.

To enable GPU use in the task, add this entitlement to your app by adding the Background GPU Access capability to your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

For more information about continuous background tasks, see [`Performing long-running tasks on iOS and iPadOS`](https://developer.apple.com/documentation/BackgroundTasks/performing-long-running-tasks-on-ios-and-ipados).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu)*