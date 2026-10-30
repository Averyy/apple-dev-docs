# Apple Business API

**Framework**: AppleBusinessAPI  
**Kind**: module  
**Role**: Web Service

Automate device management activities, view device information, and manage users and user groups in Apple Business.

**Availability**:
- Apple Business API 2.7+

## Overview

> **Note**: This API is a part of the [Apple School Manager and Apple Business APIs](../apple-school-and-business-manager-api/apple-school-and-business-manager-api.md) collection.

## Topics

### Authentication
- [Implementing OAuth for the Apple School Manager and Apple Business API](../apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-manager-and-apple-business-api.md)
  Manage secure access to Apple School Manager and Apple Business API accounts.
### Devices
- [Get Organization Devices](./get-org-devices.md)
  Get a list of devices in an organization that enroll using Automated Device Enrollment.
- [Get Device Information](./get-orgdevice-information.md)
  Get information about a device in an organization.
- [Get AppleCare coverage Information for a Device](./get-all-applecare-coverage-for-an-orgdevice.md)
  Get a list of AppleCare coverage resources for an organization device.
- [Get Devices Enrolled in Apple Device Management Service](./get-apple-mdm-enrolled-devices.md)
  Get a list of devices enrolled in Apple Device Management service.
- [Get Details for a Device Enrolled in Apple Device Management Service](./get-the-details-for-apple-mdm-enrolled-device.md)
  Get detailed information about a device enrolled in Apple Device Management service.
### Device Management Services
- [Get Device Management Services](./get-mdm-servers.md)
  Get a list of device management services in an organization.
- [Get Device Management Service Information](./get-mdmserver-information.md)
  Get the information for a specific device management service.
- [Create a Device Management Service](./create-an-mdmserver.md)
  Create a new device management service in an organization.
- [Update a Device Management Service](./update-an-mdmserver.md)
  Update an existing device management service in an organization.
- [Delete a Device Management Service](./delete-an-mdmserver.md)
  Delete a device management service from an organization.
- [Get the Device Serial Numbers for a Device Management Service](./get-all-device-ids-for-an-mdmserver.md)
  Get a list of device serial numbers assigned to a device management service.
- [Get the Assigned Device Management Service ID for a Device](./get-the-assigned-server-id-for-an-orgdevice.md)
  Get the assigned device management service ID information for a device.
- [Get the Assigned Device Management Service Information for a Device](./get-the-assigned-server-information-for-an-orgdevice.md)
  Get the assigned device management service information for a device.
- [Assign or Unassign Devices to a Device Management Service or Release Devices](./create-an-orgdeviceactivity.md)
  Assign or unassign devices to a device management service, manage a device management service migration for devices, or release devices from an organization.
- [Get Organization Device Activity Information](./get-orgdeviceactivity-information.md)
  Get information for an organization device activity that a device management action, such as assign or unassign, creates.
### Users
- [Get Users](./get-users.md)
  Get a list of users in an organization.
- [Get User Information](./get-user-information.md)
  Get information about a specific user in an organization.
### UserGroups
- [Get User Groups](./get-user-groups.md)
  Get a list of user groups in an organization.
- [Get User Group Information](./get-usergroup-information.md)
  Get information about a specific user group in an organization.
- [Get User IDs for a User Group](./get-all-user-ids-for-a-user-group.md)
  Get a list of user IDs for a user group in an organization.
### Organizational Units
- [Get Organizational Units](./get-organizational-units.md)
  Get a list of organizational units in an organization.
- [Get Organizational Unit Information](./get-organizationalunit-information.md)
  Get information about a specific organizational unit in an organization.
### Apps and Packages
- [Get Apps](./get-apps.md)
  Get a list of apps for an organization using the built-in device management in Apple Business.
- [Get App Information](./get-app-information.md)
  Get information about a specific app for an organization using the built-in device management in Apple Business.
- [Get Packages](./get-packages.md)
  Get a list of packages for an organization using Apple Business’s built-in device management.
- [Get Package Information](./get-package-information.md)
  Get information about a specific package for an organization using Apple Business’s built-in device management.
### Blueprints
- [Get Blueprints](./get-blueprints.md)
  Get a list of Blueprints in an organization.
- [Create a Blueprint](./create-a-blueprint.md)
  Create a new Blueprint in an organization.
- [Get Blueprint Information](./get-blueprint-information.md)
  Get information about a specific Blueprint in an organization.
- [Update a Blueprint](./update-a-blueprint.md)
  Update an existing Blueprint in an organization.
