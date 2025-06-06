# OpenDirectory Constants

**Framework**: Open Directory

## Topics

### Constants
- [let ODFrameworkErrorDomain: String](odframeworkerrordomain.md)
- [let ODSessionProxyAddress: String](odsessionproxyaddress.md)
  The address to connect to via proxy. The value is of type `NSString`.
- [let ODSessionProxyPassword: String](odsessionproxypassword.md)
  The password to connect with via proxy. The value is of type `NSString`.
- [let ODSessionProxyPort: String](odsessionproxyport.md)
  The port to connect to via proxy. The value is of type `NSNumber`.
- [let ODSessionProxyUsername: String](odsessionproxyusername.md)
  The username to connect with via proxy. The value is of type `NSString`.
- [let ODTrustTypeAnonymous: String](odtrusttypeanonymous.md)
- [let ODTrustTypeJoined: String](odtrusttypejoined.md)
- [let ODTrustTypeUsingCredentials: String](odtrusttypeusingcredentials.md)
- [let kODAttributeTypeAltSecurityIdentities: String](kodattributetypealtsecurityidentities.md)
- [let kODAttributeTypeHardwareUUID: String](kodattributetypehardwareuuid.md)
- [let kODAttributeTypeMetaAmbiguousName: String](kodattributetypemetaambiguousname.md)
- [let kODAttributeTypeMetaAugmentedAttributes: String](kodattributetypemetaaugmentedattributes.md)
- [let kODAttributeTypeMetaRecordName: String](kodattributetypemetarecordname.md)
- [let kODAttributeTypeNodeOptions: String](kodattributetypenodeoptions.md)
- [let kODAttributeTypeNodeSASLRealm: String](kodattributetypenodesaslrealm.md)
- [let kODAttributeTypeOperatingSystem: String](kodattributetypeoperatingsystem.md)
- [let kODAttributeTypeOperatingSystemVersion: String](kodattributetypeoperatingsystemversion.md)
- [let kODAttributeTypeProfiles: String](kodattributetypeprofiles.md)
- [let kODAttributeTypeProfilesTimestamp: String](kodattributetypeprofilestimestamp.md)
- [let kODAttributeTypeTrustInformation: String](kodattributetypetrustinformation.md)
- [var kODErrorCredentialsAccountDisabled: ODFrameworkErrors](koderrorcredentialsaccountdisabled.md)
  The account is disabled.
- [var kODErrorCredentialsAccountExpired: ODFrameworkErrors](koderrorcredentialsaccountexpired.md)
  The account is expired.
- [var kODErrorCredentialsAccountInactive: ODFrameworkErrors](koderrorcredentialsaccountinactive.md)
  The account is inactive.
- [var kODErrorCredentialsAccountNotFound: ODFrameworkErrors](koderrorcredentialsaccountnotfound.md)
  The authentication server could not find the provided account.
- [var kODErrorCredentialsInvalid: ODFrameworkErrors](koderrorcredentialsinvalid.md)
  The provided credentials are invalid with the current node.
- [var kODErrorCredentialsInvalidComputer: ODFrameworkErrors](koderrorcredentialsinvalidcomputer.md)
  The account is not permitted to log into this computer.
- [var kODErrorCredentialsInvalidLogonHours: ODFrameworkErrors](koderrorcredentialsinvalidlogonhours.md)
  The logon attempt was not within set logon hours.
- [var kODErrorCredentialsMethodNotSupported: ODFrameworkErrors](koderrorcredentialsmethodnotsupported.md)
  The extended authentication method is not supported.
- [var kODErrorCredentialsNotAuthorized: ODFrameworkErrors](koderrorcredentialsnotauthorized.md)
  The operation, such as changing a password, is not permitted with current privileges.
- [var kODErrorCredentialsOperationFailed: ODFrameworkErrors](koderrorcredentialsoperationfailed.md)
  The requested operation failed.
