# localizedTermsAndConditionsText

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A localized, user-readable string that summarizes the terms and conditions of your company’s services.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var localizedTermsAndConditionsText: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) NSString * localizedTermsAndConditionsText;
```

*macOS*

```objc
@property (atomic, readonly) NSString * localizedTermsAndConditionsText;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Terms and Conditions
- [var privacyPolicyURL: URL?](./privacypolicyurl.md)
  The URL to your company’s privacy policy web page.
- [var termsAndConditionsURL: URL?](./termsandconditionsurl.md)
  The URL to your company’s terms and conditions web page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intermsandconditions/localizedtermsandconditionstext)*