- [Delete a Blueprint](./delete-a-blueprint.md)
  Delete a Blueprint from an organization.
- [Get App IDs for a Blueprint](./get-all-app-ids-for-a-blueprint.md)
  Get a list of app IDs associated with a Blueprint.
- [Add Apps to a Blueprint](./add-apps-to-a-blueprint.md)
  Add apps to a Blueprint.
- [Remove Apps from a Blueprint](./remove-apps-from-a-blueprint.md)
  Remove apps from a Blueprint.
- [Get Configuration IDs for a Blueprint](./get-all-configuration-ids-for-a-blueprint.md)
  Get a list of Configuration IDs associated with a Blueprint.
- [Add Configurations to a Blueprint](./add-configurations-to-a-blueprint.md)
  Add Configurations to a Blueprint.
- [Remove Configurations from a Blueprint](./remove-configurations-from-a-blueprint.md)
  Remove Configurations from a Blueprint.
- [Get Package IDs for a Blueprint](./get-all-package-ids-for-a-blueprint.md)
  Get a list of package IDs associated with a Blueprint.
- [Add Packages to a Blueprint](./add-packages-to-a-blueprint.md)
  Add packages to a Blueprint.
- [Remove Packages from a Blueprint](./remove-packages-from-a-blueprint.md)
  Remove packages from a Blueprint.
- [Get Device IDs for a Blueprint](./get-all-orgdevice-ids-for-a-blueprint.md)
  Get a list of device IDs associated with a Blueprint.
- [Add Devices to a Blueprint](./add-org-devices-to-a-blueprint.md)
  Add devices to a Blueprint.
- [Remove Devices from a Blueprint](./remove-org-devices-from-a-blueprint.md)
  Remove devices from a Blueprint.
- [Get User IDs for a Blueprint](./get-all-user-ids-for-a-blueprint.md)
  Get a list of user IDs associated with a Blueprint.
- [Add Users to a Blueprint](./add-users-to-a-blueprint.md)
  Add users to a Blueprint.
- [Remove Users from a Blueprint](./remove-users-from-a-blueprint.md)
  Remove users from a Blueprint.
- [Get User Group IDs for a Blueprint](./get-all-user-group-ids-for-a-blueprint.md)
  Get a list of user group IDs associated with a Blueprint.
- [Add User Groups to a Blueprint](./add-user-groups-to-a-blueprint.md)
  Add user groups to a Blueprint.
- [Remove User Groups from a Blueprint](./remove-user-groups-from-a-blueprint.md)
  Remove user groups from a Blueprint.
### Configurations
- [Get Configurations](./get-configurations.md)
  Get a list of Configurations in an organization.
- [Create a Configuration](./create-a-configuration.md)
  Create a new custom Configuration in an organization.
- [Get Configuration Information](./get-configuration-information.md)
  Get information about a specific Configuration in an organization.
- [Update a Configuration](./update-a-configuration.md)
  Update an existing custom Configuration in an organization.
- [Delete a Configuration](./delete-a-configuration.md)
  Delete a Configuration from an organization.
### Audit Events
- [Get Audit Events](./get-audit-events.md)
  Get a list of audit events in an organization that satisfies the query criteria.
### Objects and Data Types
- [object OrgDevice](./orgdevice.md)
  The data structure that represents an organization device resource.
- [object OrgDeviceResponse](./orgdeviceresponse.md)
  A response that contains a single organization device resource.
- [object OrgDevicesResponse](./orgdevicesresponse.md)
  A response that contains a list of organization device resources.
- [object OrgDeviceAssignedServerLinkageResponse](./orgdeviceassignedserverlinkageresponse.md)
  The data and links that describe the relationship between the resources.
- [object MdmDevice](./mdmdevice.md)
  The data structure that represents a device management service enrolled device resource.
- [object MdmDeviceResponse](./mdmdeviceresponse.md)
  A response that contains a list of Apple devices enrolled in a device management service.
- [object MdmDevicesResponse](./mdmdevicesresponse.md)
  A response that contains a list of Apple devices enrolled in a device management service.
- [object MdmDeviceDetail](./mdmdevicedetail.md)
  The data structure that represents the detailed information for a device management service enrolled device resource.
- [object MdmDeviceDetailResponse](./mdmdevicedetailresponse.md)
  A response that contains the detailed information for an Apple device enrolled in a device management service.
- [object MdmServer](./mdmserver.md)
  The data structure that represents a device management service resource in an organization.
