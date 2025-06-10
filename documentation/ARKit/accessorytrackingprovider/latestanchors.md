# latestAnchors

**Framework**: ARKit  
**Kind**: property

Get the latest accessory anchors seen by the provider. These could be used for `predictAnchor` The output array may be empty if the provider is not running or no accessory is tracked at the moment.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
final var latestAnchors: [AccessoryAnchor] { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider/latestanchors)*