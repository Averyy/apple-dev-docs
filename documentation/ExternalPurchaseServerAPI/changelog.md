# External Purchase Server API changelog

**Framework**: External Purchase Server API  
**Role**: Article

Learn about new features and updates in the External Purchase Server API.

## Overview

Use this changelog to learn about feature updates, deprecations, and removals for the External Purchase Server API.

## 1.2.0 — 2025/06/26

**New features**

- Added support for new custom link token types, `ACQUISITION` and `SERVICES`.
- Added DUPLICATE_TOKEN possible value in [`status`](./status.md) and [`ExternalPurchaseReport`](./externalpurchasereport.md) objects.
- Added errors [`LineItemCreationDateOutOfRangeError`](./lineitemcreationdateoutofrangeerror.md) and [`DuplicateTokenStatusNotAllowedError`](./duplicatetokenstatusnotallowederror.md).

## 1.1.0 — 2025/04/14

**New features**

- Added errors [`RestatementCreationDateMismatchError`](./restatementcreationdatemismatcherror.md), [`RestatementNotAllowedCreationDateError`](./restatementnotallowedcreationdateerror.md), and [`RefundNotAllowedCreationDateError`](./refundnotallowedcreationdateerror.md).

## Server update — 2024/03/05

Initial release.

## 1.0.0 — 2024/02/29

Initial beta release with functionality enabled for sandbox testing.

## 0.1.0 — 2024/01/25

Initial beta release for preview.

## See Also

### Essentials
- [Creating API keys to authorize API requests](../AppStoreServerAPI/creating-api-keys-to-authorize-api-requests.md)
  Create API keys you use to sign JSON Web Tokens and authorize API requests.
- [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)
  Create JSON Web Tokens signed with your private key to authorize requests for App Store Server API and External Purchase Server API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/changelog)*