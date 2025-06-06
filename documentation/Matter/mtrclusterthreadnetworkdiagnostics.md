# MTRClusterThreadNetworkDiagnostics

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterthreadnetworkdiagnostics/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterthreadnetworkdiagnostics/init(device:endpointid:queue:).md)
### Instance Methods
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActiveNetworkFaultsList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeactivenetworkfaultslist(with:).md)
- [func readAttributeActiveTimestamp(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeactivetimestamp(with:).md)
- [func readAttributeAttachAttemptCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeattachattemptcount(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeattributelist(with:).md)
- [func readAttributeBetterPartitionAttachAttemptCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributebetterpartitionattachattemptcount(with:).md)
- [func readAttributeChannel(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributechannel(with:).md)
- [func readAttributeChannelPage0Mask(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributechannelpage0mask(with:).md)
- [func readAttributeChildRoleCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributechildrolecount(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeclusterrevision(with:).md)
- [func readAttributeDataVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributedataversion(with:).md)
- [func readAttributeDelay(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributedelay(with:).md)
- [func readAttributeDetachedRoleCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributedetachedrolecount(with:).md)
- [func readAttributeExtendedPanId(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeextendedpanid(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLeaderRoleCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeleaderrolecount(with:).md)
- [func readAttributeLeaderRouterId(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeleaderrouterid(with:).md)
- [func readAttributeMeshLocalPrefix(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributemeshlocalprefix(with:).md)
- [func readAttributeNeighborTable(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeneighbortable(with:).md)
- [func readAttributeNeighborTableList(with: MTRReadParams?) -> [String : Any]](mtrclusterthreadnetworkdiagnostics/readattributeneighbortablelist(with:).md)
- [func readAttributeNetworkName(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributenetworkname(with:).md)
- [func readAttributeOperationalDatasetComponents(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeoperationaldatasetcomponents(with:).md)
- [func readAttributeOverrunCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeoverruncount(with:).md)
- [func readAttributePanId(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributepanid(with:).md)
- [func readAttributeParentChangeCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeparentchangecount(with:).md)
- [func readAttributePartitionId(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributepartitionid(with:).md)
- [func readAttributePartitionIdChangeCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributepartitionidchangecount(with:).md)
- [func readAttributePendingTimestamp(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributependingtimestamp(with:).md)
- [func readAttributeRouteTable(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeroutetable(with:).md)
- [func readAttributeRouteTableList(with: MTRReadParams?) -> [String : Any]](mtrclusterthreadnetworkdiagnostics/readattributeroutetablelist(with:).md)
- [func readAttributeRouterRoleCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerouterrolecount(with:).md)
- [func readAttributeRoutingRole(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeroutingrole(with:).md)
- [func readAttributeRxAddressFilteredCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxaddressfilteredcount(with:).md)
- [func readAttributeRxBeaconCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxbeaconcount(with:).md)
- [func readAttributeRxBeaconRequestCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxbeaconrequestcount(with:).md)
- [func readAttributeRxBroadcastCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxbroadcastcount(with:).md)
- [func readAttributeRxDataCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxdatacount(with:).md)
- [func readAttributeRxDataPollCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxdatapollcount(with:).md)
- [func readAttributeRxDestAddrFilteredCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxdestaddrfilteredcount(with:).md)
- [func readAttributeRxDuplicatedCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxduplicatedcount(with:).md)
- [func readAttributeRxErrFcsCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxerrfcscount(with:).md)
- [func readAttributeRxErrInvalidSrcAddrCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxerrinvalidsrcaddrcount(with:).md)
- [func readAttributeRxErrNoFrameCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxerrnoframecount(with:).md)
- [func readAttributeRxErrOtherCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxerrothercount(with:).md)
- [func readAttributeRxErrSecCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxerrseccount(with:).md)
- [func readAttributeRxErrUnknownNeighborCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxerrunknownneighborcount(with:).md)
- [func readAttributeRxOtherCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxothercount(with:).md)
- [func readAttributeRxTotalCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxtotalcount(with:).md)
- [func readAttributeRxUnicastCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributerxunicastcount(with:).md)
- [func readAttributeSecurityPolicy(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributesecuritypolicy(with:).md)
- [func readAttributeStableDataVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributestabledataversion(with:).md)
- [func readAttributeTxAckRequestedCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxackrequestedcount(with:).md)
- [func readAttributeTxAckedCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxackedcount(with:).md)
- [func readAttributeTxBeaconCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxbeaconcount(with:).md)
- [func readAttributeTxBeaconRequestCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxbeaconrequestcount(with:).md)
- [func readAttributeTxBroadcastCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxbroadcastcount(with:).md)
- [func readAttributeTxDataCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxdatacount(with:).md)
- [func readAttributeTxDataPollCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxdatapollcount(with:).md)
- [func readAttributeTxDirectMaxRetryExpiryCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxdirectmaxretryexpirycount(with:).md)
- [func readAttributeTxErrAbortCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxerrabortcount(with:).md)
- [func readAttributeTxErrBusyChannelCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxerrbusychannelcount(with:).md)
- [func readAttributeTxErrCcaCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxerrccacount(with:).md)
- [func readAttributeTxIndirectMaxRetryExpiryCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxindirectmaxretryexpirycount(with:).md)
- [func readAttributeTxNoAckRequestedCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxnoackrequestedcount(with:).md)
- [func readAttributeTxOtherCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxothercount(with:).md)
- [func readAttributeTxRetryCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxretrycount(with:).md)
- [func readAttributeTxTotalCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxtotalcount(with:).md)
- [func readAttributeTxUnicastCount(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributetxunicastcount(with:).md)
- [func readAttributeWeighting(with: MTRReadParams?) -> [String : Any]?](mtrclusterthreadnetworkdiagnostics/readattributeweighting(with:).md)
- [func resetCounts(with: MTRThreadNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterthreadnetworkdiagnostics/resetcounts(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func resetCounts(with: MTRThreadNetworkDiagnosticsClusterResetCountsParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterthreadnetworkdiagnostics/resetcounts(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: MTRStatusCompletion)](mtrclusterthreadnetworkdiagnostics/resetcounts(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func resetCounts(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: MTRStatusCompletion)](mtrclusterthreadnetworkdiagnostics/resetcounts(withexpectedvalues:expectedvalueinterval:completionhandler:).md)

## Relationships

### Inherits From
- [MTRGenericCluster](mtrgenericcluster.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthreadnetworkdiagnostics)*