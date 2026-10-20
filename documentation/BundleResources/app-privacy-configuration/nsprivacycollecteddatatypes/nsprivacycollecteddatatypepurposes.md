# NSPrivacyCollectedDataTypePurposes

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An array of strings that identify reasons your app or third-party SDK collects private data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Details

- **Name**: `NSPrivacyCollectedDataTypePurposes` (Collection Purposes)
- **Type**: array of string 

## Possible Values

- `NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising`: Third-party advertising; such as displaying third-party ads in your app, or sharing data with entities who display third-party ads.
- `NSPrivacyCollectedDataTypePurposeDeveloperAdvertising`: Developer’s advertising or marketing; such as displaying first-party ads in your app, sending marketing communications directly to your users, or sharing data with entities who will display your ads.
- `NSPrivacyCollectedDataTypePurposeAnalytics`: Analytics — using data to evaluate user behavior, including to understand the effectiveness of existing product features, plan new features, or measure audience size or characteristics.
- `NSPrivacyCollectedDataTypePurposeProductPersonalization`: Product personalization — customizing what the user sees, such as a list of recommended products, posts, or suggestions.
- `NSPrivacyCollectedDataTypePurposeAppFunctionality`: App functionality; such as to authenticate the user, enable features, prevent fraud, implement security measures, ensure server up-time, minimize app crashes, improve scalability and performance, or perform customer support.
- `NSPrivacyCollectedDataTypePurposeOther`: Any other purposes not listed.

## Mentions

- [Describing data use in privacy manifests](../../describing-data-use-in-privacy-manifests.md)

## See Also

### Reporting categories of collected data
- [NSPrivacyCollectedDataType](./nsprivacycollecteddatatype.md)
  A string that identifies the type of data your app or third-party SDK collects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/app-privacy-configuration/nsprivacycollecteddatatypes/nsprivacycollecteddatatypepurposes)*