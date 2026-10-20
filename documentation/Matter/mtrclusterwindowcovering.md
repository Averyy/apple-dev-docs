# MTRClusterWindowCovering

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
class MTRClusterWindowCovering
```

```objc
@interface MTRClusterWindowCovering : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterwindowcovering/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterwindowcovering/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func downOrClose(with: MTRWindowCoveringClusterDownOrCloseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/downorclose%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func downOrClose(with: MTRWindowCoveringClusterDownOrCloseParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/downorclose%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func downOrClose(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/downorclose%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func downOrClose(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/downorclose%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func goToLiftPercentage(with: MTRWindowCoveringClusterGoToLiftPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gotoliftpercentage%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func goToLiftPercentage(with: MTRWindowCoveringClusterGoToLiftPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gotoliftpercentage%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func goToLiftValue(with: MTRWindowCoveringClusterGoToLiftValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gotoliftvalue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func goToLiftValue(with: MTRWindowCoveringClusterGoToLiftValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gotoliftvalue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func goToTiltPercentage(with: MTRWindowCoveringClusterGoToTiltPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gototiltpercentage%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func goToTiltPercentage(with: MTRWindowCoveringClusterGoToTiltPercentageParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gototiltpercentage%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func goToTiltValue(with: MTRWindowCoveringClusterGoToTiltValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gototiltvalue%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func goToTiltValue(with: MTRWindowCoveringClusterGoToTiltValueParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/gototiltvalue%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeclusterrevision%28with%29.md)
- [func readAttributeConfigStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeconfigstatus%28with%29.md)
- [func readAttributeCurrentPositionLift(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributecurrentpositionlift%28with%29.md)
- [func readAttributeCurrentPositionLiftPercent100ths(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributecurrentpositionliftpercent100ths%28with%29.md)
- [func readAttributeCurrentPositionLiftPercentage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributecurrentpositionliftpercentage%28with%29.md)
- [func readAttributeCurrentPositionTilt(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributecurrentpositiontilt%28with%29.md)
- [func readAttributeCurrentPositionTiltPercent100ths(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributecurrentpositiontiltpercent100ths%28with%29.md)
- [func readAttributeCurrentPositionTiltPercentage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributecurrentpositiontiltpercentage%28with%29.md)
- [func readAttributeEndProductType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeendproducttype%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeInstalledClosedLimitLift(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeinstalledclosedlimitlift%28with%29.md)
- [func readAttributeInstalledClosedLimitTilt(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeinstalledclosedlimittilt%28with%29.md)
- [func readAttributeInstalledOpenLimitLift(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeinstalledopenlimitlift%28with%29.md)
- [func readAttributeInstalledOpenLimitTilt(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeinstalledopenlimittilt%28with%29.md)
- [func readAttributeMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributemode%28with%29.md)
- [func readAttributeNumberOfActuationsLift(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributenumberofactuationslift%28with%29.md)
- [func readAttributeNumberOfActuationsTilt(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributenumberofactuationstilt%28with%29.md)
- [func readAttributeOperationalStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributeoperationalstatus%28with%29.md)
- [func readAttributePhysicalClosedLimitLift(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributephysicalclosedlimitlift%28with%29.md)
- [func readAttributePhysicalClosedLimitTilt(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributephysicalclosedlimittilt%28with%29.md)
- [func readAttributeSafetyStatus(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributesafetystatus%28with%29.md)
- [func readAttributeTargetPositionLiftPercent100ths(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributetargetpositionliftpercent100ths%28with%29.md)
- [func readAttributeTargetPositionTiltPercent100ths(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributetargetpositiontiltpercent100ths%28with%29.md)
- [func readAttributeType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterwindowcovering/readattributetype%28with%29.md)
- [func stopMotion(with: MTRWindowCoveringClusterStopMotionParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/stopmotion%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func stopMotion(with: MTRWindowCoveringClusterStopMotionParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/stopmotion%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func stopMotion(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/stopmotion%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func stopMotion(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/stopmotion%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func upOrOpen(with: MTRWindowCoveringClusterUpOrOpenParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/uporopen%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func upOrOpen(with: MTRWindowCoveringClusterUpOrOpenParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/uporopen%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func upOrOpen(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterwindowcovering/uporopen%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func upOrOpen(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterwindowcovering/uporopen%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterwindowcovering/writeattributemode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterwindowcovering/writeattributemode%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterwindowcovering)*