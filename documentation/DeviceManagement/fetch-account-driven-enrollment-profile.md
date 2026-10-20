# Fetch Account-Driven Enrollment Service Discovery

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch the Account-Driven Enrollment profile that the MDM server sets, which includes information about service discovery for account-driven enrollment.

**Availability**:
- Device Assignment Services 5.1+

## Topics

### Supporting responses
- [object GetAccountDrivenEnrollmentProfileResponse](./getaccountdrivenenrollmentprofileresponse.md)
  The details for an account-driven enrollment profile.

## Endpoint

`GET https://mdmenrollment.apple.com/account-driven-enrollment/profile`

## Responses

- `200` OK (`GetAccountDrivenEnrollmentProfileResponse`, `application/json`)
- `400` Bad Request:

  - `ORG_NOT_SUPPORTED`: Indicates that the associated organization isn’t supported.
- `404` Not Found:

  - `NOT_FOUND`: Indicates that the system can’t find the MDM Service Discovery URL.

## See Also

### Account-driven enrollment service discovery
- [Assign Account-Driven Enrollment Service Discovery](./assign-account-driven-enrollment-profile.md)
  The Account-Driven Enrollment profile defines key attributes related to service discovery for account-driven enrollment by MDM.
- [Remove Account-Driven Enrollment Profile](./remove-account-driven-enrollment-profile.md)
  Remove the Account-Driven Enrollment profile that the MDM server sets, which includes information about service discovery for account-driven enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-account-driven-enrollment-profile)*