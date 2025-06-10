# Assign Account-Driven Enrollment Service Discovery

**Framework**: Device Management  
**Kind**: httpRequest

The Account-Driven Enrollment profile defines key attributes related to service discovery for account-driven enrollment by MDM.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Implementing the simple authentication account-driven enrollment flow](implementing-the-simple-authentication-user-enrollment-flow.md)

#### Overview

This profile includes the MDM Service Discovery URL, which redirects users to the MDM server to start the enrollment process during account-driven enrollment.

## Topics

### Supporting requests
- [object AccountDrivenEnrollmentProfileRequest](accountdrivenenrollmentprofilerequest.md)
  The details for an account-driven enrollment profile.

## Request Body

The profile request for this account-driven enrollment.

## See Also

- [Fetch Account-Driven Enrollment Service Discovery](fetch-account-driven-enrollment-profile.md)
  Fetch the Account-Driven Enrollment profile that the MDM server sets, which includes information about service discovery for account-driven enrollment.
- [Remove Account-Driven Enrollment Profile](remove-account-driven-enrollment-profile.md)
  Remove the Account-Driven Enrollment profile that the MDM server sets, which includes information about service discovery for account-driven enrollment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assign-account-driven-enrollment-profile)*