# Setting Up Your Server

**Framework**: Apple Pay on the Web

Set up your server for secure communications with Apple Pay.

#### Overview

These are the requirements for incorporating Apple Pay on your website:

- You must serve all pages that include Apple Pay over HTTPS.
- Your domain must have a valid SSL certificate.
- Your server must support the Transport Layer Security (TLS) protocol version 1.2 or later, and one of the cipher suites listed here:

| Cipher suite value | Name |
| --- | --- |
| 0x13, 0x01 | TLS_AES_128_GCM_SHA256 |
| 0x13, 0x02 | TLS_AES_256_GCM_SHA384 |
| 0xC0,0x2B | ECDHE-ECDSA-AES128-GCM-SHA256 |
| 0xC0,0x2F | ECDHE-RSA-AES128-GCM-SHA256 |
| 0xC0,0x2C | ECDHE-ECDSA-AES256-GCM-SHA384 |
| 0xC0,0x30 | ECDHE-RSA-AES256-GCM-SHA384 |

##### Allow Apple Pay Ip Addresses

To successfully connect with Apple Pay IP addresses and domains, your server needs to allow access over HTTPS (TCP over port 443)  and include the TLS Server Name Indication (SNI) extension. Apple Pay requires SNI on all connections. Your server needs to connect to the Apple Pay IP addresses and domains provided listed in [`Setting Up Your Server`](setting-up-your-server.md), below.

> ❗ **Important**:  Use a strict allow list for Apple IP addresses and domains provided in [`Setting Up Your Server`](setting-up-your-server.md). Do not allow your server to access any other IP addresses or domains.

Listing 1. Apple Pay IP addresses and domain names for production.

```other
Domain
apple-pay-gateway.apple.com (Global)

This name resolves to the IP addresses / CIDR block below:
17.171.78.7/32, 17.171.78.71/32, 17.171.78.135/32, 17.171.78.199/32, 17.171.79.12/32
17.141.128.7/32, 17.141.128.71/32, 17.141.128.135/32, 17.141.128.199/32, 17.141.129.12/32
17.32.214.7/32, 17.157.96.181/32
17.33.194.239/32, 17.33.192.38/32, 17.33.193.110/32
17.33.202.35/32, 17.33.201.101/32, 17.33.200.169/32


Domain
cn-apple-pay-gateway.apple.com (China Region)

This name resolves to the IP addresses / CIDR block below:
101.230.204.232/32, 101.230.204.242/32, 101.230.204.240/32
60.29.205.104/32, 60.29.205.106/32, 60.29.205.108/32
```

> ❗ **Important**:  Use the IP addresses, in [`Setting Up Your Server`](setting-up-your-server.md) for development and sandbox testing only. Do not allow your production apps or production servers to use these testing services in production.

Listing 2. Apple Pay IP addresses and domain names for testing (development sandbox).

```other
For sandbox testing only:
Domain
apple-pay-gateway-cert.apple.com (Global)

This name resolves to the IP addresses / CIDR block below:
17.171.85.7/32
17.179.124.181/32, 17.32.214.56/32
17.33.194.218/32, 17.33.192.145/32, 17.33.193.45/32
17.33.200.47/32, 17.33.202.99/32, 17.33.201.105/32

Domain
cn-apple-pay-gateway-cert.apple.com (China Region)

This name resolves to the IP addresses / CIDR block below:
101.230.204.235/32
```

For more information about merchant validation, see [`Providing Merchant Validation`](providing-merchant-validation.md).

##### Allow Apple Ip Addresses for Domain Verification

Apple uses the following IP addresses when you register or verify your merchant domain. If you protect your domain from public access and you wish to complete domain verification, you need to allow the following IP address ranges.

```other
17.32.139.128/27
17.32.139.160/27
17.140.126.0/27
17.140.126.32/27
17.179.144.128/27
17.179.144.160/27
17.179.144.192/27
17.179.144.224/27
17.253.0.0/16
```

See [`Configuring Your Environment`](configuring-your-environment.md) for more information.

## See Also

- [Configuring Your Environment](configuring-your-environment.md)
  Create your Apple Pay merchant ID and certificates, and verify your domain.
- [Maintaining Your Environment](maintaining-your-environment.md)
  Prevent interruptions in your Apple Pay service by keeping certificates and domain verification current.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/setting-up-your-server)*