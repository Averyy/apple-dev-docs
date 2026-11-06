# getReferenceSex:error:

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```objc
- (BOOL) getReferenceSex:(HKReferenceSex *) referenceSex error:(NSError **) error;
```

## Discussion

Reads the sex whose reference ranges should be used when classifying a clinical measurement for the user.

Before calling this method, the application should request authorization to access objects with the HKCharacteristicType identified by HKCharacteristicTypeIdentifierReferenceSex.

```
           Returns YES and sets referenceSex when the read succeeds; HKReferenceSexNotSet then means the
           user has not provided a value. Returns NO and populates error when read authorization was not
           granted or the read itself failed, and leaves referenceSex unchanged.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/getreferencesex:error:)*