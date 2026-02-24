# Getting Certificate Values

**Framework**: Security

Obtain all the values associated with a certificate.

#### Overview

In macOS, you can also dig deeper into the certificate content using a call to the [`SecCertificateCopyValues(_:_:_:)`](seccertificatecopyvalues(_:_:_:).md) function:

**Swift**:

```swift
var error: Unmanaged<CFError>?
guard let dict = SecCertificateCopyValues(certificate,nil,&error) else {
    throw error!.takeRetainedValue() as Error
}
```

**Objective-C**:

```objc
CFErrorRef error = NULL;
NSDictionary* dict = (NSDictionary*)CFBridgingRelease(  // ARC takes ownership
                       SecCertificateCopyValues(certificate, NULL, &error)
                    );
if (!dict) {
    NSError *err = CFBridgingRelease(error);            // ARC takes ownership
    // Handle the error. . .
}
```

The return value is a dictionary with keys corresponding to the OID values found in [`Certificate OIDs`](certificate-oids.md). Each value is itself a dictionary that contains information about the certificate’s fields and extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/getting-certificate-values)*