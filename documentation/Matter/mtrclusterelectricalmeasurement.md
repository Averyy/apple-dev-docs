# MTRClusterElectricalMeasurement

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.1+ - Deprecated in 18.2
- iPadOS 16.1+ - Deprecated in 18.2
- Mac Catalyst 16.1+ - Deprecated in 18.2
- macOS 13.0+ - Deprecated in 15.2
- tvOS 16.1+ - Deprecated in 18.2
- visionOS 1.0+ - Deprecated in 2.2
- watchOS 9.1+ - Deprecated in 11.2

> **Deprecated**: ElectricalMeasurement is deprecated and will be removed

## Declaration

```swift
class MTRClusterElectricalMeasurement
```

```objc
@interface MTRClusterElectricalMeasurement : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterelectricalmeasurement/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterelectricalmeasurement/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func getProfileCommand(with: MTRElectricalMeasurementClusterGetMeasurementProfileCommandParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterelectricalmeasurement/getprofilecommand%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getProfileCommand(with: MTRElectricalMeasurementClusterGetMeasurementProfileCommandParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterelectricalmeasurement/getprofilecommand%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getProfileInfoCommand(with: MTRElectricalMeasurementClusterGetProfileInfoCommandParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterelectricalmeasurement/getprofileinfocommand%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getProfileInfoCommand(with: MTRElectricalMeasurementClusterGetProfileInfoCommandParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterelectricalmeasurement/getprofileinfocommand%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getProfileInfoCommand(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterelectricalmeasurement/getprofileinfocommand%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func getProfileInfoCommand(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterelectricalmeasurement/getprofileinfocommand%28withexpectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func readAttributeAcActivePowerOverload(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacactivepoweroverload%28with%29.md)
- [func readAttributeAcCurrentDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaccurrentdivisor%28with%29.md)
- [func readAttributeAcCurrentMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaccurrentmultiplier%28with%29.md)
- [func readAttributeAcCurrentOverload(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaccurrentoverload%28with%29.md)
- [func readAttributeAcFrequency(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacfrequency%28with%29.md)
- [func readAttributeAcFrequencyDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacfrequencydivisor%28with%29.md)
- [func readAttributeAcFrequencyMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacfrequencymax%28with%29.md)
- [func readAttributeAcFrequencyMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacfrequencymin%28with%29.md)
- [func readAttributeAcFrequencyMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacfrequencymultiplier%28with%29.md)
- [func readAttributeAcOverloadAlarmsMask(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacoverloadalarmsmask%28with%29.md)
- [func readAttributeAcPowerDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacpowerdivisor%28with%29.md)
- [func readAttributeAcPowerMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacpowermultiplier%28with%29.md)
- [func readAttributeAcReactivePowerOverload(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacreactivepoweroverload%28with%29.md)
- [func readAttributeAcVoltageDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacvoltagedivisor%28with%29.md)
- [func readAttributeAcVoltageMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacvoltagemultiplier%28with%29.md)
- [func readAttributeAcVoltageOverload(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacvoltageoverload%28with%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActiveCurrentPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivecurrentphaseb%28with%29.md)
- [func readAttributeActiveCurrentPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivecurrentphasec%28with%29.md)
- [func readAttributeActivePower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepower%28with%29.md)
- [func readAttributeActivePowerMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowermax%28with%29.md)
- [func readAttributeActivePowerMaxPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowermaxphaseb%28with%29.md)
- [func readAttributeActivePowerMaxPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowermaxphasec%28with%29.md)
- [func readAttributeActivePowerMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowermin%28with%29.md)
- [func readAttributeActivePowerMinPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowerminphaseb%28with%29.md)
- [func readAttributeActivePowerMinPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowerminphasec%28with%29.md)
- [func readAttributeActivePowerPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowerphaseb%28with%29.md)
- [func readAttributeActivePowerPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeactivepowerphasec%28with%29.md)
- [func readAttributeApparentPower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeapparentpower%28with%29.md)
- [func readAttributeApparentPowerPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeapparentpowerphaseb%28with%29.md)
- [func readAttributeApparentPowerPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeapparentpowerphasec%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeattributelist%28with%29.md)
- [func readAttributeAverageRmsOverVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsovervoltage%28with%29.md)
- [func readAttributeAverageRmsOverVoltageCounterPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsovervoltagecounterphaseb%28with%29.md)
- [func readAttributeAverageRmsOverVoltageCounterPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsovervoltagecounterphasec%28with%29.md)
- [func readAttributeAverageRmsUnderVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsundervoltage%28with%29.md)
- [func readAttributeAverageRmsUnderVoltageCounter(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsundervoltagecounter%28with%29.md)
- [func readAttributeAverageRmsUnderVoltageCounterPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsundervoltagecounterphaseb%28with%29.md)
- [func readAttributeAverageRmsUnderVoltageCounterPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsundervoltagecounterphasec%28with%29.md)
- [func readAttributeAverageRmsVoltageMeasurementPeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsvoltagemeasurementperiod%28with%29.md)
- [func readAttributeAverageRmsVoltageMeasurementPeriodPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsvoltagemeasurementperiodphaseb%28with%29.md)
- [func readAttributeAverageRmsVoltageMeasurementPeriodPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeaveragermsvoltagemeasurementperiodphasec%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeclusterrevision%28with%29.md)
- [func readAttributeCurrentOverload(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributecurrentoverload%28with%29.md)
- [func readAttributeDcCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedccurrent%28with%29.md)
- [func readAttributeDcCurrentDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedccurrentdivisor%28with%29.md)
- [func readAttributeDcCurrentMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedccurrentmax%28with%29.md)
- [func readAttributeDcCurrentMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedccurrentmin%28with%29.md)
- [func readAttributeDcCurrentMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedccurrentmultiplier%28with%29.md)
- [func readAttributeDcPower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcpower%28with%29.md)
- [func readAttributeDcPowerDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcpowerdivisor%28with%29.md)
- [func readAttributeDcPowerMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcpowermax%28with%29.md)
- [func readAttributeDcPowerMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcpowermin%28with%29.md)
- [func readAttributeDcPowerMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcpowermultiplier%28with%29.md)
- [func readAttributeDcVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcvoltage%28with%29.md)
- [func readAttributeDcVoltageDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcvoltagedivisor%28with%29.md)
- [func readAttributeDcVoltageMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcvoltagemax%28with%29.md)
- [func readAttributeDcVoltageMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcvoltagemin%28with%29.md)
- [func readAttributeDcVoltageMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributedcvoltagemultiplier%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeHarmonicCurrentMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeharmoniccurrentmultiplier%28with%29.md)
- [func readAttributeInstantaneousActiveCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeinstantaneousactivecurrent%28with%29.md)
- [func readAttributeInstantaneousLineCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeinstantaneouslinecurrent%28with%29.md)
- [func readAttributeInstantaneousPower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeinstantaneouspower%28with%29.md)
- [func readAttributeInstantaneousReactiveCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeinstantaneousreactivecurrent%28with%29.md)
- [func readAttributeInstantaneousVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeinstantaneousvoltage%28with%29.md)
- [func readAttributeLineCurrentPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributelinecurrentphaseb%28with%29.md)
- [func readAttributeLineCurrentPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributelinecurrentphasec%28with%29.md)
- [func readAttributeMeasured11thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasured11thharmoniccurrent%28with%29.md)
- [func readAttributeMeasured1stHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasured1stharmoniccurrent%28with%29.md)
- [func readAttributeMeasured3rdHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasured3rdharmoniccurrent%28with%29.md)
- [func readAttributeMeasured5thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasured5thharmoniccurrent%28with%29.md)
- [func readAttributeMeasured7thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasured7thharmoniccurrent%28with%29.md)
- [func readAttributeMeasured9thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasured9thharmoniccurrent%28with%29.md)
- [func readAttributeMeasuredPhase11thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasuredphase11thharmoniccurrent%28with%29.md)
- [func readAttributeMeasuredPhase1stHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasuredphase1stharmoniccurrent%28with%29.md)
- [func readAttributeMeasuredPhase3rdHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasuredphase3rdharmoniccurrent%28with%29.md)
- [func readAttributeMeasuredPhase5thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasuredphase5thharmoniccurrent%28with%29.md)
- [func readAttributeMeasuredPhase7thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasuredphase7thharmoniccurrent%28with%29.md)
- [func readAttributeMeasuredPhase9thHarmonicCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasuredphase9thharmoniccurrent%28with%29.md)
- [func readAttributeMeasurementType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributemeasurementtype%28with%29.md)
- [func readAttributeNeutralCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeneutralcurrent%28with%29.md)
- [func readAttributeOverloadAlarmsMask(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributeoverloadalarmsmask%28with%29.md)
- [func readAttributePhaseHarmonicCurrentMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributephaseharmoniccurrentmultiplier%28with%29.md)
- [func readAttributePowerDivisor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributepowerdivisor%28with%29.md)
- [func readAttributePowerFactor(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributepowerfactor%28with%29.md)
- [func readAttributePowerFactorPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributepowerfactorphaseb%28with%29.md)
- [func readAttributePowerFactorPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributepowerfactorphasec%28with%29.md)
- [func readAttributePowerMultiplier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributepowermultiplier%28with%29.md)
- [func readAttributeReactiveCurrentPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributereactivecurrentphaseb%28with%29.md)
- [func readAttributeReactiveCurrentPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributereactivecurrentphasec%28with%29.md)
- [func readAttributeReactivePower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributereactivepower%28with%29.md)
- [func readAttributeReactivePowerPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributereactivepowerphaseb%28with%29.md)
- [func readAttributeReactivePowerPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributereactivepowerphasec%28with%29.md)
- [func readAttributeRmsCurrent(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrent%28with%29.md)
- [func readAttributeRmsCurrentMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentmax%28with%29.md)
- [func readAttributeRmsCurrentMaxPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentmaxphaseb%28with%29.md)
- [func readAttributeRmsCurrentMaxPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentmaxphasec%28with%29.md)
- [func readAttributeRmsCurrentMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentmin%28with%29.md)
- [func readAttributeRmsCurrentMinPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentminphaseb%28with%29.md)
- [func readAttributeRmsCurrentMinPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentminphasec%28with%29.md)
- [func readAttributeRmsCurrentPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentphaseb%28with%29.md)
- [func readAttributeRmsCurrentPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermscurrentphasec%28with%29.md)
- [func readAttributeRmsExtremeOverVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeovervoltage%28with%29.md)
- [func readAttributeRmsExtremeOverVoltagePeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeovervoltageperiod%28with%29.md)
- [func readAttributeRmsExtremeOverVoltagePeriodPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeovervoltageperiodphaseb%28with%29.md)
- [func readAttributeRmsExtremeOverVoltagePeriodPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeovervoltageperiodphasec%28with%29.md)
- [func readAttributeRmsExtremeUnderVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeundervoltage%28with%29.md)
- [func readAttributeRmsExtremeUnderVoltagePeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeundervoltageperiod%28with%29.md)
- [func readAttributeRmsExtremeUnderVoltagePeriodPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeundervoltageperiodphaseb%28with%29.md)
- [func readAttributeRmsExtremeUnderVoltagePeriodPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsextremeundervoltageperiodphasec%28with%29.md)
- [func readAttributeRmsVoltage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltage%28with%29.md)
- [func readAttributeRmsVoltageMax(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagemax%28with%29.md)
- [func readAttributeRmsVoltageMaxPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagemaxphaseb%28with%29.md)
- [func readAttributeRmsVoltageMaxPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagemaxphasec%28with%29.md)
- [func readAttributeRmsVoltageMin(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagemin%28with%29.md)
- [func readAttributeRmsVoltageMinPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltageminphaseb%28with%29.md)
- [func readAttributeRmsVoltageMinPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltageminphasec%28with%29.md)
- [func readAttributeRmsVoltagePhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagephaseb%28with%29.md)
- [func readAttributeRmsVoltagePhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagephasec%28with%29.md)
- [func readAttributeRmsVoltageSag(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagesag%28with%29.md)
- [func readAttributeRmsVoltageSagPeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagesagperiod%28with%29.md)
- [func readAttributeRmsVoltageSagPeriodPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagesagperiodphaseb%28with%29.md)
- [func readAttributeRmsVoltageSagPeriodPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltagesagperiodphasec%28with%29.md)
- [func readAttributeRmsVoltageSwell(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltageswell%28with%29.md)
- [func readAttributeRmsVoltageSwellPeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltageswellperiod%28with%29.md)
- [func readAttributeRmsVoltageSwellPeriodPhaseB(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltageswellperiodphaseb%28with%29.md)
- [func readAttributeRmsVoltageSwellPeriodPhaseC(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributermsvoltageswellperiodphasec%28with%29.md)
- [func readAttributeTotalActivePower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributetotalactivepower%28with%29.md)
- [func readAttributeTotalApparentPower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributetotalapparentpower%28with%29.md)
- [func readAttributeTotalReactivePower(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributetotalreactivepower%28with%29.md)
- [func readAttributeVoltageOverload(with: MTRReadParams?) -> [String : Any]?](./mtrclusterelectricalmeasurement/readattributevoltageoverload%28with%29.md)
- [func writeAttributeAcOverloadAlarmsMask(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributeacoverloadalarmsmask%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeAcOverloadAlarmsMask(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributeacoverloadalarmsmask%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeAverageRmsUnderVoltageCounter(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributeaveragermsundervoltagecounter%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeAverageRmsUnderVoltageCounter(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributeaveragermsundervoltagecounter%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeAverageRmsVoltageMeasurementPeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributeaveragermsvoltagemeasurementperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeAverageRmsVoltageMeasurementPeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributeaveragermsvoltagemeasurementperiod%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOverloadAlarmsMask(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributeoverloadalarmsmask%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOverloadAlarmsMask(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributeoverloadalarmsmask%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRmsExtremeOverVoltagePeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributermsextremeovervoltageperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRmsExtremeOverVoltagePeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributermsextremeovervoltageperiod%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRmsExtremeUnderVoltagePeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributermsextremeundervoltageperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRmsExtremeUnderVoltagePeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributermsextremeundervoltageperiod%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRmsVoltageSagPeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributermsvoltagesagperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRmsVoltageSagPeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributermsvoltagesagperiod%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRmsVoltageSwellPeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterelectricalmeasurement/writeattributermsvoltageswellperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRmsVoltageSwellPeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterelectricalmeasurement/writeattributermsvoltageswellperiod%28withvalue,expectedvalueinterval,params%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterelectricalmeasurement)*