- [object MdmServerResponse](./mdmserverresponse.md)
  A response that contains a single device management service resource.
- [object MdmServersResponse](./mdmserversresponse.md)
  A response that contains a list of device management service resources.
- [object MdmServerDevicesLinkagesResponse](./mdmserverdeviceslinkagesresponse.md)
  The data and links that describe the relationship between the resources.
- [object OrgDeviceActivity](./orgdeviceactivity.md)
  The data structure that represents an organization device activity resource.
- [object OrgDeviceActivityCreateRequest](./orgdeviceactivitycreaterequest.md)
  The request body you use to update the device management service for a device.
- [object OrgDeviceActivityResponse](./orgdeviceactivityresponse.md)
  A response that contains a single organization device activity resource.
- [object AppleCareCoverage](./applecarecoverage.md)
  The data structure that represents an AppleCare coverage resource that belongs to an organization device.
- [object AppleCareCoverageResponse](./applecarecoverageresponse.md)
  A response that contains a list of AppleCare coverage resources that belongs to an organization device.
- [object User](./user.md)
  The data structure that represents a user resource.
- [object UserResponse](./userresponse.md)
  A response that contains a single user resource.
- [object UsersResponse](./usersresponse.md)
  A response that contains a list of user resources.
- [object UserPhoneNumber](./userphonenumber.md)
  The data structure that represents a user’s phone number.
- [object UserRoleOuMapping](./userroleoumapping.md)
  The data structure that represents a user’s role and organizational unit mapping.
- [object UserGroup](./usergroup.md)
  The data structure that represents a user group resource.
- [object UserGroupResponse](./usergroupresponse.md)
  A response that contains a single user group resource.
- [object UserGroupsResponse](./usergroupsresponse.md)
  A response that contains a list of user group resources.
- [object UserGroupUsersLinkagesResponse](./usergroupuserslinkagesresponse.md)
  A response that contains a list of user IDs for a user group.
- [object OrganizationalUnit](./organizationalunit.md)
  The data structure that represents an organizational unit resource.
- [object OrganizationalUnitResponse](./organizationalunitresponse.md)
  A response that contains a single organizational unit resource.
- [object OrganizationalUnitsResponse](./organizationalunitsresponse.md)
  A response that contains a list of organizational unit resources.
- [object OrganizationalUnitUsersLinkagesResponse](./organizationalunituserslinkagesresponse.md)
  A response that contains a list of user IDs for an organizational unit.
- [object App](./app.md)
  The data structure that represents an app resource.
- [object AppResponse](./appresponse.md)
  A response that contains information about an app resource.
- [object AppsResponse](./appsresponse.md)
  A response that contains a list of app resources.
- [object Package](./package.md)
  The data structure that represents a package resource.
- [object PackageResponse](./packageresponse.md)
  A response that contains information about a package resource.
- [object PackagesResponse](./packagesresponse.md)
  A response that contains a list of package resources.
- [object Blueprint](./blueprint.md)
  The data structure that represents a Blueprint resource.
- [object BlueprintResponse](./blueprintresponse.md)
  A response that contains information about a Blueprint resource.
- [object BlueprintsResponse](./blueprintsresponse.md)
  A response that contains a list of Blueprint resources.
- [object BlueprintCreateRequest](./blueprintcreaterequest.md)
  A request to create a new Blueprint.
- [object BlueprintUpdateRequest](./blueprintupdaterequest.md)
  A request to update an existing Blueprint.
- [object BlueprintAppsLinkagesRequest](./blueprintappslinkagesrequest.md)
  A request to get a list of app resource linkages for a Blueprint.
- [object BlueprintAppsLinkagesResponse](./blueprintappslinkagesresponse.md)
  A response that contains a list of app resource linkages for a Blueprint.
- [object BlueprintConfigurationsLinkagesRequest](./blueprintconfigurationslinkagesrequest.md)
  A request to get a list of Configuration resource linkages for a Blueprint.
- [object BlueprintConfigurationsLinkagesResponse](./blueprintconfigurationslinkagesresponse.md)
  A response that contains a list of Configuration resource linkages for a Blueprint.
- [object BlueprintPackagesLinkagesRequest](./blueprintpackageslinkagesrequest.md)
  A request to get a list of package resource linkages for a Blueprint.
- [object BlueprintPackagesLinkagesResponse](./blueprintpackageslinkagesresponse.md)
  A response that contains a list of package resource linkages for a Blueprint.
- [object BlueprintOrgDevicesLinkagesRequest](./blueprintorgdeviceslinkagesrequest.md)
  A request to get a list of device resource linkages for a Blueprint.
