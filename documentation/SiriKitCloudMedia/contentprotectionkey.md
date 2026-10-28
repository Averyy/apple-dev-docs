# Retrieve an Asset’s Content Protection Key

**Framework**: SiriKit Cloud Media  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Provide the content key for a specific protected asset.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Discussion

If your service implements content protection, the client requests an item’s content protection key from this endpoint after each of the following events:

- The client receives the queue’s initial item.
- The client preloads each subsequent item in the queue.
- The user manually transitions to an item in the queue.

For more information on providing your service’s content protection configuration, see [`ExtensionConfig.Media.Queues.ContentProtectionKey`](./extensionconfig/media-data.dictionary/queues-data.dictionary/contentprotectionkey-data.dictionary.md).

## Endpoint

`POST https://cloudextension-testservice.local/api/queues/contentProtectionKey`

## Parameters

### Header Parameters

- `Accept-Language` (string): The client’s current user interface language. If possible, respond with localized content for this language.
- `User-Agent` (string) *(required)*: The client’s extension protocol. This is an RFC 7231-compliant string that contains the product name `AppleCloudExtension` and the version of the SiriKit extension library that’s running on the client.

  **Maximum Length**: `250`; **Allowed Values**: `/AppleCloudExtension/([0-9]+\.[0-9]+\.[0-9]+) *.*/`
- `x-applecloudextension-retry-count` (uint32): The number of previous requests from the client. The client omits this header on the first attempt.

  **Minimum**: `1`
- `x-applecloudextension-session-id` (string) *(required)*: A session identifier to pair each request and response. Respond to requests with the value the client provides.

  **Minimum Length**: `1`; **Maximum Length**: `128`

## Request Body

**Content-Type**: `application/json`  
**Type**: `ContentProtectionKeyRequest`

A JSON object that contains the encrypted key request and identifies the protected asset.

## Responses

- `200` OK (`ContentProtectionKeyResponse`, `application/json`): The request is successful.
- `204` No Content: The service is unable to provide a content key for the specified `assetIdentifier`.
- `401` Unauthorized: The request requires authorization. The client can attempt to reauthorize and then retry the request.
- `410` Gone: The request includes an expired [`UserActivity`](./useractivity.md), which the service is unable to use to provide a content key.

## See Also

### Content Protection
- [object ContentProtectionKeyRequest](./contentprotectionkeyrequest.md)
  A request for an item’s content protection key.
- [object ContentProtectionKeyResponse](./contentprotectionkeyresponse.md)
  A response to a request for an item’s content protection key.
- [type ContentProtectionKeySystem](./contentprotectionkeysystem.md)
  The content protection key systems that SiriKit Cloud Media supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/contentprotectionkey)*