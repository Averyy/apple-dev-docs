# MTREventNameForID(_:_:)

**Framework**: Matter  
**Kind**: func

Resolve Matter event IDs into a descriptive string.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
func MTREventNameForID(_ clusterID: MTRClusterIDType, _ eventID: MTREventIDType) -> String!
```

#### Discussion

For unknown IDs, a string ‘<Unknown clusterID %d>’ (if the cluster ID is not known) or ‘<Unknown eventID %d>’ (if the cluster ID is known but the event ID is not known) will be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtreventnameforid(_:_:))*