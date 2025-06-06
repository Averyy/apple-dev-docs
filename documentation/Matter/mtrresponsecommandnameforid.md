# MTRResponseCommandNameForID(_:_:)

**Framework**: Matter  
**Kind**: func

Resolve Matter response (server to client) command IDs into a descriptive string.

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
func MTRResponseCommandNameForID(_ clusterID: MTRClusterIDType, _ commandID: MTRCommandIDType) -> String!
```

#### Discussion

For unknown IDs, a string ‘<Unknown clusterID %d>’ (if the cluster ID is not known) or ‘<Unknown commandID %d>’ (if the cluster ID is known but the command ID is not known) will be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrresponsecommandnameforid(_:_:))*