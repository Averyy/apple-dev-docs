# Apple School Manager API

**Framework**: AppleSchoolManagerAPI  
**Kind**: module  
**Role**: Web Service

Automate device management activities and view device information in Apple School Manager.

**Availability**:
- Apple School Manager API 1.7+

## Overview

> **Note**: This API is a part of the [Apple School Manager and Apple Business APIs](../apple-school-and-business-manager-api/apple-school-and-business-manager-api.md) collection.

## Topics

### Devices
- [Get Organization Devices](./get-org-devices.md)
  Get a list of devices in an organization that enroll using Automated Device Enrollment.
- [Get Device Information](./get-orgdevice-information.md)
  Get information about a device in an organization.
- [Get AppleCare Coverage Information for a Device](./get-all-applecare-coverage-for-an-orgdevice.md)
  Get a list of AppleCare coverage resources for an organization device.
### Device Management Services
- [Get Device Management Services](./get-device-management-services.md)
  Get a list of device management services in an organization.
- [Get Device Management Service Information](./get-mdmserver-information.md)
  Get the information for a specific device management service.
- [Get All Device IDs for a Device Management Service](./get-all-device-ids-for-a-device-management-service.md)
- [Get the Assigned Device Management Service ID for a Device](./get-the-assigned-device-management-service-id-for-an-orgdevice.md)
  Get the assigned device management service ID information for a device.
- [Get the Assigned Device Management Service Information for a Device](./get-the-assigned-device-management-service-information-for-an-orgdevice.md)
  Get the assigned device management service information for a device.
- [Assign or Unassign Devices to a Device Management Service](./create-an-orgdeviceactivity.md)
  Assign or unassign devices to a device management service, or manage a device management service for devices.
- [Get Organization Device Activity Information](./get-orgdeviceactivity-information.md)
  Get information for an organization device activity that a device management action, such as assigning or unassigning, creates.
### Objects and Data Types
- [object OrgDevice](./orgdevice.md)
  The data structure that represents an organization device resource.
- [object OrgDeviceResponse](./orgdeviceresponse.md)
  A response that contains a single organization device resource.
- [object OrgDevicesResponse](./orgdevicesresponse.md)
  A response that contains a list of organization device resources.
- [object OrgDeviceAssignedServerLinkageResponse](./orgdeviceassignedserverlinkageresponse.md)
  The data and links that describe the relationship between the resources.
- [object MdmServer](./mdmserver.md)
  The data structure that represents device management services in organizations.
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
- [type ActivationLockType](./activationlocktype.md)
  Strings that represent the type of Activation Lock on a device.
- [type MdmMigrationStatus](./mdmmigrationstatus.md)
  Strings that represent the state of a device’s device management service migration.
### Endpoints
- [Get the Activation Lock Status for a Device](./get-the-activation-lock-status-information-for-an-orgdevice.md)
  Get the Activation Lock status of an organization device.
### Dictionaries
- [object ActivationLockStatus](./activationlockstatus.md)
  The data structure that represents the Activation Lock status of an organization device.
- [object ActivityTypeMetadata](./activitytypemetadata.md)
  Additional metadata for an organization device activity, used by device management service migration activity types.

## See Also

### Apple School Manager and Apple Business APIs
- [Apple Business API](../AppleBusinessAPI/AppleBusinessAPI.md)
  Automate device management activities, view device information, and manage users and user groups in Apple Business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi)*