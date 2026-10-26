# init(localizedTermsAndConditionsText:privacyPolicyURL:termsAndConditionsURL:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the terms and conditions object with the specified information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(localizedTermsAndConditionsText: String, privacyPolicyURL: URL?, termsAndConditionsURL: URL?)
```

```objc
- (instancetype) initWithLocalizedTermsAndConditionsText:(NSString *) localizedTermsAndConditionsText privacyPolicyURL:(NSURL *) privacyPolicyURL termsAndConditionsURL:(NSURL *) termsAndConditionsURL;
```

#### Return Value

An initialized terms and conditions object or `nil` if the object could not be created.

## Parameters

- `localizedTermsAndConditionsText`: A localized, user-readable string that summarizes the terms and conditions of your company’s services.
- `privacyPolicyURL`: A URL that links to a more detailed web page describing your company’s privacy policy.
- `termsAndConditionsURL`: A URL that links to a more detailed web page explaining your company’s terms and conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intermsandconditions/init(localizedtermsandconditionstext:privacypolicyurl:termsandconditionsurl:))*