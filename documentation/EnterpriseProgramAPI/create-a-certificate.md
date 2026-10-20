# Create a Certificate

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a new certificate using a certificate signing request.

#### Overview

- HTTPBody

## Endpoint

`POST https://api.enterprise.developer.apple.com/v1/certificates`

## Request Body

**Content-Type**: `application/json`  
**Type**: `CertificateCreateRequest`

## Responses

- `201` Created (`CertificateResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/create-a-certificate)*