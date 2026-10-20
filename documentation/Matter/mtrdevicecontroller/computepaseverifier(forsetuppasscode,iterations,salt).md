# computePASEVerifier(forSetupPasscode:iterations:salt:)

**Framework**: Matter  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
class func computePASEVerifier(forSetupPasscode setupPasscode: NSNumber, iterations: NSNumber, salt: Data) throws -> Data
```

```objc
+ (NSData *) computePASEVerifierForSetupPasscode:(NSNumber *) setupPasscode iterations:(NSNumber *) iterations salt:(NSData *) salt error:(NSError **) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicecontroller/computepaseverifier(forsetuppasscode:iterations:salt:))*