- [object BlueprintOrgDevicesLinkagesResponse](./blueprintorgdeviceslinkagesresponse.md)
  A response that contains a list of device resource linkages for a Blueprint.
- [object BlueprintUsersLinkagesRequest](./blueprintuserslinkagesrequest.md)
  A request to get a list of user resource linkages for a Blueprint.
- [object BlueprintUsersLinkagesResponse](./blueprintuserslinkagesresponse.md)
  A response that contains a list of user resource linkages for a Blueprint.
- [object BlueprintUserGroupsLinkagesRequest](./blueprintusergroupslinkagesrequest.md)
  A request to get a list of user group resource linkages for a Blueprint.
- [object BlueprintUserGroupsLinkagesResponse](./blueprintusergroupslinkagesresponse.md)
  A response that contains a list of user group resource linkages for a Blueprint.
- [object Configuration](./configuration.md)
  The data structure that represents a Configuration resource.
- [object ConfigurationResponse](./configurationresponse.md)
  A response that contains information about a Configuration resource.
- [object ConfigurationsResponse](./configurationsresponse.md)
  A response that contains a list of Configuration resources.
- [object ConfigurationCreateRequest](./configurationcreaterequest.md)
  A request to create a new Configuration.
- [object ConfigurationUpdateRequest](./configurationupdaterequest.md)
  A request to update an existing Configuration.
- [object ConfigurationCommon](./configurationcommon.md)
- [object ConfigurationCustomSetting](./configurationcustomsetting.md)
- [object CustomSettingsValues](./customsettingsvalues.md)
  The custom settings payload for a Configuration of type `CUSTOM_SETTING`.
- [object PagedDocumentLinks](./pageddocumentlinks.md)
  Links related to the response document, including paging links.
- [object PagingInformation](./paginginformation.md)
  Paging information for data responses.
- [object RelationshipLinks](./relationshiplinks.md)
  Links related to the response document, including self-links.
- [object ResourceLinks](./resourcelinks.md)
  Self-links to requested resources.
- [object ErrorResponse](./errorresponse.md)
  The error details that an API returns in the response body whenever the API request isn’t successful.
- [object ErrorLinks](./errorlinks.md)
- [object JsonPointer](./jsonpointer.md)
  An object that contains the JSON pointer that indicates the location of the error.
- [object Parameter](./parameter.md)
  An object that contains the query parameter that produces the error.
- [object DocumentLinks](./documentlinks.md)
  Self-links to documents that can contain information for one or more resources.
### Type Aliases
- [type OrgDeviceActivityType](./orgdeviceactivitytype.md)
  Strings that represent organization device activities.
- [type AppleCareCoveragePaymentType](./applecarecoveragepaymenttype.md)
  Strings that represent AppleCare coverage payment types.
- [type AppleCareCoverageStatus](./applecarecoveragestatus.md)
  Strings that represent AppleCare coverage status.
- [type UserStatus](./userstatus.md)
  Strings that represent user statuses.
- [type UserPhoneNumberType](./userphonenumbertype.md)
  Strings that represent phone number types.
- [type UserGroupStatus](./usergroupstatus.md)
  Strings that represent user group statuses.
- [type UserGroupType](./usergrouptype.md)
  Strings that represent user group types.
- [type SupportedOS](./supportedos.md)
  The supported operating systems for an app.
- [type BlueprintStatus](./blueprintstatus.md)
  The status of a Blueprint.
- [type ConfigurationType](./configurationtype.md)
  The type of Configuration profile.
- [type ConfigurationPlatform](./configurationplatform.md)
  The platform that a Configuration targets.
- [type ActivationLockType](./activationlocktype.md)
  Strings that represent the type of Activation Lock on a device.
- [type AuditEventActorType](./auditeventactortype.md)
  Strings that represent the type of entity that performed an action.
- [type AuditEventCategory](./auditeventcategory.md)
  Strings that represent audit event categories.
- [type AuditEventIdpProtocol](./auditeventidpprotocol.md)
  Strings that represent the federation protocol used by an identity provider.
- [type AuditEventIdpVendorName](./auditeventidpvendorname.md)
  Strings that represent the identity provider vendor.
- [type AuditEventOutcome](./auditeventoutcome.md)
  Strings that represent the result of an action.
- [type AuditEventPurchaseSourceType](./auditeventpurchasesourcetype.md)
  Strings that represent how a device was added to an organization.
