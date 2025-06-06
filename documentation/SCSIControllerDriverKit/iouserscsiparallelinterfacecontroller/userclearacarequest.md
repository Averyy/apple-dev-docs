# UserClearACARequest

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Removes an autocontingent allegiance (ACA) attribute from a logical unit’s task set.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserClearACARequest(uint64_t theT, uint64_t theL, uint32_t * response);
```

## Parameters

- `theT`: The target containing the tasks to clear ACA attributes from.
- `theL`: The logical unit containing the tasks to clear ACA attributes from.
- `response`: On return, a SCSI protocol-specific value indicating the success or failure of the request.

## See Also

- [UserAbortTaskRequest](iouserscsiparallelinterfacecontroller/useraborttaskrequest.md)
  Aborts a single task.
- [UserAbortTaskSetRequest](iouserscsiparallelinterfacecontroller/useraborttasksetrequest.md)
  Aborts all tasks in a logical unit.
- [UserClearTaskSetRequest](iouserscsiparallelinterfacecontroller/usercleartasksetrequest.md)
  Aborts all tasks in a logical unit and clears their data.
- [UserLogicalUnitResetRequest](iouserscsiparallelinterfacecontroller/userlogicalunitresetrequest.md)
  Resets a logical unit.
- [UserTargetResetRequest](iouserscsiparallelinterfacecontroller/usertargetresetrequest.md)
  Resets a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userclearacarequest)*