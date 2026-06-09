# clusterInitiatorAddress

**Framework**: Nearby Interaction  
**Kind**: property

The address of the initiator anchor within the same cluster.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var clusterInitiatorAddress: Int { get }
```

#### Discussion

In DL-TDOA deployments, anchors organize into clusters. An anchor cluster contains an initiator anchor and one or more responder anchors. The initiator coordinates a ranging sequence by sending an initial poll message.

Use this property to group measurements from anchors that belong to the same cluster. Measurements with the same value for this property originate from anchors in the same cluster, even if their individual [`address`](nidltdoameasurement/address.md) differs.

##### Group Measurements By Cluster

To process measurements from related anchors together, group the measurements by cluster:

```swift
func session(_ session: NISession, didUpdateDLTDOA measurements: [NIDLTDOAMeasurement]) {
    // Group measurements by cluster.
    let clusters = Dictionary(grouping: measurements) { $0.clusterInitiatorAddress }
    
    for (initiatorAddress, clusterMeasurements) in clusters {
        print("Cluster \(initiatorAddress) has \(clusterMeasurements.count) measurements.")
        // Process measurements from this cluster together.
        calculatePosition(from: clusterMeasurements)
    }
}
```

## See Also

- [var address: Int](nidltdoameasurement/address.md)
  A value that uniquely identifies an anchor in a tracked area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/clusterinitiatoraddress)*