- [type AuditEventReleaseEntityType](./auditeventreleaseentitytype.md)
  Strings that represent the type of entity that conducted the release operation.
- [type AuditEventSubjectType](./auditeventsubjecttype.md)
  Strings that represent the type of entity that was affected by an action.
- [type AuditEventType](./auditeventtype.md)
  Strings that represent audit event types.
- [type DeviceEraseStatus](./deviceerasestatus.md)
  Strings that represent device erase statuses.
- [type DeviceLockStatus](./devicelockstatus.md)
  Strings that represent device lock statuses.
- [type LostModeStatus](./lostmodestatus.md)
  Strings that represent lost mode statuses.
- [type MdmMigrationStatus](./mdmmigrationstatus.md)
  Strings that represent the state of a device’s device management service migration.
### Endpoints
- [Get All User IDs for an Organizational Unit](./get-all-user-ids-for-an-organizational-unit.md)
- [Get the Activation Lock Status for a Device](./get-the-activation-lock-status-information-for-an-orgdevice.md)
  Get the Activation Lock status of an organization device.
### Dictionaries
- [object ActivationLockStatus](./activationlockstatus.md)
  The data structure that represents the Activation Lock status of an organization device.
- [object ActivityTypeMetadata](./activitytypemetadata.md)
  Additional metadata for an organization device activity, used by device management service migration activity types.
- [object AuditEvent](./auditevent.md)
  The data structure that represents an audit event resource.
- [object AuditEventAccountAdded](./auditeventaccountadded.md)
  The data structure that represents the event data for an account added audit event.
- [object AuditEventAccountAddedAttributes](./auditeventaccountaddedattributes.md)
  The attributes for an account added audit event.
- [object AuditEventAccountDeleted](./auditeventaccountdeleted.md)
  The data structure that represents the event data for an account deleted audit event.
- [object AuditEventAccountDeletedAttributes](./auditeventaccountdeletedattributes.md)
  The attributes for an account deleted audit event.
- [object AuditEventAccountImageRemoved](./auditeventaccountimageremoved.md)
  The data structure that represents the event data for an account image removed audit event.
- [object AuditEventAccountImageRemovedAttributes](./auditeventaccountimageremovedattributes.md)
  The attributes for an account image removed audit event.
- [object AuditEventAccountImageReplaced](./auditeventaccountimagereplaced.md)
  The data structure that represents the event data for an account image replaced audit event.
- [object AuditEventAccountImageReplacedAttributes](./auditeventaccountimagereplacedattributes.md)
  The attributes for an account image replaced audit event.
- [object AuditEventAccountImageSet](./auditeventaccountimageset.md)
  The data structure that represents the event data for an account image set audit event.
- [object AuditEventAccountImageSetAttributes](./auditeventaccountimagesetattributes.md)
  The attributes for an account image set audit event.
- [object AuditEventAccountPasswordChanged](./auditeventaccountpasswordchanged.md)
  The data structure that represents the event data for an account password changed audit event.
- [object AuditEventAccountPasswordChangedAttributes](./auditeventaccountpasswordchangedattributes.md)
  The attributes for an account password changed audit event.
- [object AuditEventAccountRoleLocation](./auditeventaccountrolelocation.md)
  The data structure that represents a role and location assignment.
- [object AuditEventAccountRoleLocationChanged](./auditeventaccountrolelocationchanged.md)
  The data structure that represents the event data for an account role location changed audit event.
- [object AuditEventAccountRoleLocationChangedAttributes](./auditeventaccountrolelocationchangedattributes.md)
  The attributes for an account role location changed audit event.
- [object AuditEventApiAccountCreatedWithKey](./auditeventapiaccountcreatedwithkey.md)
  The data structure that represents the event data for an API account created with key audit event.
- [object AuditEventApiAccountCreatedWithKeyAttributes](./auditeventapiaccountcreatedwithkeyattributes.md)
  The attributes for an API account created with key audit event.
- [object AuditEventApiAccountCreatedWithoutKey](./auditeventapiaccountcreatedwithoutkey.md)
  The data structure that represents the event data for an API account created without key audit event.
- [object AuditEventApiAccountCreatedWithoutKeyAttributes](./auditeventapiaccountcreatedwithoutkeyattributes.md)
  The attributes for an API account created without key audit event.
- [object AuditEventApiAccountDeleted](./auditeventapiaccountdeleted.md)
  The data structure that represents the event data for an API account deleted audit event.
- [object AuditEventApiAccountDeletedAttributes](./auditeventapiaccountdeletedattributes.md)
  The attributes for an API account deleted audit event.
