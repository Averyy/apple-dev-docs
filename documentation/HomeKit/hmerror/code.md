# HMError.Code

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

Possible error values that can be returned from HomeKit APIs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Code
```

```c
enum HMErrorCode : NSInteger;
```

## Topics

### Accessory errors
- [HMError.Code.accessoryIsBlocked](./code/accessoryisblocked.md)
  An error indicating a blocked accessory.
- [HMError.Code.accessoryIsBusy](./code/accessoryisbusy.md)
  An error indicating the accessory is busy.
- [HMError.Code.accessoryIsSuspended](./code/accessoryissuspended.md)
  The accessory is suspended.
- [HMError.Code.accessoryNotReachable](./code/accessorynotreachable.md)
  An error indicating the accessory is not reachable over the network.
- [HMError.Code.accessoryOutOfCompliance](./code/accessoryoutofcompliance.md)
  An error indicating the accessory is out of compliance.
- [HMError.Code.accessoryOutOfResources](./code/accessoryoutofresources.md)
  An error indicating the accessory is out of resources.
- [HMError.Code.accessoryPoweredOff](./code/accessorypoweredoff.md)
  An error indicating the accessory is off.
- [HMError.Code.accessoryResponseError](./code/accessoryresponseerror.md)
  An error with the accessory’s response.
- [HMError.Code.addAccessoryFailed](./code/addaccessoryfailed.md)
  A failed attempt to add an accessory.
- [HMError.Code.incompatibleAccessory](./code/incompatibleaccessory.md)
  The accessory is incompatible.
### Action set errors
- [HMError.Code.actionInAnotherActionSet](./code/actioninanotheractionset.md)
  An attempt to add an action that exists in one action set to another action set.
- [HMError.Code.actionSetExecutionFailed](./code/actionsetexecutionfailed.md)
  An attempt to execute the action set failed.
- [HMError.Code.actionSetExecutionInProgress](./code/actionsetexecutioninprogress.md)
  An error indicating the execution of the action set is in progress.
- [HMError.Code.actionSetExecutionPartialSuccess](./code/actionsetexecutionpartialsuccess.md)
  An attempt to execute the action set was only partially successful.
- [HMError.Code.cannotRemoveBuiltinActionSet](./code/cannotremovebuiltinactionset.md)
  An error indicating the built-in action set cannot be removed.
- [HMError.Code.noActionsInActionSet](./code/noactionsinactionset.md)
  An attempt to execute an action set with no actions.
- [HMError.Code.noRegisteredActionSets](./code/noregisteredactionsets.md)
  An attempt to activate a trigger with no action sets.
### Association errors
- [HMError.Code.invalidAssociatedServiceType](./code/invalidassociatedservicetype.md)
  An error indicating an invalid service type.
- [HMError.Code.objectAlreadyAssociatedToHome](./code/objectalreadyassociatedtohome.md)
  An attempt to associate an object with a home when it’s already associated with that home.
- [HMError.Code.objectAssociatedToAnotherHome](./code/objectassociatedtoanotherhome.md)
  An attempt to associate an object with a home when it’s already associated with another home.
- [HMError.Code.objectNotAssociatedToAnyHome](./code/objectnotassociatedtoanyhome.md)
  An attempt to perform an operation on an object that is not associated to any home.
### Authorization errors
- [HMError.Code.invalidOrMissingAuthorizationData](./code/invalidormissingauthorizationdata.md)
  An error indicating the authorization data is invalid or missing.
- [HMError.Code.locationForHomeDisabled](./code/locationforhomedisabled.md)
  An error indicating the home’s location is disabled.
- [HMError.Code.homeAccessNotAuthorized](./code/homeaccessnotauthorized.md)
  An error indicating access to the home was not authorized.
- [HMError.Code.insufficientPrivileges](./code/insufficientprivileges.md)
  An error indicating insufficient privileges for the operation.
- [HMError.Code.messageAuthenticationFailed](./code/messageauthenticationfailed.md)
  A message authentication failure.
- [HMError.Code.notAuthorizedForLocationServices](./code/notauthorizedforlocationservices.md)
  An error indicating location services are not authorized.
- [HMError.Code.notAuthorizedForMicrophoneAccess](./code/notauthorizedformicrophoneaccess.md)
  An error indicating microphone access is not authorized.
- [HMError.Code.notSignedIntoiCloud](./code/notsignedintoicloud.md)
  An error indicating the user is not signed into iCloud.
- [HMError.Code.ownershipFailure](./code/ownershipfailure.md)
  The ownership code did not match.
- [HMError.Code.securityFailure](./code/securityfailure.md)
  A security failure.
### Bridge errors
- [HMError.Code.bridgedAccessoryNotReachable](./code/bridgedaccessorynotreachable.md)
  An error indicating the bridged accessory cannot be reached.
- [HMError.Code.cannotRemoveNonBridgeAccessory](./code/cannotremovenonbridgeaccessory.md)
  An attempt to remove a bridged accessory.
- [HMError.Code.cannotUnblockNonBridgeAccessory](./code/cannotunblocknonbridgeaccessory.md)
  An error indicating a non-bridge accessory cannot be unblocked.
### Characteristic errors
- [HMError.Code.readOnlyCharacteristic](./code/readonlycharacteristic.md)
  An attempt to modify a read-only value.
- [HMError.Code.writeOnlyCharacteristic](./code/writeonlycharacteristic.md)
  An attempt to read from a write-only characteristic.
### Collision errors
- [HMError.Code.homeWithSimilarNameExists](./code/homewithsimilarnameexists.md)
  An attempt to assign a home the same name as an existing home.
- [HMError.Code.objectWithSimilarNameExists](./code/objectwithsimilarnameexists.md)
  An object with a similar name already exists.
- [HMError.Code.objectWithSimilarNameExistsInHome](./code/objectwithsimilarnameexistsinhome.md)
  An attempt to give the name of one object to another object in the home.
- [HMError.Code.renameWithSimilarName](./code/renamewithsimilarname.md)
  An attempt to rename an object with its current name.
### Communication errors
- [HMError.Code.accessDenied](./code/accessdenied.md)
  An error indicating the current user doesn’t have privileges to perform the operation.
- [HMError.Code.accessoryCommunicationFailure](./code/accessorycommunicationfailure.md)
  The accessory failed to communicate.
- [HMError.Code.accessoryPairingFailed](./code/accessorypairingfailed.md)
  An attempt to pair with the accessory has failed.
- [HMError.Code.accessorySentInvalidResponse](./code/accessorysentinvalidresponse.md)
  An error indicating the accessory sent an invalid response.
- [HMError.Code.clientRequestError](./code/clientrequesterror.md)
  An error with the client request.
- [HMError.Code.communicationFailure](./code/communicationfailure.md)
  A communication failure.
- [HMError.Code.dataResetFailure](./code/dataresetfailure.md)
  An attempt to reset the data failed.
- [HMError.Code.timedOutWaitingForAccessory](./code/timedoutwaitingforaccessory.md)
  An accessory did not respond timely.
### Device and discovery errors
- [HMError.Code.deviceLocked](./code/devicelocked.md)
  An error indicating the device is locked.
- [HMError.Code.accessoryDiscoveryFailed](./code/accessorydiscoveryfailed.md)
  An error indicating accessory discovery failed.
### General errors
- [HMError.Code.alreadyExists](./code/alreadyexists.md)
  An error indicating the container already contains the object you are trying to add.
- [HMError.Code.genericError](./code/genericerror.md)
  An error that does not have a more specific error code.
- [static var incompatibleHomeHub: HMError.Code](./code/incompatiblehomehub.md)
  An error indicating an incompatible home hub.
- [HMError.Code.invalidClass](./code/invalidclass.md)
  An attempt to use an abstract base class in an operation instead of a concrete subclass.
- [HMError.Code.notFound](./code/notfound.md)
  An error indicating the object was not found in the container.
- [HMError.Code.notificationAlreadyEnabled](./code/notificationalreadyenabled.md)
  An error indicating the notification is already enabled.
- [HMError.Code.notificationNotSupported](./code/notificationnotsupported.md)
  An attempt to register for notifications from an accessory that does not support notifications.
- [HMError.Code.operationNotSupported](./code/operationnotsupported.md)
  An attempt to use an unsupported operation.
- [HMError.Code.unexpectedError](./code/unexpectederror.md)
  An unexpected error.
- [HMError.Code.missingEntitlement](./code/missingentitlement.md)
  An error indicating a required entitlement is not available.
- [HMError.Code.referToUserManual](./code/refertousermanual.md)
  An error described in the device’s user manual.
### Home and room errors
- [HMError.Code.maximumAccessoriesOfTypeInHome](./code/maximumaccessoriesoftypeinhome.md)
  The home already has the maximum number of accessories of the given type.
- [HMError.Code.roomForHomeCannotBeInZone](./code/roomforhomecannotbeinzone.md)
  An attempt to add the room that represents the entire home to a zone.
- [HMError.Code.roomForHomeCannotBeUpdated](./code/roomforhomecannotbeupdated.md)
  An attempt to change the room that represents the entire home.
### Hub errors
- [HMError.Code.noHomeHub](./code/nohomehub.md)
  An error indicating no home hub found.
- [HMError.Code.noCompatibleHomeHub](./code/nocompatiblehomehub.md)
  An error indicating no compatible home hub found.
### Limit errors
- [HMError.Code.cannotActivateTriggerTooFarInFuture](./code/cannotactivatetriggertoofarinfuture.md)
  An error indicating the trigger cannot be activated because it is set too far in the future.
- [HMError.Code.dateMustBeOnSpecifiedBoundaries](./code/datemustbeonspecifiedboundaries.md)
  An error indicating the date is not on the specified boundaries.
- [HMError.Code.fireDateInPast](./code/firedateinpast.md)
  An attempt to activate a timer trigger with a date in the past.
- [HMError.Code.invalidMessageSize](./code/invalidmessagesize.md)
  An error indicating an invalid message size.
- [HMError.Code.maximumObjectLimitReached](./code/maximumobjectlimitreached.md)
  An error indicating the maximum object count has been reached.
- [HMError.Code.recurrenceTooLarge](./code/recurrencetoolarge.md)
  An attempt to use a recurrence period that is too large.
- [HMError.Code.recurrenceTooSmall](./code/recurrencetoosmall.md)
  An error indicating the recurrence interval is too short.
- [HMError.Code.recurrenceMustBeOnSpecifiedBoundaries](./code/recurrencemustbeonspecifiedboundaries.md)
  An error indicating the recurrence rule is not on the specified boundaries.
### Network errors
- [HMError.Code.enterpriseNetworkNotSupported](./code/enterprisenetworknotsupported.md)
  An enterprise network doesn’t support this accessory.
- [HMError.Code.failedToJoinNetwork](./code/failedtojoinnetwork.md)
  The accessory failed to join the network.
- [HMError.Code.incompatibleNetwork](./code/incompatiblenetwork.md)
  An error indicating an incompatible network.
- [HMError.Code.networkUnavailable](./code/networkunavailable.md)
  An error indicating the network is unavailable.
- [HMError.Code.wiFiCredentialGenerationFailed](./code/wificredentialgenerationfailed.md)
  WiFi credential generation failed.
### Operation errors
- [HMError.Code.operationCancelled](./code/operationcancelled.md)
  An error indicating the user canceled the operation.
- [HMError.Code.operationInProgress](./code/operationinprogress.md)
  An error indicating the operation is already in progress.
- [HMError.Code.operationTimedOut](./code/operationtimedout.md)
  An error indicating the operation timed out.
### Parameter errors
- [HMError.Code.invalidParameter](./code/invalidparameter.md)
  An error indicating the object is invalid for the given operation.
- [HMError.Code.missingParameter](./code/missingparameter.md)
  An error indicating a missing parameter.
- [HMError.Code.nilParameter](./code/nilparameter.md)
  An error indicating that `nil` was passed for an operation that does not accept `nil`.
- [HMError.Code.unconfiguredParameter](./code/unconfiguredparameter.md)
  An error indicating an unconfigured parameter.
### Read and write errors
- [HMError.Code.readWriteFailure](./code/readwritefailure.md)
  An error indicating a failed read/write operation.
- [HMError.Code.readWritePartialSuccess](./code/readwritepartialsuccess.md)
  An error indicating a partially successful read/write operation.
### Synchronization errors
- [HMError.Code.cloudDataSyncInProgress](./code/clouddatasyncinprogress.md)
  An error indicating a data synchronization operation is in progress.
- [HMError.Code.keychainSyncNotEnabled](./code/keychainsyncnotenabled.md)
  An error indicating Keychain syncing is not enabled for the user.
### User errors
- [HMError.Code.userDeclinedAddingUser](./code/userdeclinedaddinguser.md)
  An error indicating the user canceled the add user operation.
- [HMError.Code.userDeclinedRemovingUser](./code/userdeclinedremovinguser.md)
  An error indicating the user canceled the remove user operation.
- [HMError.Code.userDeclinedInvite](./code/userdeclinedinvite.md)
  An error indicating the user declined the invitation.
- [HMError.Code.userIDNotEmailAddress](./code/useridnotemailaddress.md)
  An error indicating the user’s ID is not a valid email address.
- [HMError.Code.userManagementFailed](./code/usermanagementfailed.md)
  A user management error not covered by the other errors.
### Value errors
- [HMError.Code.invalidDataFormatSpecified](./code/invaliddataformatspecified.md)
  An error indicating an invalid data format was specified.
- [HMError.Code.invalidValueType](./code/invalidvaluetype.md)
  An attempt to use an invalid value type.
- [HMError.Code.nameContainsProhibitedCharacters](./code/namecontainsprohibitedcharacters.md)
  An attempt to name an object with prohibited characters.
- [HMError.Code.nameDoesNotEndWithValidCharacters](./code/namedoesnotendwithvalidcharacters.md)
  An error indicating the provided name has invalid characters at the end.
- [HMError.Code.nameDoesNotStartWithValidCharacters](./code/namedoesnotstartwithvalidcharacters.md)
  An attempt to start the name of an object with invalid characters.
- [HMError.Code.stringLongerThanMaximum](./code/stringlongerthanmaximum.md)
  An attempt to use a string longer than the maximum allowed.
- [HMError.Code.stringShorterThanMinimum](./code/stringshorterthanminimum.md)
  An attempt to use a string shorter than the required minimum.
- [HMError.Code.valueHigherThanMaximum](./code/valuehigherthanmaximum.md)
  An attempt to use a numeric value higher than the specified maximum value.
- [HMError.Code.valueLowerThanMinimum](./code/valuelowerthanminimum.md)
  An attempt to use a numeric value lower than the specified minimum value.
### Enumeration Cases
- [HMError.Code.partialCommunicationFailure](./code/partialcommunicationfailure.md)
- [HMError.Code.homeUpgradeRequired](./code/homeupgraderequired.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct HMError](../hmerror.md)
  An error HomeKit returns.
- [let HMErrorDomain: String](../hmerrordomain.md)
  A string that identifies the HomeKit error domain.
- [typealias HMErrorBlock](../hmerrorblock.md)
  A completion block that provides an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/code)*