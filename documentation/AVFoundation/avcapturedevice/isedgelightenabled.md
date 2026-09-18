# isEdgeLightEnabled

**Framework**: AVFoundation  
**Kind**: property

A class property indicating whether the Edge Light feature is currently enabled in Control Center.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+

## Declaration

```swift
class var isEdgeLightEnabled: Bool { get }
```

#### Discussion

This readonly property changes to reflect the Edge Light state in Control Center. It is key-value observable. On iOS, Edge Light only applies to video conferencing apps by default (apps that use “voip” as one of their UIBackgroundModes). Non video conferencing apps may opt in for Edge Light by adding the following key to their Info.plist: NSCameraEdgeLightEnabled 


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isedgelightenabled)*