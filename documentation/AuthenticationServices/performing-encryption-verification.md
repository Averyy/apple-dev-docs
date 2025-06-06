# Performing encryption verification

**Framework**: Authentication Services

Verify the login request and create a JSON Web Encryption (JWE) response.

#### Overview

Use the code snippets in this article to complete the process of encryption verification that works with platform SSO:

- Create device signing and encryption keys
- Sign the login request and encrypt the response
- Perform key exchange
- Derive a shared key and encrypt the plain text
- Verify the login response and decrypt the JWE

Use this device signing key:

```javascript
{
    "y" : "PAIz7YrH4Rxz1rlfn6JcnwSmFDVGY1ISlGnmK1NX5vs",
    "d" : "vXZoCHYVxEJVcCcQN50ZKEBwhlQYO6g3KaUIufh3vXw",
    "kid" : "Ws9mKynZxyUSNXYtMGAjjLO+Jg16HCa\/5pJO0udNWJ4=",
    "x" : "gK60EgxT-EipyAgSlrHG0LgFVrgnd8UXAvLOgykJtms",
    "kty" : "EC",
    "crv" : "P-256"
}
```

Use this device encryption key:

```javascript
{
    "y" : "4MlSuUf_7J6Ljv0FBT1jK0_sKGB4WYwdKCOtnTEAwz4",
    "d" : "1bqqmpoFEtzSnQMqp9N9ZRybnP8vjFUiZyGaSgKVGMw",
    "kid" : "pScnuzx3x85Eyp6CtK9UQADxOsAGTP72y02Tg3m1sk8=",
    "x" : "TvkPOH4yscrSC1rFYvnBVPYMqzR1vKck9ht4D7K_gAQ",
    "kty" : "EC",
    "crv" : "P-256"
}
```

##### Sign the Login Request

Note how the system signs the following login JSON Web Token (JWT) using the device-signing key:

```javascript
{
    "kid" : "Ws9mKynZxyUSNXYtMGAjjLO+Jg16HCa/5pJO0udNWJ4=",
    "x5c" : "MIIBhDCCASmgAwIBAgIBATAKBggqhkjOPQQDAjA3MRQwEgYDVQQDEwtkZXZpY2UgdGVzdDELMAkGA1UEBhMCVVMxEjAQBgNVBAoTCUFwcGxlIEluYzAeFw0yMjA2MjMxNzI1MzFaFw0yMzA2MjMxNzI1MzFaMDcxFDASBgNVBAMTC2RldmljZSB0ZXN0MQswCQYDVQQGEwJVUzESMBAGA1UEChMJQXBwbGUgSW5jMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEgK60EgxT+EipyAgSlrHG0LgFVrgnd8UXAvLOgykJtms8AjPtisfhHHPWuV+folyfBKYUNUZjUhKUaeYrU1fm+6MmMCQwEgYDVR0TAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCB4AwCgYIKoZIzj0EAwIDSQAwRgIhAMwGOYwgf5xGxNcZLL/Y4phA66w/PSVLeQYhec2JTQF1AiEAlNSUDycvv0DwDQYU4wUpco/GBuhc4mPmli3+DT+p1Is=",
    "typ" : "JWT",
    "alg" : "ES256"
}.{
    "iat" : "1656005132",
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAABUFwcGxlAAAAQQRO-Q84fjKxytILWsVi-cFU9gyrNHW8pyT2G3gPsr-ABODJUrlH_-yei479BQU9YytP7ChgeFmMHSgjrZ0xAMM-AAAAJERERjY4MTcxLTQwOUQtNEUyQy05MUYwLTlFNDJENzc0NTM2NQ"
    },
    "password" : "bar",
    "request_nonce" : "AwABAAAAAAADAOz_BADv_xtgu_SM1Mvoq02PYz_YfXxx5FAgcLHLNikH6gjrBWwcqnRW_haxqO9JCiPat5KfkTily04S8EH3AQwVsWCxHYQgAA",
    "scope" : "openid offline_access urn:apple:platformsso",
    "grant_type" : "password",
    "username" : "foo",
    "aud" : "https://localhost.apple.com:8888/auth/token",
    "client_id" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "nonce" : "DDF68171-409D-4E2C-91F0-9E42D7745365"
}
```

