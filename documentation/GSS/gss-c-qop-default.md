# GSS_C_QOP_DEFAULT

**Framework**: GSS  
**Kind**: var

The default Quality of Protection for per-message services.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var GSS_C_QOP_DEFAULT: Int32 { get }
```

#### Discussion

An implementation that offers multiple levels of QOP may define this value to be either zero (as done here) to mean “default protection,” or to a specific explicit QOP value. However, a value of 0 is always interpreted by a GSS-API implementation as a request for the default protection level.

## See Also

- [var GSS_KRB5_CONF_C_QOP_DES: Int32](gss_krb5_conf_c_qop_des.md)
  The Kerberos 5 Qualty of Service 56-bit DES encryption.
- [var GSS_KRB5_CONF_C_QOP_DES3_KD: Int32](gss_krb5_conf_c_qop_des3_kd.md)
  The Kerberos 5 Qualty of Service 168-bit DES3 encryption with key derivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gss/gss_c_qop_default)*