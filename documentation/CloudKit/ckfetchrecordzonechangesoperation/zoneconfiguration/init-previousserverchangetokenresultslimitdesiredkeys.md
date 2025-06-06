# init(previousServerChangeToken:resultsLimit:desiredKeys:)

**Framework**: CloudKit  
**Kind**: init

Creates a zone configuration with the desired keys and a result limit for updates.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS ?+
- watchOS 5.0+
- Swift 4.2+

## Declaration

```swift
convenience init(previousServerChangeToken: CKServerChangeToken? = nil, resultsLimit: Int? = nil, desiredKeys: [CKRecord.FieldKey]? = nil)
```

## Parameters

- `previousServerChangeToken`: A CloudKit server change token.
- `resultsLimit`: The maximum number of updated records that CloudKit retrieves with an update operation. The default is 0.
- `desiredKeys`: An array of the desired record keys CloudKit retrieves with updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/zoneconfiguration/init(previousserverchangetoken:resultslimit:desiredkeys:))*