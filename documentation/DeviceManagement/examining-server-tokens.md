# Examining Server Tokens

**Framework**: Device Management

View sample encrypted and unencrypted tokens to verify your server tokens are in the right format.

#### Overview

An example S/MIME encrypted token:

```other
Content-Type: application/pkcs7-mime; name="smime.p7m"; smime-type=enveloped-
data
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="smime.p7m"
Content-Description: S/MIME Encrypted Message

MIAGCSqGSIb3DQEHA6CAMIACAQAxggGeMIIBmgIBADCBgTB1MQswCQYDVQQGEwJVUzESMBAGA1UE
ChMJWmlwcG8gSW5jMSgwJgYDVQQDEx9Qcm9maWxlIE1hbmFnZXIgUy9NSU1FIElkZW50aXR5MSgw
JgYJKoZIhvcNAQkBFhlsb2NhbEB6aXBwb2luYzIuYXBwbGUuY29tAgiDS17MvQ95HDANBgkqhkiG
9w0BAQEFAASCAQC/ukglifm8tk/OjyKBWwPbm+uDNHPG+sXLRrwfTlHKRo1jnvYrqKx1bRrpV/GR
mN7WJPBZLOkFat+LoiEmrBUiUs3PnZ+U1FUAnHR66hnomKoX0JBgfuHBGYz9jeyiu1chQShgdOOe
bYQdaFPJ/P57r98yQ2ZmyqcYOWwE0lOcqa77bfRab/YmMsMx2ZE1wUwnFPM71Yq3+vLIGLBRyvAb
4pBxDlRtgGbxs+2gZwEe0MZ4tx/97RGnZbkJt/26v5P4njGiyCvq2hZUwbria7THhMEvmJRjpZNZ
x5BfTjU8a0EHwvvwnYb67LRnjoSMn/JgelRP70O9fhdZ5Y56xhs6MIAGCSqGSIb3DQEHATAdBglg
hkgBZQMEAQIEEF5d7PQ1O8lxOLjSwjNHwFaggASCAeC9GWg9EDLpyO2g6eoOmeIVYXbWXrRt4JRY
TqCB2dWDqc9BJqOYuX5lnULjvkJ8btlBfAMhUXUb/lFF5xNXGxLTtVHvyVK9FUyhikJFweRohWqM
/xtu+7/1rPT9Nmlssla9wcTAh8GsWbs9ZyM7Pnok+o1XOwRLgh1dGvW8EGxlaPWjcHolleFBStV6
lGKJUrUyzgyBvSWo/6Y/Ojb/kfzq/kzS6H7h4YZI69/Js604rpOL6FAeOwKaJLISfUUp/yNHMBr6
wj772MNnoIdVEQs14/Fk+XVDb4xghD1zzeDow+eseb+qEfY7FkgYi2jpdebk9X4BpJ1WGvy4WiA8
biyKpst6zJb0jdJ4TE0zyIcjuVeOXuV/cD1c7YrYQty1Sh3nBsjFwVOsHq33YjapcHf2wuhXW+hh
HNzpkyMKrNcsEK1HpJva2O6vBtxtYZIn5/4kGDeALUiXxVjtvio1gS37lry5YKEwhYJ+cKKe3exZ
xhLfD67AINahDm868kEuKuHIl8gku+gSKAWlUVGNrPNt/M2rM+y4+4cm23R2f3VXYuNncnFFbulF
7VQuGd3wwtKncIACU5rze4b366rRBG1PCvB7abuRcmw9UrgzkRlH8tbOhORZ0Dgimd5knujsbKMA
AAAAAAAAAAAA

```

The decrypted server token in plain text:

```other
Content-Type: text/plain;charset=UTF-8
Content-Transfer-Encoding: 7bit

{"consumer_key":"CK_9dcd8190dde27dfddd9272c657e011f7bec9761676b1b11e46a2f61d3c
b1e482ef22093c7d54b23252f3bdb4d19b4d49","consumer_secret":"CS_27c083df1ab7271e
129cb23325dabaf0de95d087","access_token":"AT_O365587095O8247e0b5288abcdee25642
311746d67b5858ea5cO1389734861908","access_secret":"AS_8c3313de9a3462014c6c96f3
9dd7c3d4342b8cea","access_token_expiry":"2015-01-14T21:27:41Z"}

```

## See Also

- [Interpreting Error Codes](dep-server-interpreting-error-codes.md)
  Interpret the error codes you might encounter or that can happen during authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/examining-server-tokens)*