# com.apple.developer.sustained-execution

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether your app performs consistently when the system constrains it to a sustainable performance level.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+

#### Discussion

Instruct the system to limit burst performance to your app by adding this entitlement. Enabling this entitlement tells the system to maintain a consistent performance state over your app’s lifecycle on applicable devices. This allows your app to assess the performance of its workload at any time, including immediately after launch. When your app includes the entitlement:

- The system avoids letting your app run higher performance levels for a period of time, which avoids transitions to other levels later on.
- You don’t need to implement code to reassess the device’s ability to process your app’s workload after performance level transitions.

> **Note**:  For devices your app supports but don’t have this sustained execution feature, maintain a consistent level of performance over time on that device. You can do this by applying settings in your app that affect the GPU’s workload, such as resolution, frame rate, texture quality, and so on.

 For devices your app supports but don’t have this sustained execution feature, maintain a consistent level of performance over time on that device. You can do this by applying settings in your app that affect the GPU’s workload, such as resolution, frame rate, texture quality, and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.sustained-execution)*