# Background GPU Access

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The entitlement the system requires for a continuous background task to use the GPU.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Details

- **Name**: `com.apple.developer.background-tasks.continued-processing.gpu`
- **Type**: boolean



**Default**: `NO`

#### Discussion

This entitlement works with [`BGContinuedProcessingTask`](../../BackgroundTasks/bgcontinuedprocessingtask.md), which allows your app’s critical work to complete even when the app goes into the background before the task finishes.

To enable GPU use in the task, add this entitlement to your app by adding the Background GPU Access capability to your target in Xcode. For more information, see [Adding capabilities to your app](../../Xcode/adding-capabilities-to-your-app.md).

For more information about continuous background tasks, see [Performing long-running tasks on iOS and iPadOS](../../BackgroundTasks/performing-long-running-tasks-on-ios-and-ipados.md).

## See Also

### Background tasks
- [Background Inference](./com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu)*