# Background Inference

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that lets a background task run inference on the Neural Engine.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Details

- **Name**: `com.apple.developer.background-tasks.continued-processing.inference`
- **Type**: boolean



**Default**: `NO`

#### Discussion

This entitlement works with [`BGContinuedProcessingTask`](../../BackgroundTasks/bgcontinuedprocessingtask.md), which lets your app’s critical inference work finish on the Neural Engine even when your app moves to the background before the task completes.

The system also requires the entitlement for any Neural Engine access while your app is in the background, regardless of whether it’s running a continued background task. You can perform inference with Core AI, Core ML, or Metal Performance Shaders Graph.

## See Also

### Background tasks
- [Background GPU Access](./com.apple.developer.background-tasks.continued-processing.gpu.md)
  The entitlement the system requires for a continuous background task to use the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.inference)*