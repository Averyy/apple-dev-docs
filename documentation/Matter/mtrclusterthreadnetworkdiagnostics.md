# MTRClusterThreadNetworkDiagnostics

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
class MTRClusterThreadNetworkDiagnostics
```

```objc
@interface MTRClusterThreadNetworkDiagnostics : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterthreadnetworkdiagnostics/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterthreadnetworkdiagnostics/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveNetworkFaultsList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeactivenetworkfaultslist%28with%29.md)
- [func readAttributeActiveTimestamp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeactivetimestamp%28with%29.md)
- [func readAttributeAttachAttemptCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeattachattemptcount%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeattributelist%28with%29.md)
- [func readAttributeBetterPartitionAttachAttemptCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributebetterpartitionattachattemptcount%28with%29.md)
- [func readAttributeChannel(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributechannel%28with%29.md)
- [func readAttributeChannelPage0Mask(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributechannelpage0mask%28with%29.md)
- [func readAttributeChildRoleCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributechildrolecount%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeclusterrevision%28with%29.md)
- [func readAttributeDataVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributedataversion%28with%29.md)
- [func readAttributeDelay(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributedelay%28with%29.md)
- [func readAttributeDetachedRoleCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributedetachedrolecount%28with%29.md)
- [func readAttributeExtendedPanId(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeextendedpanid%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLeaderRoleCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeleaderrolecount%28with%29.md)
- [func readAttributeLeaderRouterId(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeleaderrouterid%28with%29.md)
- [func readAttributeMeshLocalPrefix(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributemeshlocalprefix%28with%29.md)
- [func readAttributeNeighborTable(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeneighbortable%28with%29.md)
- [func readAttributeNeighborTableList(with: MTRReadParams?) -> [String : Any]](./mtrclusterthreadnetworkdiagnostics/readattributeneighbortablelist%28with%29.md)
- [func readAttributeNetworkName(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributenetworkname%28with%29.md)
- [func readAttributeOperationalDatasetComponents(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeoperationaldatasetcomponents%28with%29.md)
- [func readAttributeOverrunCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeoverruncount%28with%29.md)
- [func readAttributePanId(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributepanid%28with%29.md)
- [func readAttributeParentChangeCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeparentchangecount%28with%29.md)
- [func readAttributePartitionId(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributepartitionid%28with%29.md)
- [func readAttributePartitionIdChangeCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributepartitionidchangecount%28with%29.md)
- [func readAttributePendingTimestamp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributependingtimestamp%28with%29.md)
- [func readAttributeRouteTable(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeroutetable%28with%29.md)
- [func readAttributeRouteTableList(with: MTRReadParams?) -> [String : Any]](./mtrclusterthreadnetworkdiagnostics/readattributeroutetablelist%28with%29.md)
- [func readAttributeRouterRoleCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerouterrolecount%28with%29.md)
- [func readAttributeRoutingRole(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeroutingrole%28with%29.md)
- [func readAttributeRxAddressFilteredCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxaddressfilteredcount%28with%29.md)
- [func readAttributeRxBeaconCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxbeaconcount%28with%29.md)
- [func readAttributeRxBeaconRequestCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxbeaconrequestcount%28with%29.md)
- [func readAttributeRxBroadcastCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxbroadcastcount%28with%29.md)
- [func readAttributeRxDataCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxdatacount%28with%29.md)
- [func readAttributeRxDataPollCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxdatapollcount%28with%29.md)
- [func readAttributeRxDestAddrFilteredCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxdestaddrfilteredcount%28with%29.md)
- [func readAttributeRxDuplicatedCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxduplicatedcount%28with%29.md)
- [func readAttributeRxErrFcsCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxerrfcscount%28with%29.md)
- [func readAttributeRxErrInvalidSrcAddrCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxerrinvalidsrcaddrcount%28with%29.md)
- [func readAttributeRxErrNoFrameCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxerrnoframecount%28with%29.md)
- [func readAttributeRxErrOtherCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxerrothercount%28with%29.md)
- [func readAttributeRxErrSecCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxerrseccount%28with%29.md)
- [func readAttributeRxErrUnknownNeighborCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxerrunknownneighborcount%28with%29.md)
- [func readAttributeRxOtherCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxothercount%28with%29.md)
- [func readAttributeRxTotalCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxtotalcount%28with%29.md)
- [func readAttributeRxUnicastCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributerxunicastcount%28with%29.md)
- [func readAttributeSecurityPolicy(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributesecuritypolicy%28with%29.md)
- [func readAttributeStableDataVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributestabledataversion%28with%29.md)
- [func readAttributeTxAckRequestedCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxackrequestedcount%28with%29.md)
- [func readAttributeTxAckedCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxackedcount%28with%29.md)
- [func readAttributeTxBeaconCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxbeaconcount%28with%29.md)
- [func readAttributeTxBeaconRequestCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxbeaconrequestcount%28with%29.md)
- [func readAttributeTxBroadcastCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxbroadcastcount%28with%29.md)
- [func readAttributeTxDataCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxdatacount%28with%29.md)
- [func readAttributeTxDataPollCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxdatapollcount%28with%29.md)
- [func readAttributeTxDirectMaxRetryExpiryCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxdirectmaxretryexpirycount%28with%29.md)
- [func readAttributeTxErrAbortCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxerrabortcount%28with%29.md)
- [func readAttributeTxErrBusyChannelCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxerrbusychannelcount%28with%29.md)
- [func readAttributeTxErrCcaCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxerrccacount%28with%29.md)
- [func readAttributeTxIndirectMaxRetryExpiryCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxindirectmaxretryexpirycount%28with%29.md)
- [func readAttributeTxNoAckRequestedCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxnoackrequestedcount%28with%29.md)
- [func readAttributeTxOtherCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxothercount%28with%29.md)
- [func readAttributeTxRetryCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxretrycount%28with%29.md)
- [func readAttributeTxTotalCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxtotalcount%28with%29.md)
- [func readAttributeTxUnicastCount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributetxunicastcount%28with%29.md)
- [func readAttributeWeighting(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthreadnetworkdiagnostics/readattributeweighting%28with%29.md)
- [func resetCounts(with: MTRThreadNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthreadnetworkdiagnostics/resetcounts%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func resetCounts(with: MTRThreadNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterthreadnetworkdiagnostics/resetcounts%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthreadnetworkdiagnostics/resetcounts%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterthreadnetworkdiagnostics/resetcounts%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)

## Relationships

### Inherits From
- [MTRGenericCluster](./mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthreadnetworkdiagnostics)*