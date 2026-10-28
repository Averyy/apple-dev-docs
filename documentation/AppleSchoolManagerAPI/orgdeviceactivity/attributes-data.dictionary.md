# OrgDeviceActivity.Attributes

**Framework**: AppleSchoolManagerAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an organization device activity resource.

**Availability**:
- Apple School Manager API 1.7+

## Declaration

```
object OrgDeviceActivity.Attributes
```

## Overview

> **Note**: You can add new attributes to a resource without a newer version of an API.

#### Status

| **Possible values** | **Description** |
| --- | --- |
| `COMPLETED` | Indicates when an activity completes processing. |
| `IN_PROGRESS` | Indicates that an activity is still in progress. |
| `STOPPED` | Indicates that an activity is stopped. |
| `FAILED` | Indicates when an activity fails processing. For more details, check the downloadable activity logs. |

#### Substatus

| **Possible values** | **Description** |
| --- | --- |
| `SUBMITTED` | Indicates that a newly created activity is awaiting processing. |
| `PRE_PROCESSING` | Indicates that an activity is in a preprocessing state. |
| `PENDING` | Indicates that an activity is in a pending state. |
| `PROCESSING` | Indicates that an activity is processing. |
| `POST_PROCESSING` | Indicates that an activity is in the postprocessing state of generating a downloadable CSV file. |
| `STOPPING` | Indicates that an activity is stopping. |
| `COMPLETED_WITH_SUCCESS` | Indicates when an activity successfully processes all items. |
| `COMPLETED_WITH_ERROR` | Indicates when an activity encounters an error during processing. |
| `COMPLETED_WITH_FAILURE` | Indicates a partial failure of an activity. For more details, check the downloadable activity logs. |
| `COMPLETED_POST_PROCESSING_FAILED` | Indicates when an activity fails in postprocessing. For more details, check the downloadable activity logs. |

## Properties

- `createdDateTime` (date-time): The date and time of the creation of organization device activity.
- `status` (string): The top-level status of an activity. For more details, see the table below. Possible values: `COMPLETED`,  `IN_PROGRESS`, `STOPPED`, `FAILED`
- `subStatus` (string): The low-level status of an activity. For more details, see the table below. Possible values: `SUBMITTED`,`PRE_PROCESSING`,`PENDING`,`PROCESSING`,`POST_PROCESSING`,              `STOPPING`,`COMPLETED_WITH_SUCCESS`,`COMPLETED_WITH_ERROR`,`COMPLETED_WITH_FAILURE`,`COMPLETED_POST_PROCESSING_FAILED`
- `completedDateTime` (date-time): **(Optional)** The date and time of the completion of organization device activity. This is available only when an activity is in a `COMPLETED` status.
- `downloadUrl` (string): **(Optional)** A presigned URL for downloading activity logs in a CSV format. This is available only when an activity is in a `COMPLETED` status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appleschoolmanagerapi/orgdeviceactivity/attributes-data.dictionary)*