# Storing a Certificate in the Keychain

**Framework**: Security

Store a certificate in the keychain for safekeeping.

#### Overview

If you receive a certificate, perhaps from a `.cer` file, as shown in [`Storing a DER-Encoded X.509 Certificate`](storing-a-der-encoded-x-509-certificate.md), you can store it in your keychain for safekeeping. As with other keychain operations, begin by creating a query:

**Swift**:

```swift
let addquery: [String: Any] = [kSecClass as String: kSecClassCertificate,
                               kSecValueRef as String: certificate,
                               kSecAttrLabel as String: "My Certificate"]
```

**Objective-C**:

```objc
NSDictionary* addquery = @{ (id)kSecValueRef:   (__bridge id)certificate,
                            (id)kSecClass:      (id)kSecClassCertificate,
                            (id)kSecAttrLabel:  @"My Certificate",
                           };
```

In addition to including the certificate reference itself and the [`kSecClassCertificate`](ksecclasscertificate.md) attribute value, you add a label with the [`kSecAttrLabel`](ksecattrlabel.md) attribute, making it easier to search for the certificate later.

You then supply the query to the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) function:

**Swift**:

```swift
let status = SecItemAdd(addquery as CFDictionary, nil)
guard status == errSecSuccess else { throw <# an error #> }
```

**Objective-C**:

```objc
OSStatus status = SecItemAdd((__bridge CFDictionaryRef)addquery, NULL);
if (status != errSecSuccess) {
    // Handle the error
}
```

As always, test the return status before proceeding. Because you don’t need another reference to the certificate in this case, you omit the [`kSecReturnRef`](ksecreturnref.md) attribute from the query dictionary and leave the second argument to the function call empty.

Later, when you want to read the certificate back from the keychain, create a new query dictionary:

**Swift**:

```swift
let getquery: [String: Any] = [kSecClass as String: kSecClassCertificate,
                               kSecAttrLabel as String: "My Certificate",
                               kSecReturnRef as String: kCFBooleanTrue]
```

**Objective-C**:

```objc
NSDictionary *getquery = @{ (id)kSecClass:     (id)kSecClassCertificate,
                            (id)kSecAttrLabel: @"My Certificate",
                            (id)kSecReturnRef: @YES,
                            };
```

This query dictionary again uses the [`kSecClassCertificate`](ksecclasscertificate.md) value for the [`kSecClass`](ksecclass.md) entry to specify a search for a certificate item (as opposed to a key, identity, or password). Further, the query indicates the label you used when you stored the certificate. Finally, it says that the retrieval should return a certificate reference (rather than the data itself).

Use this query with the [`SecItemCopyMatching(_:_:)`](secitemcopymatching(_:_:).md) function:

**Swift**:

```swift
var item: CFTypeRef?
let status = SecItemCopyMatching(getquery as CFDictionary, &item)
guard status == errSecSuccess else { throw <# an error #> }
let certificate = item as! SecCertificate
```

**Objective-C**:

```objc
SecCertificateRef certificate = NULL;
OSStatus status = SecItemCopyMatching((__bridge CFDictionaryRef)getquery,
                                      (CFTypeRef *)&certificate);
if (status != errSecSuccess) { <# Handle error #> }
else                         { <# Use certificate #> }
 
if (certificate) { CFRelease(certificate); } // After you are done with it
```

Assuming the call is successful, the function populates the item reference. In Objective-C, when you are done with the certificate, you are responsible for freeing the object’s memory. In Swift, the system manages the object’s memory automatically, releasing it when the certificate goes out of scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/storing-a-certificate-in-the-keychain)*