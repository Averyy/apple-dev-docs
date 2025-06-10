# init(serviceIdentifier:label:recordIdentifier:)

**Framework**: Authentication Services  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(serviceIdentifier: ASCredentialServiceIdentifier, label: String, recordIdentifier: String?)
```

## Parameters

- `serviceIdentifier`: The service identifier for which this credential identity is valid.
- `label`: A user-provided label to identify the one time code.
- `recordIdentifier`: An optional string to uniquely identify this record in your local database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asonetimecodecredentialidentity/init(serviceidentifier:label:recordidentifier:))*