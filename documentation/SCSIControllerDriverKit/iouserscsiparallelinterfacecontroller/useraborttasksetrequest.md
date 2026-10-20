# UserAbortTaskSetRequest

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Aborts all tasks in a logical unit.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserAbortTaskSetRequest(uint64_t theT, uint64_t theL, uint32_t *response);
```

#### Discussion

This method doesn’t clear previously established conditions, such as `MODE SELECT` parameters, reservations, and autocontingent allegiance (ACA) attributes.

## Parameters

- `theT`: The target containing the tasks to abort.
- `theL`: The logical unit containing the tasks to abort.
- `response`: On return, a SCSI protocol-specific value indicating the success or failure of the request.

## See Also

### Performing SCSI standard task management
- [UserAbortTaskRequest](./useraborttaskrequest.md)
  Aborts a single task.
- [UserClearACARequest](./userclearacarequest.md)
  Removes an autocontingent allegiance (ACA) attribute from a logical unit’s task set.
- [UserClearTaskSetRequest](./usercleartasksetrequest.md)
  Aborts all tasks in a logical unit and clears their data.
- [UserLogicalUnitResetRequest](./userlogicalunitresetrequest.md)
  Resets a logical unit.
- [UserTargetResetRequest](./usertargetresetrequest.md)
  Resets a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/useraborttasksetrequest)*