The signed and encoded login JWT output is:

```shell
ewogICJraWQiIDogIldzOW1LeW5aeHlVU05YWXRNR0FqakxPK0pnMTZIQ2EvNXBKTzB1ZE5XSjQ9IiwKICAieDVjIiA6ICJNSUlCaERDQ0FTbWdBd0lCQWdJQkFUQUtCZ2dxaGtqT1BRUURBakEzTVJRd0VnWURWUVFERXd0a1pYWnBZMlVnZEdWemRERUxNQWtHQTFVRUJoTUNWVk14RWpBUUJnTlZCQW9UQ1VGd2NHeGxJRWx1WXpBZUZ3MHlNakEyTWpNeE56STFNekZhRncweU16QTJNak14TnpJMU16RmFNRGN4RkRBU0JnTlZCQU1UQzJSbGRtbGpaU0IwWlhOME1Rc3dDUVlEVlFRR0V3SlZVekVTTUJBR0ExVUVDaE1KUVhCd2JHVWdTVzVqTUZrd0V3WUhLb1pJemowQ0FRWUlLb1pJemowREFRY0RRZ0FFZ0s2MEVneFQrRWlweUFnU2xySEcwTGdGVnJnbmQ4VVhBdkxPZ3lrSnRtczhBalB0aXNmaEhIUFd1Vitmb2x5ZkJLWVVOVVpqVWhLVWFlWXJVMWZtKzZNbU1DUXdFZ1lEVlIwVEFRSC9CQWd3QmdFQi93SUJBREFPQmdOVkhROEJBZjhFQkFNQ0I0QXdDZ1lJS29aSXpqMEVBd0lEU1FBd1JnSWhBTXdHT1l3Z2Y1eEd4TmNaTEwvWTRwaEE2NncvUFNWTGVRWWhlYzJKVFFGMUFpRUFsTlNVRHljdnYwRHdEUVlVNHdVcGNvL0dCdWhjNG1QbWxpMytEVCtwMUlzPSIsCiAgInR5cCIgOiAiSldUIiwKICAiYWxnIiA6ICJFUzI1NiIKfQ.ewogICJpYXQiIDogIjE2NTYwMDUxMzIiLAogICJqd2VfY3J5cHRvIiA6IHsKICAgICJhbGciIDogIkVDREgtRVMiLAogICAgImVuYyIgOiAiQTI1NkdDTSIsCiAgICAiYXB2IiA6ICJBQUFBQlVGd2NHeGxBQUFBUVFSTy1RODRmakt4eXRJTFdzVmktY0ZVOWd5ck5IVzhweVQyRzNnUHNyLUFCT0RKVXJsSF8teWVpNDc5QlFVOVl5dFA3Q2hnZUZtTUhTZ2pyWjB4QU1NLUFBQUFKRVJFUmpZNE1UY3hMVFF3T1VRdE5FVXlReTA1TVVZd0xUbEZOREpFTnpjME5UTTJOUSIKICB9LAogICJwYXNzd29yZCIgOiAiYmFyIiwKICAicmVxdWVzdF9ub25jZSIgOiAiQXdBQkFBQUFBQUFEQU96X0JBRHZfeHRndV9TTTFNdm9xMDJQWXpfWWZYeHg1RkFnY0xITE5pa0g2Z2pyQld3Y3FuUldfaGF4cU85SkNpUGF0NUtma1RpbHkwNFM4RUgzQVF3VnNXQ3hIWVFnQUEiLAogICJzY29wZSIgOiAib3BlbmlkIG9mZmxpbmVfYWNjZXNzIHVybjphcHBsZTpwbGF0Zm9ybXNzbyIsCiAgImdyYW50X3R5cGUiIDogInBhc3N3b3JkIiwKICAidXNlcm5hbWUiIDogImZvbyIsCiAgImF1ZCIgOiAiaHR0cHM6Ly9sb2NhbGhvc3QuYXBwbGUuY29tOjg4ODgvYXV0aC90b2tlbiIsCiAgImNsaWVudF9pZCIgOiAiYWFmZjE1MjQtZmEzNS00MGM1LTk0ZTMtMmIyMzNjNWYyOTY1IiwKICAibm9uY2UiIDogIkRERjY4MTcxLTQwOUQtNEUyQy05MUYwLTlFNDJENzc0NTM2NSIKfQ.JMD4NkC0bwrQ0GZI66EMo50Rwgfj3fewTc_6836zWbyvNwcCSNmL9hKIgJx-oFoiwZ0dtYYN5KPI3MHLg3-GBw
```