- [object AuditEventApiAccountKeyGenerated](./auditeventapiaccountkeygenerated.md)
  The data structure that represents the event data for an API account key generated audit event.
- [object AuditEventApiAccountKeyGeneratedAttributes](./auditeventapiaccountkeygeneratedattributes.md)
  The attributes for an API account key generated audit event.
- [object AuditEventApiAccountKeyRevoked](./auditeventapiaccountkeyrevoked.md)
  The data structure that represents the event data for an API account key revoked audit event.
- [object AuditEventApiAccountKeyRevokedAttributes](./auditeventapiaccountkeyrevokedattributes.md)
  The attributes for an API account key revoked audit event.
- [object AuditEventApiAccountNameChanged](./auditeventapiaccountnamechanged.md)
  The data structure that represents the event data for an API account name changed audit event.
- [object AuditEventApiAccountNameChangedAttributes](./auditeventapiaccountnamechangedattributes.md)
  The attributes for an API account name changed audit event.
- [object AuditEventApiAccountRoleLocationChanged](./auditeventapiaccountrolelocationchanged.md)
  The data structure that represents the event data for an API account role location changed audit event.
- [object AuditEventApiAccountRoleLocationChangedAttributes](./auditeventapiaccountrolelocationchangedattributes.md)
  The attributes for an API account role location changed audit event.
- [object AuditEventAppleServicesSettingsUpdated](./auditeventappleservicessettingsupdated.md)
  The data structure that represents the event data for an Apple services settings updated audit event.
- [object AuditEventAppleServicesSettingsUpdatedAttributes](./auditeventappleservicessettingsupdatedattributes.md)
  The attributes for an Apple services settings updated audit event.
- [object AuditEventBatchPasswordResetInitiated](./auditeventbatchpasswordresetinitiated.md)
  The data structure that represents the event data for a batch password reset initiated audit event.
- [object AuditEventBatchPasswordResetInitiatedAttributes](./auditeventbatchpasswordresetinitiatedattributes.md)
  The attributes for a batch password reset initiated audit event.
- [object AuditEventCollectionCreated](./auditeventcollectioncreated.md)
  The data structure that represents the event data for a collection created audit event.
- [object AuditEventCollectionCreatedAttributes](./auditeventcollectioncreatedattributes.md)
  The attributes for a collection created audit event.
- [object AuditEventCollectionDeleted](./auditeventcollectiondeleted.md)
  The data structure that represents the event data for a collection deleted audit event.
- [object AuditEventCollectionDeletedAttributes](./auditeventcollectiondeletedattributes.md)
  The attributes for a collection deleted audit event.
- [object AuditEventCollectionUpdated](./auditeventcollectionupdated.md)
  The data structure that represents the event data for a collection updated audit event.
- [object AuditEventCollectionUpdatedAttributes](./auditeventcollectionupdatedattributes.md)
  The attributes for a collection updated audit event.
- [object AuditEventCommonAttributes](./auditeventcommonattributes.md)
  The common attributes for all audit events.
- [object AuditEventConfigSettingsCreated](./auditeventconfigsettingscreated.md)
  The data structure that represents the event data for a config settings created audit event.
- [object AuditEventConfigSettingsCreatedAttributes](./auditeventconfigsettingscreatedattributes.md)
  The attributes for a configuration settings created audit event.
- [object AuditEventConfigSettingsDeleted](./auditeventconfigsettingsdeleted.md)
  The data structure that represents the event data for a config settings deleted audit event.
- [object AuditEventConfigSettingsDeletedAttributes](./auditeventconfigsettingsdeletedattributes.md)
  The attributes for a configuration settings deleted audit event.
- [object AuditEventConfigSettingsUpdated](./auditeventconfigsettingsupdated.md)
  The data structure that represents the event data for a config settings updated audit event.
- [object AuditEventConfigSettingsUpdatedAttributes](./auditeventconfigsettingsupdatedattributes.md)
  The attributes for a configuration settings updated audit event.
- [object AuditEventDeviceAddedToOrg](./auditeventdeviceaddedtoorg.md)
  The data structure that represents the event data for a device added to organization audit event.
- [object AuditEventDeviceAddedToOrgAttributes](./auditeventdeviceaddedtoorgattributes.md)
  The attributes for a device added to organization audit event.
- [object AuditEventDeviceAssignedToServer](./auditeventdeviceassignedtoserver.md)
  The data structure that represents the event data for a device assigned to server audit event.
