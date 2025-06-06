# minimumDeploymentTarget

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The minimum deployment target to serialize the executable.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var minimumDeploymentTarget: String { get set }
```

#### Discussion

If not set, the package created will target the latest version of the `deploymentPlatform` set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutableserializationdescriptor/minimumdeploymenttarget)*