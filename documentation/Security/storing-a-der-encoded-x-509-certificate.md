# Storing a DER-Encoded X.509 Certificate

**Framework**: Security

Import and export a certificate from a file.

#### Overview

Certificates are not secret and you often want to share them to disseminate a public key, but [`SecCertificate`](seccertificate.md) is an opaque type that you can’t distribute directly. Instead, you create a Distinguished Encoding Rules (DER) encoded data representation of the certificate using the [`SecCertificateCopyData(_:)`](seccertificatecopydata(_:).md) function:

**Swift**:

```swift
let certificate = <# a certificate #>
let certData = SecCertificateCopyData(certificate) as Data
```

**Objective-C**:

```objc
SecCertificateRef certificate = <# a certificate #>;
NSData* certData = (NSData*)CFBridgingRelease( // ARC takes ownership
                       SecCertificateCopyData(certificate)
                    );
```

You might send this data object over a network connection or store it in a `.cer` file:

**Swift**:

```swift
certData.write(to: <# a URL #>)
```

**Objective-C**:

```objc
[certData writeToURL:<# a URL #> atomically:YES];
```

When you receive such a data object, you use the [`SecCertificateCreateWithData(_:_:)`](seccertificatecreatewithdata(_:_:).md) function to reverse the process:

**Swift**:

```swift
let certificate = SecCertificateCreateWithData(nil, certData as CFData)
```

**Objective-C**:

```objc
SecCertificateRef certificate =
    SecCertificateCreateWithData(NULL, (__bridge CFDataRef)certData);
		 
if (certificate)  { CFRelease(certificate); } // After you are done with it
```

By leaving the first argument empty, you rely on the default allocator to allocate memory for the certificate. Note that in Objective-C, you call [`CFRelease`](https://developer.apple.com/documentation/corefoundation/cfrelease) to free the certificate’s memory when you are done with it. In Swift, the system manages the object’s memory automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/storing-a-der-encoded-x-509-certificate)*