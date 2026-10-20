# MTRClusterThermostat

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
class MTRClusterThermostat
```

```objc
@interface MTRClusterThermostat : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterthermostat/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterthermostat/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func clearWeeklySchedule(with: MTRThermostatClusterClearWeeklyScheduleParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthermostat/clearweeklyschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearWeeklySchedule(with: MTRThermostatClusterClearWeeklyScheduleParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterthermostat/clearweeklyschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func clearWeeklySchedule(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthermostat/clearweeklyschedule%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func clearWeeklySchedule(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterthermostat/clearweeklyschedule%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getWeeklySchedule(with: MTRThermostatClusterGetWeeklyScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThermostatClusterGetWeeklyScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterthermostat/getweeklyschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getWeeklySchedule(with: MTRThermostatClusterGetWeeklyScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRThermostatClusterGetWeeklyScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterthermostat/getweeklyschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeACCapacity(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeaccapacity%28with%29.md)
- [func readAttributeACCapacityformat(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeaccapacityformat%28with%29.md)
- [func readAttributeACCoilTemperature(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeaccoiltemperature%28with%29.md)
- [func readAttributeACCompressorType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeaccompressortype%28with%29.md)
- [func readAttributeACErrorCode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeacerrorcode%28with%29.md)
- [func readAttributeACLouverPosition(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeaclouverposition%28with%29.md)
- [func readAttributeACRefrigerantType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeacrefrigeranttype%28with%29.md)
- [func readAttributeACType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeactype%28with%29.md)
- [func readAttributeAbsMaxCoolSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeabsmaxcoolsetpointlimit%28with%29.md)
- [func readAttributeAbsMaxHeatSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeabsmaxheatsetpointlimit%28with%29.md)
- [func readAttributeAbsMinCoolSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeabsmincoolsetpointlimit%28with%29.md)
- [func readAttributeAbsMinHeatSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeabsminheatsetpointlimit%28with%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeattributelist%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeclusterrevision%28with%29.md)
- [func readAttributeControlSequenceOfOperation(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributecontrolsequenceofoperation%28with%29.md)
- [func readAttributeEmergencyHeatDelta(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeemergencyheatdelta%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeHVACSystemTypeConfiguration(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributehvacsystemtypeconfiguration%28with%29.md)
- [func readAttributeLocalTemperature(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributelocaltemperature%28with%29.md)
- [func readAttributeLocalTemperatureCalibration(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributelocaltemperaturecalibration%28with%29.md)
- [func readAttributeMaxCoolSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributemaxcoolsetpointlimit%28with%29.md)
- [func readAttributeMaxHeatSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributemaxheatsetpointlimit%28with%29.md)
- [func readAttributeMinCoolSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributemincoolsetpointlimit%28with%29.md)
- [func readAttributeMinHeatSetpointLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeminheatsetpointlimit%28with%29.md)
- [func readAttributeMinSetpointDeadBand(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeminsetpointdeadband%28with%29.md)
- [func readAttributeNumberOfDailyTransitions(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributenumberofdailytransitions%28with%29.md)
- [func readAttributeNumberOfWeeklyTransitions(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributenumberofweeklytransitions%28with%29.md)
- [func readAttributeOccupancy(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeoccupancy%28with%29.md)
- [func readAttributeOccupiedCoolingSetpoint(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeoccupiedcoolingsetpoint%28with%29.md)
- [func readAttributeOccupiedHeatingSetpoint(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeoccupiedheatingsetpoint%28with%29.md)
- [func readAttributeOccupiedSetback(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeoccupiedsetback%28with%29.md)
- [func readAttributeOccupiedSetbackMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeoccupiedsetbackmax%28with%29.md)
- [func readAttributeOccupiedSetbackMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeoccupiedsetbackmin%28with%29.md)
- [func readAttributeOutdoorTemperature(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeoutdoortemperature%28with%29.md)
- [func readAttributePICoolingDemand(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributepicoolingdemand%28with%29.md)
- [func readAttributePIHeatingDemand(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributepiheatingdemand%28with%29.md)
- [func readAttributeRemoteSensing(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeremotesensing%28with%29.md)
- [func readAttributeSetpointChangeAmount(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributesetpointchangeamount%28with%29.md)
- [func readAttributeSetpointChangeSource(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributesetpointchangesource%28with%29.md)
- [func readAttributeSetpointChangeSourceTimestamp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributesetpointchangesourcetimestamp%28with%29.md)
- [func readAttributeStartOfWeek(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributestartofweek%28with%29.md)
- [func readAttributeSystemMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributesystemmode%28with%29.md)
- [func readAttributeTemperatureSetpointHold(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributetemperaturesetpointhold%28with%29.md)
- [func readAttributeTemperatureSetpointHoldDuration(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributetemperaturesetpointholdduration%28with%29.md)
- [func readAttributeThermostatProgrammingOperationMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributethermostatprogrammingoperationmode%28with%29.md)
- [func readAttributeThermostatRunningMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributethermostatrunningmode%28with%29.md)
- [func readAttributeThermostatRunningState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributethermostatrunningstate%28with%29.md)
- [func readAttributeUnoccupiedCoolingSetpoint(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeunoccupiedcoolingsetpoint%28with%29.md)
- [func readAttributeUnoccupiedHeatingSetpoint(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeunoccupiedheatingsetpoint%28with%29.md)
- [func readAttributeUnoccupiedSetback(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeunoccupiedsetback%28with%29.md)
- [func readAttributeUnoccupiedSetbackMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeunoccupiedsetbackmax%28with%29.md)
- [func readAttributeUnoccupiedSetbackMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeunoccupiedsetbackmin%28with%29.md)
- [func setWeeklyScheduleWith(MTRThermostatClusterSetWeeklyScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthermostat/setweeklyschedulewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setWeeklyScheduleWith(MTRThermostatClusterSetWeeklyScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterthermostat/setweeklyschedulewith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func setpointRaiseLower(with: MTRThermostatClusterSetpointRaiseLowerParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthermostat/setpointraiselower%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setpointRaiseLower(with: MTRThermostatClusterSetpointRaiseLowerParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterthermostat/setpointraiselower%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeACCapacity(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeaccapacity%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeACCapacity(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeaccapacity%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeACCapacityformat(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeaccapacityformat%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeACCapacityformat(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeaccapacityformat%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeACCompressorType(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeaccompressortype%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeACCompressorType(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeaccompressortype%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeACErrorCode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeacerrorcode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeACErrorCode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeacerrorcode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeACLouverPosition(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeaclouverposition%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeACLouverPosition(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeaclouverposition%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeACRefrigerantType(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeacrefrigeranttype%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeACRefrigerantType(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeacrefrigeranttype%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeACType(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeactype%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeACType(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeactype%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeControlSequenceOfOperation(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributecontrolsequenceofoperation%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeControlSequenceOfOperation(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributecontrolsequenceofoperation%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeEmergencyHeatDelta(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeemergencyheatdelta%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeEmergencyHeatDelta(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeemergencyheatdelta%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeHVACSystemTypeConfiguration(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributehvacsystemtypeconfiguration%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeHVACSystemTypeConfiguration(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributehvacsystemtypeconfiguration%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLocalTemperatureCalibration(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributelocaltemperaturecalibration%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLocalTemperatureCalibration(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributelocaltemperaturecalibration%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeMaxCoolSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributemaxcoolsetpointlimit%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMaxCoolSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributemaxcoolsetpointlimit%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeMaxHeatSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributemaxheatsetpointlimit%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMaxHeatSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributemaxheatsetpointlimit%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeMinCoolSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributemincoolsetpointlimit%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMinCoolSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributemincoolsetpointlimit%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeMinHeatSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeminheatsetpointlimit%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMinHeatSetpointLimit(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeminheatsetpointlimit%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeMinSetpointDeadBand(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeminsetpointdeadband%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeMinSetpointDeadBand(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeminsetpointdeadband%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOccupiedCoolingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeoccupiedcoolingsetpoint%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOccupiedCoolingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeoccupiedcoolingsetpoint%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOccupiedHeatingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeoccupiedheatingsetpoint%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOccupiedHeatingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeoccupiedheatingsetpoint%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOccupiedSetback(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeoccupiedsetback%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOccupiedSetback(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeoccupiedsetback%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRemoteSensing(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeremotesensing%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRemoteSensing(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeremotesensing%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeSystemMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributesystemmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSystemMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributesystemmode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeTemperatureSetpointHold(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributetemperaturesetpointhold%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeTemperatureSetpointHold(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributetemperaturesetpointhold%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeTemperatureSetpointHoldDuration(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributetemperaturesetpointholdduration%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeTemperatureSetpointHoldDuration(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributetemperaturesetpointholdduration%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeThermostatProgrammingOperationMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributethermostatprogrammingoperationmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeThermostatProgrammingOperationMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributethermostatprogrammingoperationmode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeUnoccupiedCoolingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeunoccupiedcoolingsetpoint%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUnoccupiedCoolingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeunoccupiedcoolingsetpoint%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeUnoccupiedHeatingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeunoccupiedheatingsetpoint%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUnoccupiedHeatingSetpoint(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeunoccupiedheatingsetpoint%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeUnoccupiedSetback(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeunoccupiedsetback%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUnoccupiedSetback(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeunoccupiedsetback%28withvalue,expectedvalueinterval,params%29.md)
- [func atomicRequest(with: MTRThermostatClusterAtomicRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRThermostatClusterAtomicResponseParams?, (any Error)?) -> Void)](./mtrclusterthermostat/atomicrequest%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeActivePresetHandle(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeactivepresethandle%28with%29.md)
- [func readAttributeActiveScheduleHandle(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeactiveschedulehandle%28with%29.md)
- [func readAttributeNumberOfPresets(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributenumberofpresets%28with%29.md)
- [func readAttributeNumberOfScheduleTransitionPerDay(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributenumberofscheduletransitionperday%28with%29.md)
- [func readAttributeNumberOfScheduleTransitions(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributenumberofscheduletransitions%28with%29.md)
- [func readAttributeNumberOfSchedules(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributenumberofschedules%28with%29.md)
- [func readAttributePresetTypes(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributepresettypes%28with%29.md)
- [func readAttributePresets(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributepresets%28with%29.md)
- [func readAttributeScheduleTypes(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributescheduletypes%28with%29.md)
- [func readAttributeSchedules(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributeschedules%28with%29.md)
- [func readAttributeSetpointHoldExpiryTimestamp(with: MTRReadParams?) -> [String : Any]?](./mtrclusterthermostat/readattributesetpointholdexpirytimestamp%28with%29.md)
- [func setActivePresetRequestWith(MTRThermostatClusterSetActivePresetRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthermostat/setactivepresetrequestwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setActiveScheduleRequestWith(MTRThermostatClusterSetActiveScheduleRequestParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterthermostat/setactiveschedulerequestwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func writeAttributePresets(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributepresets%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributePresets(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributepresets%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeSchedules(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterthermostat/writeattributeschedules%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSchedules(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterthermostat/writeattributeschedules%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterthermostat)*