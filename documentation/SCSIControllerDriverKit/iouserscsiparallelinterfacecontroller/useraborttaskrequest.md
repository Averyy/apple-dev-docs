# UserAbortTaskRequest

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Aborts a single task.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserAbortTaskRequest(uint64_t theT, uint64_t theL, uint64_t theQ, uint32_t *response);
```

## Discussion

This method doesn’t clear previously established conditions, such as `MODE SELECT` parameters, reservations, and autocontingent allegiance (ACA) attributes.

## Parameters

- `theT`: The target containing the task to abort.
- `theL`: The logical unit containing the task to abort.
- `theQ`: The tag of the task to abort.
- `response`: On return, a SCSI protocol-specific value indicating the success or failure of the request.

## See Also

### Performing SCSI standard task management
- [UserAbortTaskSetRequest](./useraborttasksetrequest.md)
  Aborts all tasks in a logical unit.
- [UserClearACARequest](./userclearacarequest.md)
  Removes an autocontingent allegiance (ACA) attribute from a logical unit’s task set.
- [UserClearTaskSetRequest](./usercleartasksetrequest.md)
  Aborts all tasks in a logical unit and clears their data.
- [UserLogicalUnitResetRequest](./userlogicalunitresetrequest.md)
  Resets a logical unit.
- [UserTargetResetRequest](./usertargetresetrequest.md)
  Resets a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/useraborttaskrequest)*