- [object AuditEventDeviceAssignedToServerAttributes](./auditeventdeviceassignedtoserverattributes.md)
  The attributes for a device assigned to server audit event.
- [object AuditEventDeviceIsErased](./auditeventdeviceiserased.md)
  The data structure that represents the event data for a device is erased audit event.
- [object AuditEventDeviceIsErasedAttributes](./auditeventdeviceiserasedattributes.md)
  The attributes for a device is erased audit event.
- [object AuditEventDeviceRemovedFromOrg](./auditeventdeviceremovedfromorg.md)
  The data structure that represents the event data for a device removed from organization audit event.
- [object AuditEventDeviceRemovedFromOrgAttributes](./auditeventdeviceremovedfromorgattributes.md)
  The attributes for a device removed from organization audit event.
- [object AuditEventDeviceUnassignedFromServer](./auditeventdeviceunassignedfromserver.md)
  The data structure that represents the event data for a device unassigned from server audit event.
- [object AuditEventDeviceUnassignedFromServerAttributes](./auditeventdeviceunassignedfromserverattributes.md)
  The attributes for a device unassigned from server audit event.
- [object AuditEventDomainAdded](./auditeventdomainadded.md)
  The data structure that represents the event data for a domain added audit event.
- [object AuditEventDomainAddedAttributes](./auditeventdomainaddedattributes.md)
  The attributes for a domain added audit event.
- [object AuditEventDomainFederationDisabled](./auditeventdomainfederationdisabled.md)
  The data structure that represents the event data for a domain federation disabled audit event.
- [object AuditEventDomainFederationDisabledAttributes](./auditeventdomainfederationdisabledattributes.md)
  The attributes for a domain federation disabled audit event.
- [object AuditEventDomainFederationEnabled](./auditeventdomainfederationenabled.md)
  The data structure that represents the event data for a domain federation enabled audit event.
- [object AuditEventDomainFederationEnabledAttributes](./auditeventdomainfederationenabledattributes.md)
  The attributes for a domain federation enabled audit event.
- [object AuditEventDomainRemoved](./auditeventdomainremoved.md)
  The data structure that represents the event data for a domain removed audit event.
- [object AuditEventDomainRemovedAttributes](./auditeventdomainremovedattributes.md)
  The attributes for a domain removed audit event.
- [object AuditEventDomainVerified](./auditeventdomainverified.md)
  The data structure that represents the event data for a domain verified audit event.
- [object AuditEventDomainVerifiedAttributes](./auditeventdomainverifiedattributes.md)
  The attributes for a domain verified audit event.
- [object AuditEventExternalAccountAssociated](./auditeventexternalaccountassociated.md)
  The data structure that represents the event data for an external account associated audit event.
- [object AuditEventExternalAccountAssociatedAttributes](./auditeventexternalaccountassociatedattributes.md)
  The attributes for an external account associated audit event.
- [object AuditEventExternalAccountDisassociated](./auditeventexternalaccountdisassociated.md)
  The data structure that represents the event data for an external account disassociated audit event.
- [object AuditEventExternalAccountDisassociatedAttributes](./auditeventexternalaccountdisassociatedattributes.md)
  The attributes for an external account disassociated audit event.
- [object AuditEventExternalAccountInvited](./auditeventexternalaccountinvited.md)
  The data structure that represents the event data for an external account invited audit event.
- [object AuditEventExternalAccountInvitedAttributes](./auditeventexternalaccountinvitedattributes.md)
  The attributes for an external account invited audit event.
- [object AuditEventIdpAccountSyncDisabled](./auditeventidpaccountsyncdisabled.md)
  The data structure that represents the event data for an identity provider account sync disabled audit event.
- [object AuditEventIdpAccountSyncDisabledAttributes](./auditeventidpaccountsyncdisabledattributes.md)
  The attributes for an identity provider account sync disabled audit event.
- [object AuditEventIdpAccountSyncEnabled](./auditeventidpaccountsyncenabled.md)
  The data structure that represents the event data for an identity provider account sync enabled audit event.
- [object AuditEventIdpAccountSyncEnabledAttributes](./auditeventidpaccountsyncenabledattributes.md)
  The attributes for an identity provider account sync enabled audit event.
- [object AuditEventIdpCreated](./auditeventidpcreated.md)
  The data structure that represents the event data for an identity provider created audit event.
- [object AuditEventIdpCreatedAttributes](./auditeventidpcreatedattributes.md)
  The attributes for an identity provider created audit event.
