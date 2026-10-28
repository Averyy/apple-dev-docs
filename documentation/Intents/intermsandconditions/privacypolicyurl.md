# privacyPolicyURL

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The URL to your company’s privacy policy web page.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var privacyPolicyURL: URL? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) NSURL * privacyPolicyURL;
```

*macOS*

```objc
@property (atomic, readonly, nullable) NSURL * privacyPolicyURL;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Terms and Conditions
- [var localizedTermsAndConditionsText: String](./localizedtermsandconditionstext.md)
  A localized, user-readable string that summarizes the terms and conditions of your company’s services.
- [var termsAndConditionsURL: URL?](./termsandconditionsurl.md)
  The URL to your company’s terms and conditions web page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intermsandconditions/privacypolicyurl)*