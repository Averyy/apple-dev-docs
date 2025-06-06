# showShotLocations(_:)

**Framework**: RealityKit  
**Kind**: method

Shows the locations where shots have been taken. Example: ObjectCapturePointCloudView(session: mySession) .showShotLocations()

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
func showShotLocations(_ value: Bool = true) -> ObjectCapturePointCloudView
```

#### Discussion

It can also be passed a value if there is a state variable controlling it:

ObjectCapturePointCloudView(session: mySession) .showShotLocations(shouldShowShots)

Other modifiers can be chained to build the final view: ObjectCapturePointCloudView(session: mySession) .showShotLocations() .transition(.opacity)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturepointcloudview/showshotlocations(_:))*