- [object AuditEventIdpDeleted](./auditeventidpdeleted.md)
  The data structure that represents the event data for an identity provider deleted audit event.
- [object AuditEventIdpDeletedAttributes](./auditeventidpdeletedattributes.md)
  The attributes for an identity provider deleted audit event.
- [object AuditEventIdpUpdated](./auditeventidpupdated.md)
  The data structure that represents the event data for an identity provider updated audit event.
- [object AuditEventIdpUpdatedAttributes](./auditeventidpupdatedattributes.md)
  The attributes for an identity provider updated audit event.
- [object AuditEventRoleCreated](./auditeventrolecreated.md)
  The data structure that represents the event data for a role created audit event.
- [object AuditEventRoleCreatedAttributes](./auditeventrolecreatedattributes.md)
  The attributes for a role created audit event.
- [object AuditEventRoleUpdated](./auditeventroleupdated.md)
  The data structure that represents the event data for a role updated audit event.
- [object AuditEventRoleUpdatedAttributes](./auditeventroleupdatedattributes.md)
  The attributes for a role updated audit event.
- [object AuditEventSubjectHasAppleCarePurchaseAdded](./auditeventsubjecthasapplecarepurchaseadded.md)
  The data structure that represents the event data for a subject has AppleCare purchase added audit event.
- [object AuditEventSubjectHasAppleCarePurchaseRemoved](./auditeventsubjecthasapplecarepurchaseremoved.md)
  The data structure that represents the event data for a subject has AppleCare purchase removed audit event.
- [object AuditEventSubjectHasApplecarePurchaseAddedAttributes](./auditeventsubjecthasapplecarepurchaseaddedattributes.md)
  The attributes for a subject has AppleCare purchase added audit event.
- [object AuditEventSubjectHasApplecarePurchaseRemovedAttributes](./auditeventsubjecthasapplecarepurchaseremovedattributes.md)
  The attributes for a subject has AppleCare purchase removed audit event.
- [object AuditEventSubjectHasICloudStoragePurchaseAdded](./auditeventsubjecthasicloudstoragepurchaseadded.md)
  The data structure that represents the event data for a subject has iCloud storage purchase added audit event.
- [object AuditEventSubjectHasICloudStoragePurchaseRemoved](./auditeventsubjecthasicloudstoragepurchaseremoved.md)
  The data structure that represents the event data for a subject has iCloud storage purchase removed audit event.
- [object AuditEventSubjectHasIcloudStoragePurchaseAddedAttributes](./auditeventsubjecthasicloudstoragepurchaseaddedattributes.md)
  The attributes for a subject has iCloud storage purchase added audit event.
- [object AuditEventSubjectHasIcloudStoragePurchaseRemovedAttributes](./auditeventsubjecthasicloudstoragepurchaseremovedattributes.md)
  The attributes for a subject has iCloud storage purchase removed audit event.
- [object AuditEventSubscriptionCreated](./auditeventsubscriptioncreated.md)
  The data structure that represents the event data for a subscription created audit event.
- [object AuditEventSubscriptionCreatedAttributes](./auditeventsubscriptioncreatedattributes.md)
  The attributes for a subscription created audit event.
- [object AuditEventSubscriptionDeleted](./auditeventsubscriptiondeleted.md)
  The data structure that represents the event data for a subscription deleted audit event.
- [object AuditEventSubscriptionDeletedAttributes](./auditeventsubscriptiondeletedattributes.md)
  The attributes for a subscription deleted audit event.
- [object AuditEventSubscriptionUpdated](./auditeventsubscriptionupdated.md)
  The data structure that represents the event data for a subscription updated audit event.
- [object AuditEventSubscriptionUpdatedAttributes](./auditeventsubscriptionupdatedattributes.md)
  The attributes for a subscription updated audit event.
- [object AuditEventTermsAccepted](./auditeventtermsaccepted.md)
  The data structure that represents the event data for a terms accepted audit event.
- [object AuditEventTermsAcceptedAttributes](./auditeventtermsacceptedattributes.md)
  The attributes for a terms accepted audit event.
- [object MdmServerCreateRequest](./mdmservercreaterequest.md)
  A request to create a new device management service.
- [object MdmServerUpdateRequest](./mdmserverupdaterequest.md)
  A request to update an existing device management service.

## See Also

### Apple School Manager and Apple Business APIs
- [Apple School Manager API](../AppleSchoolManagerAPI/AppleSchoolManagerAPI.md)
  Automate device management activities and view device information in Apple School Manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi)*