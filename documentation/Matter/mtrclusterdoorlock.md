# MTRClusterDoorLock

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
class MTRClusterDoorLock
```

```objc
@interface MTRClusterDoorLock : MTRGenericCluster
```

## Topics

### Initializers
- [init?(device: MTRDevice, endpoint: UInt16, queue: dispatch_queue_t)](./mtrclusterdoorlock/init%28device,endpoint,queue%29.md)
- [init?(device: MTRDevice, endpointID: NSNumber, queue: dispatch_queue_t)](./mtrclusterdoorlock/init%28device,endpointid,queue%29.md)
### Instance Methods
- [func clearCredential(with: MTRDoorLockClusterClearCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearcredential%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearCredential(with: MTRDoorLockClusterClearCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearcredential%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func clearHolidaySchedule(with: MTRDoorLockClusterClearHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearholidayschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearHolidaySchedule(with: MTRDoorLockClusterClearHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearholidayschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func clearUser(with: MTRDoorLockClusterClearUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearuser%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearUser(with: MTRDoorLockClusterClearUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearuser%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func clearWeekDaySchedule(with: MTRDoorLockClusterClearWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearweekdayschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearWeekDaySchedule(with: MTRDoorLockClusterClearWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearweekdayschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func clearYearDaySchedule(with: MTRDoorLockClusterClearYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearyeardayschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearYearDaySchedule(with: MTRDoorLockClusterClearYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearyeardayschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getCredentialStatus(with: MTRDoorLockClusterGetCredentialStatusParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetCredentialStatusResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getcredentialstatus%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getCredentialStatus(with: MTRDoorLockClusterGetCredentialStatusParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetCredentialStatusResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getcredentialstatus%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getHolidaySchedule(with: MTRDoorLockClusterGetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetHolidayScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getholidayschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getHolidaySchedule(with: MTRDoorLockClusterGetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetHolidayScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getholidayschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getUserWith(MTRDoorLockClusterGetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetUserResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getuserwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getUserWith(MTRDoorLockClusterGetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetUserResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getuserwith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getWeekDaySchedule(with: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetWeekDayScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getweekdayschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getWeekDaySchedule(with: MTRDoorLockClusterGetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetWeekDayScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getweekdayschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func getYearDaySchedule(with: MTRDoorLockClusterGetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterGetYearDayScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getyeardayschedule%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func getYearDaySchedule(with: MTRDoorLockClusterGetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterGetYearDayScheduleResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/getyeardayschedule%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func lockDoor(with: MTRDoorLockClusterLockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/lockdoor%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func lockDoor(with: MTRDoorLockClusterLockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/lockdoor%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func lockDoor(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/lockdoor%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAcceptedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeacceptedcommandlist%28with%29.md)
- [func readAttributeActuatorEnabled(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeactuatorenabled%28with%29.md)
- [func readAttributeAttributeList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeattributelist%28with%29.md)
- [func readAttributeAutoRelockTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeautorelocktime%28with%29.md)
- [func readAttributeClusterRevision(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeclusterrevision%28with%29.md)
- [func readAttributeCredentialRulesSupport(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributecredentialrulessupport%28with%29.md)
- [func readAttributeDefaultConfigurationRegister(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributedefaultconfigurationregister%28with%29.md)
- [func readAttributeDoorClosedEvents(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributedoorclosedevents%28with%29.md)
- [func readAttributeDoorOpenEvents(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributedooropenevents%28with%29.md)
- [func readAttributeDoorState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributedoorstate%28with%29.md)
- [func readAttributeEnableInsideStatusLED(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeenableinsidestatusled%28with%29.md)
- [func readAttributeEnableLocalProgramming(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeenablelocalprogramming%28with%29.md)
- [func readAttributeEnableOneTouchLocking(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeenableonetouchlocking%28with%29.md)
- [func readAttributeEnablePrivacyModeButton(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeenableprivacymodebutton%28with%29.md)
- [func readAttributeExpiringUserTimeout(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeexpiringusertimeout%28with%29.md)
- [func readAttributeFeatureMap(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributefeaturemap%28with%29.md)
- [func readAttributeGeneratedCommandList(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributegeneratedcommandlist%28with%29.md)
- [func readAttributeLEDSettings(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeledsettings%28with%29.md)
- [func readAttributeLanguage(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributelanguage%28with%29.md)
- [func readAttributeLocalProgrammingFeatures(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributelocalprogrammingfeatures%28with%29.md)
- [func readAttributeLockState(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributelockstate%28with%29.md)
- [func readAttributeLockType(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributelocktype%28with%29.md)
- [func readAttributeMaxPINCodeLength(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributemaxpincodelength%28with%29.md)
- [func readAttributeMaxRFIDCodeLength(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributemaxrfidcodelength%28with%29.md)
- [func readAttributeMinPINCodeLength(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeminpincodelength%28with%29.md)
- [func readAttributeMinRFIDCodeLength(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeminrfidcodelength%28with%29.md)
- [func readAttributeNumberOfCredentialsSupportedPerUser(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofcredentialssupportedperuser%28with%29.md)
- [func readAttributeNumberOfHolidaySchedulesSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofholidayschedulessupported%28with%29.md)
- [func readAttributeNumberOfPINUsersSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofpinuserssupported%28with%29.md)
- [func readAttributeNumberOfRFIDUsersSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofrfiduserssupported%28with%29.md)
- [func readAttributeNumberOfTotalUsersSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberoftotaluserssupported%28with%29.md)
- [func readAttributeNumberOfWeekDaySchedulesSupportedPerUser(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofweekdayschedulessupportedperuser%28with%29.md)
- [func readAttributeNumberOfYearDaySchedulesSupportedPerUser(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofyeardayschedulessupportedperuser%28with%29.md)
- [func readAttributeOpenPeriod(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeopenperiod%28with%29.md)
- [func readAttributeOperatingMode(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeoperatingmode%28with%29.md)
- [func readAttributeRequirePINforRemoteOperation(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributerequirepinforremoteoperation%28with%29.md)
- [func readAttributeSendPINOverTheAir(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributesendpinovertheair%28with%29.md)
- [func readAttributeSoundVolume(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributesoundvolume%28with%29.md)
- [func readAttributeSupportedOperatingModes(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributesupportedoperatingmodes%28with%29.md)
- [func readAttributeUserCodeTemporaryDisableTime(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributeusercodetemporarydisabletime%28with%29.md)
- [func readAttributeWrongCodeEntryLimit(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributewrongcodeentrylimit%28with%29.md)
- [func setCredentialWith(MTRDoorLockClusterSetCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: (MTRDoorLockClusterSetCredentialResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/setcredentialwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setCredentialWith(MTRDoorLockClusterSetCredentialParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: (MTRDoorLockClusterSetCredentialResponseParams?, (any Error)?) -> Void)](./mtrclusterdoorlock/setcredentialwith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func setHolidayScheduleWith(MTRDoorLockClusterSetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/setholidayschedulewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setHolidayScheduleWith(MTRDoorLockClusterSetHolidayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/setholidayschedulewith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func setUserWith(MTRDoorLockClusterSetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/setuserwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setUserWith(MTRDoorLockClusterSetUserParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/setuserwith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func setWeekDayScheduleWith(MTRDoorLockClusterSetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/setweekdayschedulewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setWeekDayScheduleWith(MTRDoorLockClusterSetWeekDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/setweekdayschedulewith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func setYearDayScheduleWith(MTRDoorLockClusterSetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/setyeardayschedulewith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func setYearDayScheduleWith(MTRDoorLockClusterSetYearDayScheduleParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/setyeardayschedulewith%28_,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func unlockDoor(with: MTRDoorLockClusterUnlockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/unlockdoor%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func unlockDoor(with: MTRDoorLockClusterUnlockDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/unlockdoor%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func unlockDoor(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/unlockdoor%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func unlockWithTimeout(with: MTRDoorLockClusterUnlockWithTimeoutParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/unlockwithtimeout%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func unlockWithTimeout(with: MTRDoorLockClusterUnlockWithTimeoutParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completionHandler: ((any Error)?) -> Void)](./mtrclusterdoorlock/unlockwithtimeout%28with,expectedvalues,expectedvalueinterval,completionhandler%29.md)
- [func writeAttributeAutoRelockTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeautorelocktime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeAutoRelockTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeautorelocktime%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeDoorClosedEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributedoorclosedevents%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDoorClosedEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributedoorclosedevents%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeDoorOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributedooropenevents%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeDoorOpenEvents(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributedooropenevents%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeEnableInsideStatusLED(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeenableinsidestatusled%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeEnableInsideStatusLED(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeenableinsidestatusled%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeEnableLocalProgramming(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeenablelocalprogramming%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeEnableLocalProgramming(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeenablelocalprogramming%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeEnableOneTouchLocking(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeenableonetouchlocking%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeEnableOneTouchLocking(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeenableonetouchlocking%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeEnablePrivacyModeButton(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeenableprivacymodebutton%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeEnablePrivacyModeButton(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeenableprivacymodebutton%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeExpiringUserTimeout(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeexpiringusertimeout%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeExpiringUserTimeout(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeexpiringusertimeout%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLEDSettings(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeledsettings%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLEDSettings(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeledsettings%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLanguage(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributelanguage%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLanguage(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributelanguage%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeLocalProgrammingFeatures(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributelocalprogrammingfeatures%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeLocalProgrammingFeatures(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributelocalprogrammingfeatures%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeopenperiod%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOpenPeriod(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeopenperiod%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeOperatingMode(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeoperatingmode%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeOperatingMode(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeoperatingmode%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeRequirePINforRemoteOperation(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributerequirepinforremoteoperation%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeRequirePINforRemoteOperation(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributerequirepinforremoteoperation%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeSendPINOverTheAir(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributesendpinovertheair%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSendPINOverTheAir(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributesendpinovertheair%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeSoundVolume(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributesoundvolume%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeSoundVolume(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributesoundvolume%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeUserCodeTemporaryDisableTime(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributeusercodetemporarydisabletime%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeUserCodeTemporaryDisableTime(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributeusercodetemporarydisabletime%28withvalue,expectedvalueinterval,params%29.md)
- [func writeAttributeWrongCodeEntryLimit(withValue: [String : Any], expectedValueInterval: NSNumber)](./mtrclusterdoorlock/writeattributewrongcodeentrylimit%28withvalue,expectedvalueinterval%29.md)
- [func writeAttributeWrongCodeEntryLimit(withValue: [String : Any], expectedValueInterval: NSNumber, params: MTRWriteParams?)](./mtrclusterdoorlock/writeattributewrongcodeentrylimit%28withvalue,expectedvalueinterval,params%29.md)
- [func clearAliroReaderConfig(with: MTRDoorLockClusterClearAliroReaderConfigParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearaliroreaderconfig%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func clearAliroReaderConfig(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/clearaliroreaderconfig%28withexpectedvalues,expectedvalueinterval,completion%29.md)
- [func readAttributeAliroBLEAdvertisingVersion(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributealirobleadvertisingversion%28with%29.md)
- [func readAttributeAliroExpeditedTransactionSupportedProtocolVersions(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributealiroexpeditedtransactionsupportedprotocolversions%28with%29.md)
- [func readAttributeAliroGroupResolvingKey(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributealirogroupresolvingkey%28with%29.md)
- [func readAttributeAliroReaderGroupIdentifier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributealiroreadergroupidentifier%28with%29.md)
- [func readAttributeAliroReaderGroupSubIdentifier(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributealiroreadergroupsubidentifier%28with%29.md)
- [func readAttributeAliroReaderVerificationKey(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributealiroreaderverificationkey%28with%29.md)
- [func readAttributeAliroSupportedBLEUWBProtocolVersions(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributealirosupportedbleuwbprotocolversions%28with%29.md)
- [func readAttributeNumberOfAliroCredentialIssuerKeysSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofalirocredentialissuerkeyssupported%28with%29.md)
- [func readAttributeNumberOfAliroEndpointKeysSupported(with: MTRReadParams?) -> [String : Any]?](./mtrclusterdoorlock/readattributenumberofaliroendpointkeyssupported%28with%29.md)
- [func setAliroReaderConfigWith(MTRDoorLockClusterSetAliroReaderConfigParams, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/setaliroreaderconfigwith%28_,expectedvalues,expectedvalueinterval,completion%29.md)
- [func unboltDoor(with: MTRDoorLockClusterUnboltDoorParams?, expectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/unboltdoor%28with,expectedvalues,expectedvalueinterval,completion%29.md)
- [func unboltDoor(withExpectedValues: [[String : Any]]?, expectedValueInterval: NSNumber?, completion: ((any Error)?) -> Void)](./mtrclusterdoorlock/unboltdoor%28withexpectedvalues,expectedvalueinterval,completion%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrclusterdoorlock)*