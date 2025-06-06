# descriptorClusters()

**Framework**: Matter  
**Kind**: method

Read all known attributes from descriptor clusters on all known endpoints.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
func descriptorClusters() -> [MTRAttributePath : [String : Any]]
```

#### Return Value

A dictionary with the paths of the attributes as keys and the data-values (as described in the documentation for MTRDeviceResponseHandler) as values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevice/descriptorclusters())*