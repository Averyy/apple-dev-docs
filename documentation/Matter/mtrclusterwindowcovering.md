# MTRClusterWindowCovering

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
class MTRClusterWindowCovering
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterwindowcovering/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterwindowcovering/init(device:endpointid:queue:).md)
### Instance Methods
- [func downOrClose(with: MTRWindowCoveringClusterDownOrCloseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/downorclose(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func downOrClose(with: MTRWindowCoveringClusterDownOrCloseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/downorclose(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func downOrClose(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/downorclose(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func downOrClose(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/downorclose(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func goToLiftPercentage(with: MTRWindowCoveringClusterGoToLiftPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/gotoliftpercentage(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func goToLiftPercentage(with: MTRWindowCoveringClusterGoToLiftPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/gotoliftpercentage(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func goToLiftValue(with: MTRWindowCoveringClusterGoToLiftValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/gotoliftvalue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func goToLiftValue(with: MTRWindowCoveringClusterGoToLiftValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/gotoliftvalue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func goToTiltPercentage(with: MTRWindowCoveringClusterGoToTiltPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/gototiltpercentage(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func goToTiltPercentage(with: MTRWindowCoveringClusterGoToTiltPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/gototiltpercentage(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func goToTiltValue(with: MTRWindowCoveringClusterGoToTiltValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/gototiltvalue(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func goToTiltValue(with: MTRWindowCoveringClusterGoToTiltValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/gototiltvalue(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeacceptedcommandlist(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeattributelist(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeclusterrevision(with:).md)
- [func readAttributeConfigStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeconfigstatus(with:).md)
- [func readAttributeCurrentPositionLift(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributecurrentpositionlift(with:).md)
- [func readAttributeCurrentPositionLiftPercent100ths(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributecurrentpositionliftpercent100ths(with:).md)
- [func readAttributeCurrentPositionLiftPercentage(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributecurrentpositionliftpercentage(with:).md)
- [func readAttributeCurrentPositionTilt(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributecurrentpositiontilt(with:).md)
- [func readAttributeCurrentPositionTiltPercent100ths(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributecurrentpositiontiltpercent100ths(with:).md)
- [func readAttributeCurrentPositionTiltPercentage(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributecurrentpositiontiltpercentage(with:).md)
- [func readAttributeEndProductType(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeendproducttype(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributegeneratedcommandlist(with:).md)
- [func readAttributeInstalledClosedLimitLift(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeinstalledclosedlimitlift(with:).md)
- [func readAttributeInstalledClosedLimitTilt(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeinstalledclosedlimittilt(with:).md)
- [func readAttributeInstalledOpenLimitLift(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeinstalledopenlimitlift(with:).md)
- [func readAttributeInstalledOpenLimitTilt(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeinstalledopenlimittilt(with:).md)
- [func readAttributeMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributemode(with:).md)
- [func readAttributeNumberOfActuationsLift(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributenumberofactuationslift(with:).md)
- [func readAttributeNumberOfActuationsTilt(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributenumberofactuationstilt(with:).md)
- [func readAttributeOperationalStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributeoperationalstatus(with:).md)
- [func readAttributePhysicalClosedLimitLift(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributephysicalclosedlimitlift(with:).md)
- [func readAttributePhysicalClosedLimitTilt(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributephysicalclosedlimittilt(with:).md)
- [func readAttributeSafetyStatus(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributesafetystatus(with:).md)
- [func readAttributeTargetPositionLiftPercent100ths(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributetargetpositionliftpercent100ths(with:).md)
- [func readAttributeTargetPositionTiltPercent100ths(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributetargetpositiontiltpercent100ths(with:).md)
- [func readAttributeType(with: MTRReadParams?) -> [String : Any]?](mtrclusterwindowcovering/readattributetype(with:).md)
- [func stopMotion(with: MTRWindowCoveringClusterStopMotionParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/stopmotion(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func stopMotion(with: MTRWindowCoveringClusterStopMotionParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/stopmotion(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func stopMotion(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/stopmotion(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func stopMotion(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/stopmotion(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func upOrOpen(with: MTRWindowCoveringClusterUpOrOpenParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/uporopen(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func upOrOpen(with: MTRWindowCoveringClusterUpOrOpenParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/uporopen(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func upOrOpen(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterwindowcovering/uporopen(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func upOrOpen(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterwindowcovering/uporopen(withexpectedvalues:expectedvalueinterval:completionhandler:).md)
- [func writeAttributeMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterwindowcovering/writeattributemode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterwindowcovering/writeattributemode(withvalue:expectedvalueinterval:params:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwindowcovering)*