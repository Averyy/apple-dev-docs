# SCSIServiceResponse

**Framework**: DriverKit  
**Kind**: enum

Attributes for task service response.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef enum SCSIServiceResponse : unsigned int { ... } SCSIServiceResponse;
```

#### Overview

The Service Response represents the execution status of a service request made to a Protocol Services Driver. The Service Response can only be modified by the SCSI Protocol Layer. The SCSI Application Layer can only read the state.

## Topics

### Constants
- [kSCSIServiceResponse_Request_In_Process](scsiserviceresponse/kscsiserviceresponse_request_in_process.md)
- [kSCSIServiceResponse_SERVICE_DELIVERY_OR_TARGET_FAILURE](scsiserviceresponse/kscsiserviceresponse_service_delivery_or_target_failure.md)
- [kSCSIServiceResponse_TASK_COMPLETE](scsiserviceresponse/kscsiserviceresponse_task_complete.md)
- [kSCSIServiceResponse_LINK_COMMAND_COMPLETE](scsiserviceresponse/kscsiserviceresponse_link_command_complete.md)
- [kSCSIServiceResponse_FUNCTION_COMPLETE](scsiserviceresponse/kscsiserviceresponse_function_complete.md)
- [kSCSIServiceResponse_FUNCTION_REJECTED](scsiserviceresponse/kscsiserviceresponse_function_rejected.md)

## See Also

- [IOLockAssertState](iolockassertstate.md)
- [IORWLockAssertState](iorwlockassertstate.md)
- [kC0DataMaxStringLen](kc0datamaxstringlen.md)
- [kINQUIRY_ANSI_VERSION_Mask](kinquiry_ansi_version_mask.md)
- [kINQUIRY_ANSI_VERSION_NoClaimedConformance](kinquiry_ansi_version_noclaimedconformance.md)
- [kINQUIRY_ANSI_VERSION_SCSI_1_Compliant](kinquiry_ansi_version_scsi_1_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_2_Compliant](kinquiry_ansi_version_scsi_2_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_SPC_2_Compliant](kinquiry_ansi_version_scsi_spc_2_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_SPC_3_Compliant](kinquiry_ansi_version_scsi_spc_3_compliant.md)
- [kINQUIRY_ANSI_VERSION_SCSI_SPC_Compliant](kinquiry_ansi_version_scsi_spc_compliant.md)
- [kINQUIRY_Byte3_AERC_Bit](kinquiry_byte3_aerc_bit.md)
- [kINQUIRY_Byte3_AERC_Mask](kinquiry_byte3_aerc_mask.md)
- [kINQUIRY_Byte3_HISUP_Bit](kinquiry_byte3_hisup_bit.md)
- [kINQUIRY_Byte3_HISUP_Mask](kinquiry_byte3_hisup_mask.md)
- [kINQUIRY_Byte3_NORMACA_Bit](kinquiry_byte3_normaca_bit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/scsiserviceresponse)*