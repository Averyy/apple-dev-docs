# Status items

**Framework**: Device Management

Monitor device state using status reports.

## Topics

### Status report
- [object StatusReport](statusreport.md)
  Provides details about an error for an item in a status report.
- [object StatusReason](statusreason.md)
  Provides details about an error for an item in a status report.
### Account list items
- [object StatusAccountListCalDAV](statusaccountlistcaldav.md)
  The status item that lists the devices’s Calendar accounts.
- [object StatusAccountListCardDAV](statusaccountlistcarddav.md)
  The status item that lists the devices’s Contacts accounts.
- [object StatusAccountListExchange](statusaccountlistexchange.md)
  The status item that lists the devices’s Exchange accounts.
- [object StatusAccountListGoogle](statusaccountlistgoogle.md)
  The status item that lists the client’s Google accounts.
- [object StatusAccountListLDAP](statusaccountlistldap.md)
  The status item that lists the devices’s Lightweight Directory Access Protocol (LDAP) accounts.
- [object StatusAccountListMailIncoming](statusaccountlistmailincoming.md)
  The status item that lists the devices’s incoming Mail accounts.
- [object StatusAccountListMailOutgoing](statusaccountlistmailoutgoing.md)
  The status item that lists the devices’s outgoing Mail accounts.
- [object StatusAccountListSubscribedCalendar](statusaccountlistsubscribedcalendar.md)
  The status item that lists the devices’s subscribed calendars.
### App and package items
- [object StatusAppManagedList](statusappmanagedlist.md)
  The status item that lists the device’s declarative managed apps.
- [object StatusMDMApp](statusmdmapp.md)
  The status item that lists the devices’s MDM-installed apps.
- [object StatusPackageList](statuspackagelist.md)
  The status item that lists the device’s declarative packages.
### Content cache items
- [object StatusContentCacheInfo](statuscontentcacheinfo.md)
  The status item that reports information about the Content Cache service.
- [object StatusContentCacheParents](statuscontentcacheparents.md)
  The status item that reports information about the Content Cache service parent caches.
- [object StatusContentCachePeers](statuscontentcachepeers.md)
  The status item that reports information about the Content Cache service peer caches.
- [object StatusContentCacheStatus](statuscontentcachestatus.md)
  The status item that reports the status of the Content Cache service.
### Device property items
- [object StatusDeviceBatteryHealth](statusdevicebatteryhealth.md)
  The status item that reports the device’s battery health.
- [object StatusDeviceModelFamily](statusdevicemodelfamily.md)
  The status item that reports the device’s hardware model family.
- [object StatusDeviceModelIdentifier](statusdevicemodelidentifier.md)
  The status item that reports the device’s hardware model identifier.
- [object StatusDeviceModelMarketingName](statusdevicemodelmarketingname.md)
  The status item that reports the device’s model marketing name.
- [object StatusDeviceModelNumber](statusdevicemodelnumber.md)
  The status item that reports the device’s hardware number.
- [object StatusDeviceOperatingSystemBuildVersion](statusdeviceoperatingsystembuildversion.md)
  The status item that reports the device’s operating system build version.
- [object StatusDeviceOperatingSystemFamily](statusdeviceoperatingsystemfamily.md)
  The status item that reports the device’s operating system family.
- [object StatusDeviceOperatingSystemMarketingName](statusdeviceoperatingsystemmarketingname.md)
  The status item that reports the device’s operating system marketing name.
- [object StatusDeviceOperatingSystemSupplementalBuildVersion](statusdeviceoperatingsystemsupplementalbuildversion.md)
  The status item that reports the device’s operating system supplemental build version and Background Security Improvement version.
- [object StatusDeviceOperatingSystemSupplementalExtraVersion](statusdeviceoperatingsystemsupplementalextraversion.md)
  The status item that reports the device’s operating system Background Security Improvement version.
- [object StatusDeviceOperatingSystemVersion](statusdeviceoperatingsystemversion.md)
  The status item that reports the device’s operating system version.
- [object StatusDeviceSerialNumber](statusdeviceserialnumber.md)
  The status item that reports the device’s serial number.
- [object StatusDeviceSystemHealth](statusdevicesystemhealth.md)
  The status item that reports the device’s system health.
- [object StatusDeviceUDID](statusdeviceudid.md)
  The status item that reports the device’s UDID.
### Enhanced logging items
- [object StatusEnhancedLoggingStatus](statusenhancedloggingstatus.md)
  The status item that reports the device’s enhanced log collection session status.
