# OrgDeviceActivityCreateRequest.Data

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- Apple Business API 2.7+

## Declaration

```
object OrgDeviceActivityCreateRequest.Data
```

## Topics

### Dictionaries
- [object OrgDeviceActivityCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes with values that you’re changing as part of the create request.
- [object OrgDeviceActivityCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request, and those that you can operate on.

## Properties

- `attributes` (OrgDeviceActivityCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (OrgDeviceActivityCreateRequest.Data.Relationships) *(required)*: The types and IDs of the related data to update.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `orgDeviceActivities`


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/orgdeviceactivitycreaterequest/data-data.dictionary)*