##### Encrypt the Response

Use the following ephemeral key, response header, and plain text to generate a sample encrypted response. The plain text is encrypted and all data values are base-64 URL encoded.

`}`

##### Perform Diffie Hellman Key Exchange

Diffie–Hellman key exchange is a method to securely exchange cryptographic keys over a public channel.

Use the device encryption public key and the ephemeral private key to perform Diffie-Hellman key exchange ([`ecdhKeyExchangeStandard`](https://developer.apple.com/documentation/Security/SecKeyAlgorithm/ecdhKeyExchangeStandard)).

##### Perform Concatkdf

ConcatKDF is a concatenation Key Derivation Function (KDF) to derive a shared key from the result of performing Diffie-Hellman key exchange.

Perform ConcatKDF using the key exchange result, algorithm, `PartyUInfo`, and `PartyVInfo`: Here are the values that these code snippets use, including the data before the hash and the computed key (output):

##### Encrypt the Plain Text

The system uses the key from ConcatKDF with the Initialization Vector (IV) and the Additional Authentication Data (AAD) to encrypt the plain text using AESGCM. The AAD is the ASCII-encoded response header per RFC 7516 Section 5.1, Step 14. The response header was already base-64 URL encoded. Here are the values that these code snippets use, and the output:

##### Verify the Login Jwe Response

Check the response to confirm that it matches the following output when formatted as a JWE with compact serialization. The system formats the response per RFC 7516 Section 5.1, Step 19. The JWE encrypted key is empty because the system uses direct key agreement:

```shell
ewogICJlbmMiIDogIkEyNTZHQ00iLAogICJraWQiIDogInBTY251engzeDg1RXlwNkN0SzlVUUFEeE9zQUdUUDcyeTAyVGczbTFzazg9IiwKICAiZXBrIiA6IHsKICAgICJ5IiA6ICJlcmY5bkVrRUM4U2l1d1AtN2Y3dWREN0NuWDVLRWF1VklmQlBvcW5tbFlvIiwKICAgICJ4IiA6ICJWSVhkZ3UzeDBlTGdFVnRST1o1WVE0R1VTOFdaUVQtM0hQcVgyRlBvWTRJIiwKICAgICJrdHkiIDogIkVDIiwKICAgICJjcnYiIDogIlAtMjU2IgogIH0sCiAgImFwdSIgOiAiQUFBQUJVRlFVRXhGQUFBQVFRUlVoZDJDN2ZIUjR1QVJXMUU1bmxoRGdaUkx4WmxCUDdjYy1wZllVLWhqZ25xM19aeEpCQXZFb3JzRF91My03blEtd3AxLVNoR3JsU0h3VDZLcDVwV0siLAogICJ0eXAiIDogIkpXVCIsCiAgImFsZyIgOiAiRUNESC1FUyIKfQ..cFAKroCUiODyXmdK.Clpc69y98u7GwODBB9u4ZIcxyOY-MHlVmPIlP5Tz9pKKMLJfHTKkWtHpP1Y8YKAdT7iuRN09bTNRgArfPLIlo7WkUolOGoU3oV07p3m3cOmTzmVqOmVs0dXlEVZlF21TX_hjN2sj5RpC4tWBdKVdoCej4u0Brkgypw0jXtKUzjIM2HcE-8Yy4fC-ixTnescR1M3eM_6IWRR1MtEYTy1C7JrBcw9gZVSmvC1DpeH49gYw9FkIQUpdnfvyreVU0DfvqhABvp29fpVmQqoaENoLuqDt0Ajfko5LWRz3sLcZipoZ0gdRgwQpcNLnBUYAZs5D7t8Yuay2CZjAoTZcbFv4F8Mrg2BgEncVwhC9jTEVGe3GinlsziPdSVIt-7lXbV99yk2qX0eYb4ItScWgUfl3y_p623Xtr3AOxlslahF7fm8PN3sAJnwb_aQQxeeQZQyRZKD9uMHHUTMZeoJbXxV1KdGgQMYdW0Z40_WYFtqT8UwboptazbZX02GOmz2gO7JSe0OHgLCPAfvp9Ah2apYrEDqp01tYwhCG8SNuBB_sXPuJx-euUuxu70s1809k44A_hAc_iYDPwTBpAXBLOiuJIxVZgy54WNNiP_WqBImjsA1ioE7Mrvqkn-DnkM0NP2rt1GvaZ-IpUNgAXKudjiT51guQLnRcr9r3pNmmIaUrqKepMJdAYqUbc9PjYUus7RX-20r5pudVi8Ef0Tg5y9Hk3f7sfiX9peBea_L5yQP-tjXJN8lITRBFCtvvsTb0ALVbKTTHiItmYFxl7XzAljiOMiXEKDKwb0VqOtkU4Ljdz2_M7mW0sT1M6_8XZ6dn3W9RMAeqmLnKlxU5gxj0rK5C8Dnok-I2jOlDzr7uS01WBmaln4E2MTRLyGsdUhXk6JLewtomMTrM7dfq1x6iZubbV8fOk4ayKlEh6xQONPfUXAnr-OB45gllZ2GWNaipd9nwJyGnktSQYpjHiMgl-eKQ3nwwD6Tnj9yYZgvq-D5_DUknvk1XMGTF1CAKaGWDWvf4t2LTyxLld6qgDKyrQWYVKRbHY5LtUqlQjTUP9WGVCNnojVfEIVJIxGXspgL_QwViuBBkmHa_IEd18UE68_yhtBh1dxi_K3td6AG01_Fm1UgYNhi4SPHJqA22zJQ397HdAAGk1bYk5IacY9qyqpVXPBRhEE92DG5oDZcCUB9li87NWRJIaF46Q1z5S2ROSBimBi-nyOX5G4DpgrPjst3lK7NacpssjdPk2fDh3XXKu2r4RXBr7l7hweuwKNgyzPBoTZ37dadYKz1MpxO5Ag43xLzTougLDkVrS5w.4dpX5cVdPodXep2NyC2Vyg
```

##### Decrypt the Jwe

The system calculates the key differently when decrypting the JWE. For decryption, the system performs Diffie-Hellman key exchange ([`ecdhKeyExchangeStandard`](https://developer.apple.com/documentation/Security/SecKeyAlgorithm/ecdhKeyExchangeStandard)) using the device encryption private key and the ephemeral public key from the JWE header. The other inputs for ConcatKDF are the same and the system uses the calculated key for AESGCM decryption using the fields from the encrypted JWE.

## See Also

- [Creating a JSON Web Encryption (JWE) login response](creating-a-json-web-encryption-jwe-login-response.md)
  Create an encrypted login response and configure the concatenation key derivation function (Concat KDF).
- [Processing the JSON Web Encryption (JWE) login response](processing-the-json-web-encryption-jwe-login-response.md)
  Validate the encrypted response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/performing-encryption-verification)*