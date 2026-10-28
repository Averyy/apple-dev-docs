# shared()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Type Method

Returns a fully initialized, singleton certificate panel object.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class func shared() -> SFCertificatePanel!
```

```objc
+ (SFCertificatePanel *) sharedCertificatePanel;
```

## Discussion

Use this method if your application displays a single certificate panel or sheet at a time. If your application can display multiple certificate panels or sheets at once, you must allocate separate object instances (using the [`alloc`](../../ObjectiveC/nsobject-swift.class/alloc.md) class method inherited from [`NSObject`](../../ObjectiveC/nsobject-swift.class.md)) and initialize them (using the [`init()`](../../ObjectiveC/nsobject-swift.class/init%28%29.md) instance method, also inherited from [`NSObject`](../../ObjectiveC/nsobject-swift.class.md)) instead of using this class method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/shared())*