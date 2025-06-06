# shouldScanNetworks

**Framework**: MatterSupport  
**Kind**: property

A flag that indicates whether to receive network scan results.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
var shouldScanNetworks: Bool
```

#### Discussion

The app receives the network scan results, or an empty list if no scan occurred. Even if the property is set to `true`, the scan may not occur if the accessory doesn’t support scanning.

## See Also

- [func perform() async throws](matteradddevicerequest/perform.md)
  Launch the user interface to set up a Matter device in the ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/shouldscannetworks)*