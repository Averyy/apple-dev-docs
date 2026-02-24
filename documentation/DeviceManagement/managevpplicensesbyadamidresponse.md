# ManageVppLicensesByAdamIdResponse

**Framework**: Device Management  
**Kind**: dictionary

The response from managing licenses.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManageVppLicensesByAdamIdResponse
```

## Properties

- `adamIdStr` (string): The unique identifier for a product in the iTunes Store.
- `associations` ([VppAssociation]): An array of dictionaries representing successful and failed associations. If an association succeeds, its dictionary contains the license and either a client-user ID or the serial number of the device associated with the license. If an association fails, its dictionary contains the error message and number, and either the client-user ID or the serial number of the device that couldn’t be associated with the license.
- `clientContext` (string): The value currently associated with the provided sToken. This field is only included in the response when a value has been set via the [`Client Configuration`](client-configuration.md) endpoint. See [`Protecting Your VPP Account`](protecting-your-vpp-account.md) for more information.
- `disassociations` ([VppAssociation]): An array of dictionaries representing successful and failed disassociations. If a disassociation succeeds, its dictionary contains a license and either a client-user ID or the serial number of the device disassociated. The license may not be the license ID that was just disassociated; rather the license ID is any currently available license at the time of disassociation. If the disassociation fails, its dictionary contains the error message and number, and either the client-user ID or the serial number of the device that couldn’t be disassociated from the license.
- `errorMessage` (string): The human-readable explanation of the error.
- `errorNumber` (int32): The numeric code of the error.
- `expirationMillis` (int64): The UNIX epoch timestamp, in milliseconds, when the account’s sToken or password expires (whichever is earlier).
- `isIrrevocable` (boolean): If `true`, licenses for the specified product can’t be revoked and reassigned.
- `location` (VppLocation): The location associated with the provided sToken. This field is only returned when a location token is used with an Apple School Manager account.
- `pricingParam` (string): The quality of a product in the iTunes Store. Possible values are: STDQ: Standard quality PLUS: High quality
- `productTypeId` (int32): The type of a product. Possible values are: 7 = macOS software 8 = iOS or macOS app from the App Store 10 = Book
- `productTypeName` (string): The name of the product type.
- `status` (int32): The status code for the response. Possible values are: `0` = Success. All requested associations and disassociations have succeeded. -1 = Failure. All requested associations and disassociations have failed. An errorNumber, errorCode, and errorMessage is returned for each failed association and disassociation. See [`VppAssociation`](vppassociation.md) and  [`Interpreting Error Codes`](interpreting-error-codes.md) for more information. `-3` = The licenses can’t be changed as requested. Some of the requested associations and disassociations have succeeded and others have failed. An errorNumber, errorCode, and errorMessage is returned for each failed association and disassociation. See [`VppAssociation`](vppassociation.md) and [`Interpreting Error Codes`](interpreting-error-codes.md) for more information.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates. In this way, you can avoid double-counting records when duplicate tokens are uploaded by different content managers.

## See Also

- [object ManageVppLicensesByAdamIdRequest](managevpplicensesbyadamidrequest.md)
  The request to manage licenses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managevpplicensesbyadamidresponse)*