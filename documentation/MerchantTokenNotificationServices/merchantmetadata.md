# MerchantMetadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary  
**Role**: Object

The metadata of the merchant that updated on the server.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```
object MerchantMetadata
```

## Discussion

Apple Pay sends a notification with a unique event identifier to this URL for events that impact the associated MPAN.

## Properties

- `tokenNotificationURL` (string): The URL for the token notification.

  **Maximum Length**: `256`


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchantmetadata)*