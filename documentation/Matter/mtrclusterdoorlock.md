# MTRClusterDoorLock

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
class MTRClusterDoorLock
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](mtrclusterdoorlock/init(device:endpoint:queue:).md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](mtrclusterdoorlock/init(device:endpointid:queue:).md)
### Instance Methods
- [func clearCredential(with: MTRDoorLockClusterClearCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/clearcredential(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func clearCredential(with: MTRDoorLockClusterClearCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/clearcredential(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func clearHolidaySchedule(with: MTRDoorLockClusterClearHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/clearholidayschedule(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func clearHolidaySchedule(with: MTRDoorLockClusterClearHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/clearholidayschedule(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func clearUser(with: MTRDoorLockClusterClearUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/clearuser(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func clearUser(with: MTRDoorLockClusterClearUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/clearuser(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func clearWeekDaySchedule(with: MTRDoorLockClusterClearWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/clearweekdayschedule(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func clearWeekDaySchedule(with: MTRDoorLockClusterClearWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/clearweekdayschedule(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func clearYearDaySchedule(with: MTRDoorLockClusterClearYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/clearyeardayschedule(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func clearYearDaySchedule(with: MTRDoorLockClusterClearYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/clearyeardayschedule(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func getCredentialStatus(with: MTRDoorLockClusterGetCredentialStatusParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetCredentialStatusResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getcredentialstatus(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getCredentialStatus(with: MTRDoorLockClusterGetCredentialStatusParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetCredentialStatusResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getcredentialstatus(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func getHolidaySchedule(with: MTRDoorLockClusterGetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetHolidayScheduleResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getholidayschedule(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getHolidaySchedule(with: MTRDoorLockClusterGetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetHolidayScheduleResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getholidayschedule(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func getUserWith(MTRDoorLockClusterGetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetUserResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getuserwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func getUserWith(MTRDoorLockClusterGetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetUserResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getuserwith(_:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func getWeekDaySchedule(with: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetWeekDayScheduleResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getweekdayschedule(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getWeekDaySchedule(with: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetWeekDayScheduleResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getweekdayschedule(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func getYearDaySchedule(with: MTRDoorLockClusterGetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetYearDayScheduleResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getyeardayschedule(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func getYearDaySchedule(with: MTRDoorLockClusterGetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetYearDayScheduleResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/getyeardayschedule(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func lockDoor(with: MTRDoorLockClusterLockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/lockdoor(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func lockDoor(with: MTRDoorLockClusterLockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/lockdoor(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func lockDoor(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/lockdoor(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeacceptedcommandlist(with:).md)
- [func readAttributeActuatorEnabled(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeactuatorenabled(with:).md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeattributelist(with:).md)
- [func readAttributeAutoRelockTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeautorelocktime(with:).md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeclusterrevision(with:).md)
- [func readAttributeCredentialRulesSupport(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributecredentialrulessupport(with:).md)
- [func readAttributeDefaultConfigurationRegister(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributedefaultconfigurationregister(with:).md)
- [func readAttributeDoorClosedEvents(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributedoorclosedevents(with:).md)
- [func readAttributeDoorOpenEvents(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributedooropenevents(with:).md)
- [func readAttributeDoorState(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributedoorstate(with:).md)
- [func readAttributeEnableInsideStatusLED(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeenableinsidestatusled(with:).md)
- [func readAttributeEnableLocalProgramming(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeenablelocalprogramming(with:).md)
- [func readAttributeEnableOneTouchLocking(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeenableonetouchlocking(with:).md)
- [func readAttributeEnablePrivacyModeButton(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeenableprivacymodebutton(with:).md)
- [func readAttributeExpiringUserTimeout(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeexpiringusertimeout(with:).md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributefeaturemap(with:).md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributegeneratedcommandlist(with:).md)
- [func readAttributeLEDSettings(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeledsettings(with:).md)
- [func readAttributeLanguage(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributelanguage(with:).md)
- [func readAttributeLocalProgrammingFeatures(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributelocalprogrammingfeatures(with:).md)
- [func readAttributeLockState(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributelockstate(with:).md)
- [func readAttributeLockType(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributelocktype(with:).md)
- [func readAttributeMaxPINCodeLength(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributemaxpincodelength(with:).md)
- [func readAttributeMaxRFIDCodeLength(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributemaxrfidcodelength(with:).md)
- [func readAttributeMinPINCodeLength(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeminpincodelength(with:).md)
- [func readAttributeMinRFIDCodeLength(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeminrfidcodelength(with:).md)
- [func readAttributeNumberOfCredentialsSupportedPerUser(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofcredentialssupportedperuser(with:).md)
- [func readAttributeNumberOfHolidaySchedulesSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofholidayschedulessupported(with:).md)
- [func readAttributeNumberOfPINUsersSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofpinuserssupported(with:).md)
- [func readAttributeNumberOfRFIDUsersSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofrfiduserssupported(with:).md)
- [func readAttributeNumberOfTotalUsersSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberoftotaluserssupported(with:).md)
- [func readAttributeNumberOfWeekDaySchedulesSupportedPerUser(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofweekdayschedulessupportedperuser(with:).md)
- [func readAttributeNumberOfYearDaySchedulesSupportedPerUser(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofyeardayschedulessupportedperuser(with:).md)
- [func readAttributeOpenPeriod(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeopenperiod(with:).md)
- [func readAttributeOperatingMode(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeoperatingmode(with:).md)
- [func readAttributeRequirePINforRemoteOperation(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributerequirepinforremoteoperation(with:).md)
- [func readAttributeSendPINOverTheAir(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributesendpinovertheair(with:).md)
- [func readAttributeSoundVolume(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributesoundvolume(with:).md)
- [func readAttributeSupportedOperatingModes(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributesupportedoperatingmodes(with:).md)
- [func readAttributeUserCodeTemporaryDisableTime(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributeusercodetemporarydisabletime(with:).md)
- [func readAttributeWrongCodeEntryLimit(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributewrongcodeentrylimit(with:).md)
- [func setCredentialWith(MTRDoorLockClusterSetCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterSetCredentialResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/setcredentialwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setCredentialWith(MTRDoorLockClusterSetCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterSetCredentialResponseParams?, (any Error)?) -> Void)](mtrclusterdoorlock/setcredentialwith(_:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func setHolidayScheduleWith(MTRDoorLockClusterSetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/setholidayschedulewith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setHolidayScheduleWith(MTRDoorLockClusterSetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/setholidayschedulewith(_:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func setUserWith(MTRDoorLockClusterSetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/setuserwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setUserWith(MTRDoorLockClusterSetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/setuserwith(_:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func setWeekDayScheduleWith(MTRDoorLockClusterSetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/setweekdayschedulewith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setWeekDayScheduleWith(MTRDoorLockClusterSetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/setweekdayschedulewith(_:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func setYearDayScheduleWith(MTRDoorLockClusterSetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/setyeardayschedulewith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func setYearDayScheduleWith(MTRDoorLockClusterSetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/setyeardayschedulewith(_:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func unlockDoor(with: MTRDoorLockClusterUnlockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/unlockdoor(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func unlockDoor(with: MTRDoorLockClusterUnlockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/unlockdoor(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func unlockDoor(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/unlockdoor(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func unlockWithTimeout(with: MTRDoorLockClusterUnlockWithTimeoutParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/unlockwithtimeout(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func unlockWithTimeout(with: MTRDoorLockClusterUnlockWithTimeoutParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](mtrclusterdoorlock/unlockwithtimeout(with:expectedvalues:expectedvalueinterval:completionhandler:).md)
- [func writeAttributeAutoRelockTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeautorelocktime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeAutoRelockTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeautorelocktime(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeDoorClosedEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributedoorclosedevents(withvalue:expectedvalueinterval:).md)
- [func writeAttributeDoorClosedEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributedoorclosedevents(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeDoorOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributedooropenevents(withvalue:expectedvalueinterval:).md)
- [func writeAttributeDoorOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributedooropenevents(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeEnableInsideStatusLED(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeenableinsidestatusled(withvalue:expectedvalueinterval:).md)
- [func writeAttributeEnableInsideStatusLED(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeenableinsidestatusled(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeEnableLocalProgramming(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeenablelocalprogramming(withvalue:expectedvalueinterval:).md)
- [func writeAttributeEnableLocalProgramming(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeenablelocalprogramming(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeEnableOneTouchLocking(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeenableonetouchlocking(withvalue:expectedvalueinterval:).md)
- [func writeAttributeEnableOneTouchLocking(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeenableonetouchlocking(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeEnablePrivacyModeButton(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeenableprivacymodebutton(withvalue:expectedvalueinterval:).md)
- [func writeAttributeEnablePrivacyModeButton(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeenableprivacymodebutton(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeExpiringUserTimeout(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeexpiringusertimeout(withvalue:expectedvalueinterval:).md)
- [func writeAttributeExpiringUserTimeout(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeexpiringusertimeout(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLEDSettings(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeledsettings(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLEDSettings(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeledsettings(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLanguage(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributelanguage(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLanguage(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributelanguage(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeLocalProgrammingFeatures(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributelocalprogrammingfeatures(withvalue:expectedvalueinterval:).md)
- [func writeAttributeLocalProgrammingFeatures(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributelocalprogrammingfeatures(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeopenperiod(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeopenperiod(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeOperatingMode(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeoperatingmode(withvalue:expectedvalueinterval:).md)
- [func writeAttributeOperatingMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeoperatingmode(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeRequirePINforRemoteOperation(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributerequirepinforremoteoperation(withvalue:expectedvalueinterval:).md)
- [func writeAttributeRequirePINforRemoteOperation(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributerequirepinforremoteoperation(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeSendPINOverTheAir(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributesendpinovertheair(withvalue:expectedvalueinterval:).md)
- [func writeAttributeSendPINOverTheAir(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributesendpinovertheair(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeSoundVolume(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributesoundvolume(withvalue:expectedvalueinterval:).md)
- [func writeAttributeSoundVolume(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributesoundvolume(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeUserCodeTemporaryDisableTime(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributeusercodetemporarydisabletime(withvalue:expectedvalueinterval:).md)
- [func writeAttributeUserCodeTemporaryDisableTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributeusercodetemporarydisabletime(withvalue:expectedvalueinterval:params:).md)
- [func writeAttributeWrongCodeEntryLimit(withValue: [String : Any], expectedValueInterval: NSNumber)](mtrclusterdoorlock/writeattributewrongcodeentrylimit(withvalue:expectedvalueinterval:).md)
- [func writeAttributeWrongCodeEntryLimit(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](mtrclusterdoorlock/writeattributewrongcodeentrylimit(withvalue:expectedvalueinterval:params:).md)
- [func clearAliroReaderConfig(with: MTRDoorLockClusterClearAliroReaderConfigParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/clearaliroreaderconfig(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func clearAliroReaderConfig(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/clearaliroreaderconfig(withexpectedvalues:expectedvalueinterval:completion:).md)
- [func readAttributeAliroBLEAdvertisingVersion(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributealirobleadvertisingversion(with:).md)
- [func readAttributeAliroExpeditedTransactionSupportedProtocolVersions(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributealiroexpeditedtransactionsupportedprotocolversions(with:).md)
- [func readAttributeAliroGroupResolvingKey(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributealirogroupresolvingkey(with:).md)
- [func readAttributeAliroReaderGroupIdentifier(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributealiroreadergroupidentifier(with:).md)
- [func readAttributeAliroReaderGroupSubIdentifier(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributealiroreadergroupsubidentifier(with:).md)
- [func readAttributeAliroReaderVerificationKey(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributealiroreaderverificationkey(with:).md)
- [func readAttributeAliroSupportedBLEUWBProtocolVersions(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributealirosupportedbleuwbprotocolversions(with:).md)
- [func readAttributeNumberOfAliroCredentialIssuerKeysSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofalirocredentialissuerkeyssupported(with:).md)
- [func readAttributeNumberOfAliroEndpointKeysSupported(with: MTRReadParams?) -> [String : Any]?](mtrclusterdoorlock/readattributenumberofaliroendpointkeyssupported(with:).md)
- [func setAliroReaderConfigWith(MTRDoorLockClusterSetAliroReaderConfigParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/setaliroreaderconfigwith(_:expectedvalues:expectedvalueinterval:completion:).md)
- [func unboltDoor(with: MTRDoorLockClusterUnboltDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/unboltdoor(with:expectedvalues:expectedvalueinterval:completion:).md)
- [func unboltDoor(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](mtrclusterdoorlock/unboltdoor(withexpectedvalues:expectedvalueinterval:completion:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock)*