- [var kODErrorCredentialsParameterError: ODFrameworkErrors](koderrorcredentialsparametererror.md)
  An invalid parameter was provided.
- [var kODErrorCredentialsPasswordChangeRequired: ODFrameworkErrors](koderrorcredentialspasswordchangerequired.md)
  The password must be changed.
- [var kODErrorCredentialsPasswordChangeTooSoon: ODFrameworkErrors](koderrorcredentialspasswordchangetoosoon.md)
  The password was changed too recently to be changed again.
- [var kODErrorCredentialsPasswordExpired: ODFrameworkErrors](koderrorcredentialspasswordexpired.md)
  The password has expired and must be changed.
- [var kODErrorCredentialsPasswordNeedsDigit: ODFrameworkErrors](koderrorcredentialspasswordneedsdigit.md)
  The provided password needs at least one digit.
- [var kODErrorCredentialsPasswordNeedsLetter: ODFrameworkErrors](koderrorcredentialspasswordneedsletter.md)
  The provided password needs at least one letter.
- [var kODErrorCredentialsPasswordQualityFailed: ODFrameworkErrors](koderrorcredentialspasswordqualityfailed.md)
  The provided password did not meet minimum quality requirements.
- [var kODErrorCredentialsPasswordTooLong: ODFrameworkErrors](koderrorcredentialspasswordtoolong.md)
  The provided password is too long.
- [var kODErrorCredentialsPasswordTooShort: ODFrameworkErrors](koderrorcredentialspasswordtooshort.md)
  The provided password is too short.
- [var kODErrorCredentialsPasswordUnrecoverable: ODFrameworkErrors](koderrorcredentialspasswordunrecoverable.md)
  The password could not be recovered from the authentication database.
- [var kODErrorCredentialsServerCommunicationError: ODFrameworkErrors](koderrorcredentialsservercommunicationerror.md)
  The authentication server encountered a communication error.
- [var kODErrorCredentialsServerError: ODFrameworkErrors](koderrorcredentialsservererror.md)
  The authentication server encountered an error.
- [var kODErrorCredentialsServerNotFound: ODFrameworkErrors](koderrorcredentialsservernotfound.md)
  The authentication server could not be found.
- [var kODErrorCredentialsServerTimeout: ODFrameworkErrors](koderrorcredentialsservertimeout.md)
  The authentication server timed out.
- [var kODErrorCredentialsServerUnreachable: ODFrameworkErrors](koderrorcredentialsserverunreachable.md)
  The authentication server could not be reached.
- [var kODErrorDaemonError: ODFrameworkErrors](koderrordaemonerror.md)
  The daemon has encountered an undefined error.
- [let kODErrorDomainFramework: CFString!](koderrordomainframework.md)
  The error domain used for errors from the Open Directory framework.
- [var kODErrorNodeConnectionFailed: ODFrameworkErrors](koderrornodeconnectionfailed.md)
  The node connection failed.
- [var kODErrorNodeDisabled: ODFrameworkErrors](koderrornodedisabled.md)
- [var kODErrorNodeUnknownHost: ODFrameworkErrors](koderrornodeunknownhost.md)
  The host provided is invalid.
- [var kODErrorNodeUnknownName: ODFrameworkErrors](koderrornodeunknownname.md)
  The node name provided does not exist and cannot be opened.
- [var kODErrorNodeUnknownType: ODFrameworkErrors](koderrornodeunknowntype.md)
  The node type provided is not a known value.
- [var kODErrorPluginError: ODFrameworkErrors](koderrorpluginerror.md)
  A plug-in has encountered an undefined error.
- [var kODErrorPluginOperationNotSupported: ODFrameworkErrors](koderrorpluginoperationnotsupported.md)
  The plug-in does not support the requested operation.
