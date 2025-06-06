# version

**Framework**: Apple Pay on the Web  
**Kind**: property

The Apple Pay version supported on your website.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
required long version;
```

#### Discussion

The version number you provide here represents the minimum Apple Pay version that the user’s browser must support. You can check which API version the browser supports by calling [`supportsVersion`](applepaysession/supportsversion.md).

Always check [`supportsVersion`](applepaysession/supportsversion.md) before using an Apple Pay feature that isn’t available in all versions. See doc://com.apple.documentation/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history for information about the features available in each version.

## See Also

- [merchantIdentifier](applepayrequest/merchantidentifier.md)
  The merchant identifier you registered with Apple for use with Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequest/version)*