# UserClearTaskSetRequest

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Aborts all tasks in a logical unit and clears their data.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserClearTaskSetRequest(uint64_t theT, uint64_t theL, uint32_t * response);
```

#### Discussion

This method clears all pending and status data, but not previously established conditions, such as `MODE SELECT` parameters, reservations, and autocontingent allegiance (ACA) attributes.

## Parameters

- `theT`: The target containing the tasks to clear.
- `theL`: The logical unit containing the tasks to clear.
- `response`: On return, a SCSI protocol-specific value indicating the success or failure of the request.

## See Also

- [UserAbortTaskRequest](iouserscsiparallelinterfacecontroller/useraborttaskrequest.md)
  Aborts a single task.
- [UserAbortTaskSetRequest](iouserscsiparallelinterfacecontroller/useraborttasksetrequest.md)
  Aborts all tasks in a logical unit.
- [UserClearACARequest](iouserscsiparallelinterfacecontroller/userclearacarequest.md)
  Removes an autocontingent allegiance (ACA) attribute from a logical unit’s task set.
- [UserLogicalUnitResetRequest](iouserscsiparallelinterfacecontroller/userlogicalunitresetrequest.md)
  Resets a logical unit.
- [UserTargetResetRequest](iouserscsiparallelinterfacecontroller/usertargetresetrequest.md)
  Resets a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usercleartasksetrequest)*