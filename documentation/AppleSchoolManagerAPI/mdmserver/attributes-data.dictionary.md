# MdmServer.Attributes

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a device management service resource.

**Availability**:
- Apple School Manager API 1.8+

## Declaration

```
object MdmServer.Attributes
```

## Overview

> **Note**: You can add new attributes to a resource without a newer version of an API.

## Properties

- `createdDateTime` (date-time): The date and time of the creation of the resource.
- `defaultProductFamilies` ([MdmServerProductFamily]): The product families that are assigned by default to this device management service. Read only.
- `deviceCount` (integer): The number of devices currently assigned to this device management service. Read only.
- `enableMdmDisownFlag` (boolean): A Boolean value that indicates whether the device management service is allowed to disown its enrolled devices. Read only.
- `lastConnectedDateTime` (date-time): The date and time the device management service last connected to Apple’s servers. Read only.
- `lastConnectedIp` (string): The IP address from which the device management service last connected to Apple’s servers. Read only.
- `serverName` (string): The device management service’s name.
- `serverType` (string): The type of device management service: `MDM`, `APPLE_CONFIGURATOR`, `APPLE_MDM`. Read only.
- `status` (MdmServerStatus): The operational status of the device management service. Read only. See [`MdmServerStatus`](../mdmserverstatus.md) for possible values.
- `updatedDateTime` (date-time): The date and time of the most-recent update for the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/mdmserver/attributes-data.dictionary)*