# Background GPU Access

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement the system requires for a continuous background task to use the GPU.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+



**Type**: boolean

**Default**: `NO`

#### Discussion

This entitlement works with [`BGContinuedProcessingTask`](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask), which allows your app’s critical work to complete even when the app goes into the background before the task finishes.

To enable GPU use in the task, add this entitlement to your app by adding the Background GPU Access capability to your target in Xcode. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

For more information about continuous background tasks, see [`Performing long-running tasks on iOS and iPadOS`](https://developer.apple.com/documentation/backgroundtasks/performing-long-running-tasks-on-ios-and-ipados).

## See Also

- [Background Inference](entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu)*