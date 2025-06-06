# UserLogicalUnitResetRequest

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Resets a logical unit.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t UserLogicalUnitResetRequest(uint64_t theT, uint64_t theL, uint32_t * response);
```

#### Discussion

The definition of the reset event that this request performs depends on the SCSI protocol.

## Parameters

- `theT`: The target containing the logical unit to reset.
- `theL`: The logical unit to reset.
- `response`: On return, a SCSI protocol-specific value indicating the success or failure of the request.

## See Also

- [UserAbortTaskRequest](iouserscsiparallelinterfacecontroller/useraborttaskrequest.md)
  Aborts a single task.
- [UserAbortTaskSetRequest](iouserscsiparallelinterfacecontroller/useraborttasksetrequest.md)
  Aborts all tasks in a logical unit.
- [UserClearACARequest](iouserscsiparallelinterfacecontroller/userclearacarequest.md)
  Removes an autocontingent allegiance (ACA) attribute from a logical unit’s task set.
- [UserClearTaskSetRequest](iouserscsiparallelinterfacecontroller/usercleartasksetrequest.md)
  Aborts all tasks in a logical unit and clears their data.
- [UserTargetResetRequest](iouserscsiparallelinterfacecontroller/usertargetresetrequest.md)
  Resets a target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/userlogicalunitresetrequest)*