- [var kODErrorPluginOperationTimeout: ODFrameworkErrors](koderrorpluginoperationtimeout.md)
- [var kODErrorPolicyOutOfRange: ODFrameworkErrors](koderrorpolicyoutofrange.md)
- [var kODErrorPolicyUnsupported: ODFrameworkErrors](koderrorpolicyunsupported.md)
- [var kODErrorQueryInvalidMatchType: ODFrameworkErrors](koderrorqueryinvalidmatchtype.md)
  An invalid match type was provided in the query.
- [var kODErrorQuerySynchronize: ODFrameworkErrors](koderrorquerysynchronize.md)
  A query synchronization has been initiated.
- [var kODErrorQueryTimeout: ODFrameworkErrors](koderrorquerytimeout.md)
  The query timed out.
- [var kODErrorQueryUnsupportedMatchType: ODFrameworkErrors](koderrorqueryunsupportedmatchtype.md)
  An unsupported match type was provided in the query.
- [var kODErrorRecordAlreadyExists: ODFrameworkErrors](koderrorrecordalreadyexists.md)
  The record create failed because the record already exists.
- [var kODErrorRecordAttributeNotFound: ODFrameworkErrors](koderrorrecordattributenotfound.md)
  The requested attribute could not be found in the record.
- [var kODErrorRecordAttributeUnknownType: ODFrameworkErrors](koderrorrecordattributeunknowntype.md)
  The attribute type is unknown.
- [var kODErrorRecordAttributeValueNotFound: ODFrameworkErrors](koderrorrecordattributevaluenotfound.md)
  The requested attribute value could not be found in the record.
- [var kODErrorRecordAttributeValueSchemaError: ODFrameworkErrors](koderrorrecordattributevalueschemaerror.md)
  The attribute value does not meet schema requirements.
- [var kODErrorRecordInvalidType: ODFrameworkErrors](koderrorrecordinvalidtype.md)
- [var kODErrorRecordNoLongerExists: ODFrameworkErrors](koderrorrecordnolongerexists.md)
- [var kODErrorRecordParameterError: ODFrameworkErrors](koderrorrecordparametererror.md)
  An invalid parameter was provided.
- [var kODErrorRecordPermissionError: ODFrameworkErrors](koderrorrecordpermissionerror.md)
  The changes were denied due to insufficient permissions.
- [var kODErrorRecordReadOnlyNode: ODFrameworkErrors](koderrorrecordreadonlynode.md)
  The record cannot be modified.
- [var kODErrorRecordTypeDisabled: ODFrameworkErrors](koderrorrecordtypedisabled.md)
  The record type is disabled by policy for a plug-in.
- [var kODErrorSessionDaemonNotRunning: ODFrameworkErrors](koderrorsessiondaemonnotrunning.md)
  The daemon is not running.
- [var kODErrorSessionDaemonRefused: ODFrameworkErrors](koderrorsessiondaemonrefused.md)
  The daemon refused the session.
- [var kODErrorSessionLocalOnlyDaemonInUse: ODFrameworkErrors](koderrorsessionlocalonlydaemoninuse.md)
  A normal request was issued when the local-only daemon was in use.
- [var kODErrorSessionNormalDaemonInUse: ODFrameworkErrors](koderrorsessionnormaldaemoninuse.md)
  A local-only request was issued when the normal daemon was in use.
- [var kODErrorSessionProxyCommunicationError: ODFrameworkErrors](koderrorsessionproxycommunicationerror.md)
  There was a communication error with the remote daemon.
- [var kODErrorSessionProxyIPUnreachable: ODFrameworkErrors](koderrorsessionproxyipunreachable.md)
  The proxy did not respond.
- [var kODErrorSessionProxyUnknownHost: ODFrameworkErrors](koderrorsessionproxyunknownhost.md)
  The proxy could not be resolved.
- [var kODErrorSessionProxyVersionMismatch: ODFrameworkErrors](koderrorsessionproxyversionmismatch.md)
  Versions mismatch between the remote daemon and the local framework.
