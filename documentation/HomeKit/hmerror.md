# HMError

**Framework**: HomeKit  
**Kind**: struct

An error HomeKit returns.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct HMError
```

## Topics

### Obtaining error information
- [let HMErrorDomain: String](hmerrordomain.md)
  A string that identifies the HomeKit error domain.
### Detecting accessory errors
- [static var accessoryIsBlocked: HMError.Code](hmerror/accessoryisblocked.md)
  An error indicating a blocked accessory.
- [static var accessoryIsBusy: HMError.Code](hmerror/accessoryisbusy.md)
  An error indicating the accessory is busy.
- [static var accessoryIsSuspended: HMError.Code](hmerror/accessoryissuspended.md)
  The accessory is suspended.
- [static var accessoryNotReachable: HMError.Code](hmerror/accessorynotreachable.md)
  An error indicating the accessory is not reachable over the network.
- [static var accessoryOutOfCompliance: HMError.Code](hmerror/accessoryoutofcompliance.md)
  An error indicating the accessory is out of compliance.
- [static var accessoryOutOfResources: HMError.Code](hmerror/accessoryoutofresources.md)
  An error indicating the accessory is out of resources.
- [static var accessoryPoweredOff: HMError.Code](hmerror/accessorypoweredoff.md)
  An error indicating the accessory is off.
- [static var accessoryResponseError: HMError.Code](hmerror/accessoryresponseerror.md)
  An error with the accessory’s response.
- [static var addAccessoryFailed: HMError.Code](hmerror/addaccessoryfailed.md)
  A failed attempt to add an accessory.
- [static var incompatibleAccessory: HMError.Code](hmerror/incompatibleaccessory.md)
  The accessory is incompatible.
### Detecting action set errors
- [static var actionInAnotherActionSet: HMError.Code](hmerror/actioninanotheractionset.md)
  An attempt to add an action that exists in one action set to another action set.
- [static var actionSetExecutionFailed: HMError.Code](hmerror/actionsetexecutionfailed.md)
  An attempt to execute the action set failed.
- [static var actionSetExecutionInProgress: HMError.Code](hmerror/actionsetexecutioninprogress.md)
  An error indicating the execution of the action set is in progress.
- [static var actionSetExecutionPartialSuccess: HMError.Code](hmerror/actionsetexecutionpartialsuccess.md)
  An attempt to execute the action set was only partially successful.
- [static var cannotRemoveBuiltinActionSet: HMError.Code](hmerror/cannotremovebuiltinactionset.md)
  An error indicating the built-in action set cannot be removed.
- [static var noActionsInActionSet: HMError.Code](hmerror/noactionsinactionset.md)
  An attempt to execute an action set with no actions.
- [static var noRegisteredActionSets: HMError.Code](hmerror/noregisteredactionsets.md)
  An attempt to activate a trigger with no action sets.
### Detecting association errors
- [static var invalidAssociatedServiceType: HMError.Code](hmerror/invalidassociatedservicetype.md)
  An error indicating an invalid service type.
- [static var objectAlreadyAssociatedToHome: HMError.Code](hmerror/objectalreadyassociatedtohome.md)
  An attempt to associate an object with a home when it’s already associated with that home.
- [static var objectAssociatedToAnotherHome: HMError.Code](hmerror/objectassociatedtoanotherhome.md)
  An attempt to associate an object with a home when it’s already associated with another home.
- [static var objectNotAssociatedToAnyHome: HMError.Code](hmerror/objectnotassociatedtoanyhome.md)
  An attempt to perform an operation on an object that is not associated to any home.
### Detecting authorization errors
- [static var invalidOrMissingAuthorizationData: HMError.Code](hmerror/invalidormissingauthorizationdata.md)
  An error indicating the authorization data is invalid or missing.
- [static var locationForHomeDisabled: HMError.Code](hmerror/locationforhomedisabled.md)
  An error indicating the home’s location is disabled.
- [static var homeAccessNotAuthorized: HMError.Code](hmerror/homeaccessnotauthorized.md)
  An error indicating access to the home is not authorized.
- [static var insufficientPrivileges: HMError.Code](hmerror/insufficientprivileges.md)
  An error indicating insufficient privileges for the operation.
- [static var messageAuthenticationFailed: HMError.Code](hmerror/messageauthenticationfailed.md)
  A message authentication failure.
- [static var notAuthorizedForLocationServices: HMError.Code](hmerror/notauthorizedforlocationservices.md)
  An error indicating location services are not authorized.
- [static var notAuthorizedForMicrophoneAccess: HMError.Code](hmerror/notauthorizedformicrophoneaccess.md)
  An error indicating microphone access is not authorized.
- [static var notSignedIntoiCloud: HMError.Code](hmerror/notsignedintoicloud.md)
  An error indicating the user is not signed into iCloud.
- [static var ownershipFailure: HMError.Code](hmerror/ownershipfailure.md)
  The ownership code did not match.
- [static var securityFailure: HMError.Code](hmerror/securityfailure.md)
  A security failure.
### Detecting bridge errors
- [static var bridgedAccessoryNotReachable: HMError.Code](hmerror/bridgedaccessorynotreachable.md)
  An error indicating the bridged accessory cannot be reached.
- [static var cannotRemoveNonBridgeAccessory: HMError.Code](hmerror/cannotremovenonbridgeaccessory.md)
  An attempt to remove a bridged accessory.
- [static var cannotUnblockNonBridgeAccessory: HMError.Code](hmerror/cannotunblocknonbridgeaccessory.md)
  An error indicating a non-bridge accessory cannot be unblocked.
### Detecting characteristic errors
- [static var readOnlyCharacteristic: HMError.Code](hmerror/readonlycharacteristic.md)
  An attempt to modify a read-only value.
- [static var writeOnlyCharacteristic: HMError.Code](hmerror/writeonlycharacteristic.md)
  An attempt to read from a write-only characteristic.
### Detecting collision errors
- [static var homeWithSimilarNameExists: HMError.Code](hmerror/homewithsimilarnameexists.md)
  An attempt to assign a home the same name as an existing home.
- [static var objectWithSimilarNameExists: HMError.Code](hmerror/objectwithsimilarnameexists.md)
  An object with a similar name already exists.
- [static var objectWithSimilarNameExistsInHome: HMError.Code](hmerror/objectwithsimilarnameexistsinhome.md)
  An attempt to give the name of one object to another object in the home.
- [static var renameWithSimilarName: HMError.Code](hmerror/renamewithsimilarname.md)
  An attempt to rename an object with its current name.
### Detecting communication errors
- [static var accessDenied: HMError.Code](hmerror/accessdenied.md)
  An error indicating the current user doesn’t have privileges to perform the operation.
- [static var accessoryCommunicationFailure: HMError.Code](hmerror/accessorycommunicationfailure.md)
  The accessory failed to communicate.
- [static var accessoryPairingFailed: HMError.Code](hmerror/accessorypairingfailed.md)
  An attempt to pair with the accessory has failed.
- [static var accessorySentInvalidResponse: HMError.Code](hmerror/accessorysentinvalidresponse.md)
  An error indicating the accessory sent an invalid response.
- [static var clientRequestError: HMError.Code](hmerror/clientrequesterror.md)
  An error with the client request.
- [static var communicationFailure: HMError.Code](hmerror/communicationfailure.md)
  A communication failure.
- [static var dataResetFailure: HMError.Code](hmerror/dataresetfailure.md)
  An attempt to reset the data failed.
- [static var timedOutWaitingForAccessory: HMError.Code](hmerror/timedoutwaitingforaccessory.md)
  An accessory did not respond timely.
- [static var partialCommunicationFailure: HMError.Code](hmerror/partialcommunicationfailure.md)
### Detecting device and discovery errors
- [static var deviceLocked: HMError.Code](hmerror/devicelocked.md)
  An error indicating the device is locked.
- [static var accessoryDiscoveryFailed: HMError.Code](hmerror/accessorydiscoveryfailed.md)
  An error indicating that accessory discovery failed.
### Detecting general errors
- [static var alreadyExists: HMError.Code](hmerror/alreadyexists.md)
  An error indicating the container already contains the object you are trying to add.
- [static var genericError: HMError.Code](hmerror/genericerror.md)
  An error that does not have a more specific error code.
- [static var incompatibleHomeHub: HMError.Code](hmerror/incompatiblehomehub.md)
  No compatible home hub found.
- [static var invalidClass: HMError.Code](hmerror/invalidclass.md)
  An attempt to use an abstract base class in an operation instead of a concrete subclass.
- [static var notFound: HMError.Code](hmerror/notfound.md)
  An error indicating the object was not found in the container.
- [static var notificationAlreadyEnabled: HMError.Code](hmerror/notificationalreadyenabled.md)
  An error indicating the notification is already enabled.
- [static var notificationNotSupported: HMError.Code](hmerror/notificationnotsupported.md)
  An attempt to register for notifications from an accessory that does not support notifications.
- [static var operationNotSupported: HMError.Code](hmerror/operationnotsupported.md)
  An attempt to use an unsupported operation.
- [static var unexpectedError: HMError.Code](hmerror/unexpectederror.md)
  An unexpected error.
- [static var missingEntitlement: HMError.Code](hmerror/missingentitlement.md)
  An error indicating a required entitlement is not available.
- [static var referToUserManual: HMError.Code](hmerror/refertousermanual.md)
  An error described in the device’s user manual.
### Detecting home and room errors
- [static var maximumAccessoriesOfTypeInHome: HMError.Code](hmerror/maximumaccessoriesoftypeinhome.md)
  The home already has the maximum number of accessories of the given type.
- [static var roomForHomeCannotBeInZone: HMError.Code](hmerror/roomforhomecannotbeinzone.md)
  An attempt to add the room that represents the entire home to a zone.
- [static var roomForHomeCannotBeUpdated: HMError.Code](hmerror/roomforhomecannotbeupdated.md)
  An attempt to change the room that represents the entire home.
### Detecting hub errors
- [static var noHomeHub: HMError.Code](hmerror/nohomehub.md)
  An error indicating no home hub found.
- [static var noCompatibleHomeHub: HMError.Code](hmerror/nocompatiblehomehub.md)
  An error indicating no compatible home hub found.
- [static var incompatibleHomeHub: HMError.Code](hmerror/code/incompatiblehomehub.md)
  An error indicating an incompatible home hub.
### Detecting limit errors
- [static var cannotActivateTriggerTooFarInFuture: HMError.Code](hmerror/cannotactivatetriggertoofarinfuture.md)
  An error indicating the trigger cannot be activated because it is set too far in the future.
- [static var dateMustBeOnSpecifiedBoundaries: HMError.Code](hmerror/datemustbeonspecifiedboundaries.md)
  An error indicating the date is not on the specified boundaries.
- [static var fireDateInPast: HMError.Code](hmerror/firedateinpast.md)
  An attempt to activate a timer trigger with a date in the past.
- [static var invalidMessageSize: HMError.Code](hmerror/invalidmessagesize.md)
  An error indicating an invalid message size.
- [static var maximumObjectLimitReached: HMError.Code](hmerror/maximumobjectlimitreached.md)
  An error indicating the maximum object count has been reached.
- [static var recurrenceTooLarge: HMError.Code](hmerror/recurrencetoolarge.md)
  An attempt to use a recurrence period that is too large.
- [static var recurrenceTooSmall: HMError.Code](hmerror/recurrencetoosmall.md)
  An error indicating the recurrence interval is too short.
- [static var recurrenceMustBeOnSpecifiedBoundaries: HMError.Code](hmerror/recurrencemustbeonspecifiedboundaries.md)
  An error indicating the recurrence rule is not on the specified boundaries.
### Detecting network errors
- [static var enterpriseNetworkNotSupported: HMError.Code](hmerror/enterprisenetworknotsupported.md)
  An enterprise network doesn’t support this accessory.
- [static var failedToJoinNetwork: HMError.Code](hmerror/failedtojoinnetwork.md)
  The accessory failed to join the network.
- [static var incompatibleNetwork: HMError.Code](hmerror/incompatiblenetwork.md)
  An error indicating an incompatible network.
- [static var networkUnavailable: HMError.Code](hmerror/networkunavailable.md)
  An error indicating the network is unavailable.
- [static var wiFiCredentialGenerationFailed: HMError.Code](hmerror/wificredentialgenerationfailed.md)
  WiFi credential generation failed.
### Detecting operation errors
- [static var operationCancelled: HMError.Code](hmerror/operationcancelled.md)
  An error indicating the user canceled the operation.
- [static var operationInProgress: HMError.Code](hmerror/operationinprogress.md)
  An error indicating the operation is already in progress.
- [static var operationTimedOut: HMError.Code](hmerror/operationtimedout.md)
  An error indicating the operation timed out.
### Detecting parameter errors
- [static var invalidParameter: HMError.Code](hmerror/invalidparameter.md)
  An error indicating the object is invalid for the given operation.
- [static var missingParameter: HMError.Code](hmerror/missingparameter.md)
  An error indicating a missing parameter.
- [static var nilParameter: HMError.Code](hmerror/nilparameter.md)
  An error indicating that nil was passed for an operation that does not accept nil.
- [static var unconfiguredParameter: HMError.Code](hmerror/unconfiguredparameter.md)
  An error indicating an unconfigured parameter.
### Detecting read and write errors
- [static var readWriteFailure: HMError.Code](hmerror/readwritefailure.md)
  An error indicating a failed read/write operation.
- [static var readWritePartialSuccess: HMError.Code](hmerror/readwritepartialsuccess.md)
  An error indicating a partially successful read/write operation.
### Detecting synchronization errors
- [static var cloudDataSyncInProgress: HMError.Code](hmerror/clouddatasyncinprogress.md)
  An error indicating a data synchronization operation is in progress.
- [static var keychainSyncNotEnabled: HMError.Code](hmerror/keychainsyncnotenabled.md)
  An error indicating Keychain syncing is not enabled for the user.
### Detecting user errors
- [static var userDeclinedAddingUser: HMError.Code](hmerror/userdeclinedaddinguser.md)
  An error indicating the user canceled the add user operation.
- [static var userDeclinedRemovingUser: HMError.Code](hmerror/userdeclinedremovinguser.md)
  An error indicating the user canceled the remove user operation.
- [static var userDeclinedInvite: HMError.Code](hmerror/userdeclinedinvite.md)
  An error indicating the user declined the invitation.
- [static var userIDNotEmailAddress: HMError.Code](hmerror/useridnotemailaddress.md)
  An error indicating the user’s ID is not a valid email address.
- [static var userManagementFailed: HMError.Code](hmerror/usermanagementfailed.md)
  A user management error not covered by the other errors.
### Detecting value errors
- [static var invalidDataFormatSpecified: HMError.Code](hmerror/invaliddataformatspecified.md)
  An error indicating an invalid data format was specified.
- [static var invalidValueType: HMError.Code](hmerror/invalidvaluetype.md)
  An attempt to use an invalid value type.
- [static var nameContainsProhibitedCharacters: HMError.Code](hmerror/namecontainsprohibitedcharacters.md)
  An attempt to name an object with prohibited characters.
- [static var nameDoesNotEndWithValidCharacters: HMError.Code](hmerror/namedoesnotendwithvalidcharacters.md)
  An error indicating the provided name has invalid characters at the end.
- [static var nameDoesNotStartWithValidCharacters: HMError.Code](hmerror/namedoesnotstartwithvalidcharacters.md)
  An attempt to start the name of an object with invalid characters.
- [static var stringLongerThanMaximum: HMError.Code](hmerror/stringlongerthanmaximum.md)
  An attempt to use a string longer than the maximum allowed.
- [static var stringShorterThanMinimum: HMError.Code](hmerror/stringshorterthanminimum.md)
  An attempt to use a string shorter than the required minimum.
- [static var valueHigherThanMaximum: HMError.Code](hmerror/valuehigherthanmaximum.md)
  An attempt to use a numeric value higher than the specified maximum value.
- [static var valueLowerThanMinimum: HMError.Code](hmerror/valuelowerthanminimum.md)
  An attempt to use a numeric value lower than the specified minimum value.
### Enumerating errors
- [HMError.Code](hmerror/code.md)
  Possible error values that can be returned from HomeKit APIs.
### Type Properties
- [static var errorDomain: String](hmerror/errordomain.md)
- [static var homeUpgradeRequired: HMError.Code](hmerror/homeupgraderequired.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let HMErrorDomain: String](hmerrordomain.md)
  A string that identifies the HomeKit error domain.
- [HMError.Code](hmerror/code.md)
  Possible error values that can be returned from HomeKit APIs.
- [typealias HMErrorBlock](hmerrorblock.md)
  A completion block that provides an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror)*