- [object StatusEnhancedLoggingAppleCareToken](statusenhancedloggingapplecaretoken.md)
  The status item that reports the device’s enhanced log collection session AppleCare token.
- [object StatusEnhancedLoggingTimestamp](statusenhancedloggingtimestamp.md)
  The status item that reports the device’s enhanced log collection session timestamp.
### Management items
- [object StatusManagementClientCapabilities](statusmanagementclientcapabilities.md)
  The status item that reports the devices’s protocol capabilities.
- [object StatusManagementDeclarations](statusmanagementdeclarations.md)
  The status item that reports the device’s processed declarations.
### MDM protocol items
- [object StatusMDMEnrollmentType](statusmdmenrollmenttype.md)
  The status item that reports the device’s management enrollment type.
- [object StatusMDMIsAwaitingConfiguration](statusmdmisawaitingconfiguration.md)
  The status item that reports the device management awaiting configuration state.
- [object StatusMDMIsReturnToService](statusmdmisreturntoservice.md)
  The status item that reports the device’s return to service with app preservation state.
- [object StatusMDMIsSharedIPad](statusmdmissharedipad.md)
  The status item that reports the device’s Shared iPad state.
- [object StatusMDMPushMagic](statusmdmpushmagic.md)
  The status item that reports the device’s push magic value.
- [object StatusMDMPushToken](statusmdmpushtoken.md)
  The status item that reports the device’s push token.
### Migration assisstant items
- [object StatusMigrationAssistantReport](statusmigrationassistantreport.md)
  The status item that reports the state of a completed migration.
- [object StatusMigrationAssistantState](statusmigrationassistantstate.md)
  A status item that shows the device’s current migration state.
### Passcode and security items
- [object StatusPasscodeCompliance](statuspasscodecompliance.md)
  The status item that reports the device’s passcode compliance.
- [object StatusPasscodeIsPresent](statuspasscodeispresent.md)
  The status item that reports whether the device has a passcode.
- [object StatusDiskManagementFileVaultEnabled](statusdiskmanagementfilevaultenabled.md)
  The status item that reports whether FileVault is enabled.
- [object StatusSecurityCertificateList](statussecuritycertificatelist.md)
  The status item that lists the device’s managed certificates.
- [object StatusSecurityLockdownMode](statussecuritylockdownmode.md)
  The status item that reports the device’s Lockdown Mode state.
### Software update items
- [object StatusSoftwareUpdateBetaEnrollment](statussoftwareupdatebetaenrollment.md)
  The status item that reports the device’s enrolled beta program.
- [object StatusSoftwareUpdateDeviceID](statussoftwareupdatedeviceid.md)
  The status item that reports the device’s software update device ID.
- [object StatusSoftwareUpdateFailureReason](statussoftwareupdatefailurereason.md)
  The status item that reports the device’s software update failure reason.
- [object StatusSoftwareUpdateInstallReason](statussoftwareupdateinstallreason.md)
  The status item that reports the device’s pending software update reason.
- [object StatusSoftwareUpdateInstallState](statussoftwareupdateinstallstate.md)
  The status item that reports the device’s software update install state.
- [object StatusSoftwareUpdatePendingVersion](statussoftwareupdatependingversion.md)
  The status item that reports the device’s pending software update version.
### Miscellaneous items
- [object StatusScreenSharingConnectionGroupUnresolvedConnections](statusscreensharingconnectiongroupunresolvedconnections.md)
  The status item that lists connection groups with member connection references that the device couldn’t resolve.
- [object StatusServicesBackgroundTask](statusservicesbackgroundtask.md)
  The status item that reports the device’s background task details.
### Test items
- [object StatusTestArrayValue](statustestarrayvalue.md)
  A test status item for an array.
- [object StatusTestBooleanValue](statustestbooleanvalue.md)
  A test status item for a Boolean value.
- [object StatusTestDictionaryValue](statustestdictionaryvalue.md)
  A test status item for a dictionary.
- [object StatusTestErrorValue](statustesterrorvalue.md)
  A test status item for an error.
- [object StatusTestIntegerValue](statustestintegervalue.md)
  A test status item for an integer.
- [object StatusTestRealValue](statustestrealvalue.md)
  A test status item for a real value.
- [object StatusTestStringValue](statusteststringvalue.md)
  A test status item for a string.

## See Also

- [Declarations](devicemanagement-declarations.md)
  Configure devices using declarative device management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/status-items)*