- [var kODErrorSuccess: ODFrameworkErrors](koderrorsuccess.md)
- [let kODModuleConfigOptionConnectionIdleDisconnect: CFString!](kodmoduleconfigoptionconnectionidledisconnect.md)
- [let kODModuleConfigOptionConnectionSetupTimeout: CFString!](kodmoduleconfigoptionconnectionsetuptimeout.md)
- [let kODModuleConfigOptionManInTheMiddle: CFString!](kodmoduleconfigoptionmaninthemiddle.md)
- [let kODModuleConfigOptionPacketEncryption: CFString!](kodmoduleconfigoptionpacketencryption.md)
- [let kODModuleConfigOptionPacketSigning: CFString!](kodmoduleconfigoptionpacketsigning.md)
- [let kODModuleConfigOptionQueryTimeout: CFString!](kodmoduleconfigoptionquerytimeout.md)
- [let kODNodeOptionsQuerySkippedSubnode: CFString!](kodnodeoptionsqueryskippedsubnode.md)
- [let kODPolicyAttributeCreationTime: String](kodpolicyattributecreationtime.md)
- [let kODPolicyAttributeCurrentDate: String](kodpolicyattributecurrentdate.md)
- [let kODPolicyAttributeCurrentDayOfWeek: String](kodpolicyattributecurrentdayofweek.md)
- [let kODPolicyAttributeCurrentTime: String](kodpolicyattributecurrenttime.md)
- [let kODPolicyAttributeCurrentTimeOfDay: String](kodpolicyattributecurrenttimeofday.md)
- [let kODPolicyAttributeDaysUntilExpiration: String](kodpolicyattributedaysuntilexpiration.md)
- [let kODPolicyAttributeEnableAtTimeOfDay: String](kodpolicyattributeenableattimeofday.md)
- [let kODPolicyAttributeEnableOnDate: String](kodpolicyattributeenableondate.md)
- [let kODPolicyAttributeEnableOnDayOfWeek: String](kodpolicyattributeenableondayofweek.md)
- [let kODPolicyAttributeExpiresAtTimeOfDay: String](kodpolicyattributeexpiresattimeofday.md)
- [let kODPolicyAttributeExpiresEveryNDays: String](kodpolicyattributeexpireseveryndays.md)
- [let kODPolicyAttributeExpiresOnDate: String](kodpolicyattributeexpiresondate.md)
- [let kODPolicyAttributeExpiresOnDayOfWeek: String](kodpolicyattributeexpiresondayofweek.md)
- [let kODPolicyAttributeFailedAuthentications: String](kodpolicyattributefailedauthentications.md)
- [let kODPolicyAttributeLastAuthenticationTime: String](kodpolicyattributelastauthenticationtime.md)
- [let kODPolicyAttributeLastFailedAuthenticationTime: String](kodpolicyattributelastfailedauthenticationtime.md)
- [let kODPolicyAttributeLastPasswordChangeTime: String](kodpolicyattributelastpasswordchangetime.md)
- [let kODPolicyAttributeMaximumFailedAuthentications: String](kodpolicyattributemaximumfailedauthentications.md)
- [let kODPolicyAttributeNewPasswordRequiredTime: String](kodpolicyattributenewpasswordrequiredtime.md)
- [let kODPolicyAttributePassword: String](kodpolicyattributepassword.md)
- [let kODPolicyAttributePasswordHashes: String](kodpolicyattributepasswordhashes.md)
- [let kODPolicyAttributePasswordHistory: String](kodpolicyattributepasswordhistory.md)
- [let kODPolicyAttributePasswordHistoryDepth: String](kodpolicyattributepasswordhistorydepth.md)
- [let kODPolicyAttributeRecordName: String](kodpolicyattributerecordname.md)
- [let kODPolicyAttributeRecordType: String](kodpolicyattributerecordtype.md)
- [let kODPolicyCategoryAuthentication: String](kodpolicycategoryauthentication.md)
- [let kODPolicyCategoryPasswordChange: String](kodpolicycategorypasswordchange.md)
- [let kODPolicyCategoryPasswordContent: String](kodpolicycategorypasswordcontent.md)
- [let kODPolicyKeyContent: String](kodpolicykeycontent.md)
- [let kODPolicyKeyContentDescription: String](kodpolicykeycontentdescription.md)
- [let kODPolicyKeyEvaluationDetails: String](kodpolicykeyevaluationdetails.md)
- [let kODPolicyKeyIdentifier: String](kodpolicykeyidentifier.md)
- [let kODPolicyKeyParameters: String](kodpolicykeyparameters.md)
- [let kODPolicyKeyPolicySatisfied: String](kodpolicykeypolicysatisfied.md)
- [let kODPolicyTypeAccountExpiresOnDate: String](kodpolicytypeaccountexpiresondate.md)
- [let kODPolicyTypeAccountMaximumFailedLogins: String](kodpolicytypeaccountmaximumfailedlogins.md)
- [let kODPolicyTypeAccountMaximumMinutesOfNonUse: String](kodpolicytypeaccountmaximumminutesofnonuse.md)
- [let kODPolicyTypeAccountMaximumMinutesUntilDisabled: String](kodpolicytypeaccountmaximumminutesuntildisabled.md)
- [let kODPolicyTypeAccountMinutesUntilFailedLoginReset: String](kodpolicytypeaccountminutesuntilfailedloginreset.md)
- [let kODPolicyTypePasswordCannotBeAccountName: String](kodpolicytypepasswordcannotbeaccountname.md)
- [let kODPolicyTypePasswordChangeRequired: String](kodpolicytypepasswordchangerequired.md)
- [let kODPolicyTypePasswordHistory: String](kodpolicytypepasswordhistory.md)
- [let kODPolicyTypePasswordMaximumAgeInMinutes: String](kodpolicytypepasswordmaximumageinminutes.md)
- [let kODPolicyTypePasswordMaximumNumberOfCharacters: String](kodpolicytypepasswordmaximumnumberofcharacters.md)
- [let kODPolicyTypePasswordMinimumNumberOfCharacters: String](kodpolicytypepasswordminimumnumberofcharacters.md)
- [let kODPolicyTypePasswordRequiresAlpha: String](kodpolicytypepasswordrequiresalpha.md)
- [let kODPolicyTypePasswordRequiresMixedCase: String](kodpolicytypepasswordrequiresmixedcase.md)
- [let kODPolicyTypePasswordRequiresNumeric: String](kodpolicytypepasswordrequiresnumeric.md)
- [let kODPolicyTypePasswordRequiresSymbol: String](kodpolicytypepasswordrequiressymbol.md)
- [let kODPolicyTypePasswordSelfModification: String](kodpolicytypepasswordselfmodification.md)
- [let kODRecordTypeQueryInformation: String](kodrecordtypequeryinformation.md)
- [let kODAuthenticationTypeClearTextReadOnly: String](kodauthenticationtypecleartextreadonly.md)
- [let kODAuthenticationTypeMPPEPrimaryKeys: String](kodauthenticationtypemppeprimarykeys.md)
- [let kODBackOffSeconds: String](kodbackoffseconds.md)
- [var kODErrorCredentialsAccountLocked: ODFrameworkErrors](koderrorcredentialsaccountlocked.md)
- [var kODErrorCredentialsAccountTemporarilyLocked: ODFrameworkErrors](koderrorcredentialsaccounttemporarilylocked.md)
- [var kODErrorCredentialsContactPrimary: ODFrameworkErrors](koderrorcredentialscontactprimary.md)

## See Also

- [OpenDirectory Functions](opendirectory-functions.md)
  This document describes the functions, constants, and data types used to interact with Open Directory.
- [OpenDirectory Enumerations](opendirectory-enumerations.md)
- [OpenDirectory Data Types](opendirectory-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/opendirectory-constants)*