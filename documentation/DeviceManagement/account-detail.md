# Get Account Detail

**Framework**: Device Management  
**Kind**: httpRequest

Obtain the details for your account.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Each Mobile Device Management server must be registered with Apple. This endpoint provides details about the server entity to identify it uniquely throughout your organization. Each server is identifiable by either its system-generated unique identifier or by a user-provided name assigned by one of the organization’s users. Both the identifier and server name must be unique within your organization.

## Topics

### Response
- [object AccountDetail](accountdetail.md)
  The response that contains the details for an account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/account-detail)*