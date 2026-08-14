# Background Inference

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that lets a background task run inference on the Neural Engine.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)



**Type**: boolean

**Default**: `NO`

#### Discussion

This entitlement works with [`BGContinuedProcessingTask`](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask), which lets your app’s critical inference work finish on the Neural Engine even when your app moves to the background before the task completes.

The system also requires the entitlement for any Neural Engine access while your app is in the background, regardless of whether it’s running a continued background task. You can perform inference with Core AI, Core ML, or Metal Performance Shaders Graph.

## See Also

- [Background GPU Access](entitlements/com.apple.developer.background-tasks.continued-processing.gpu.md)
  The entitlement the system requires for a continuous background task to use the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.inference)*