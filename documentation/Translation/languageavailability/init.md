# init()

**Framework**: Translation  
**Kind**: init

Creates an instance to check what languages are available.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
init()
```

#### Discussion

This initializer uses the default translation strategy based on the SDK version your app was built with. Apps built with iOS 26.4 or macOS 26.4 SDKs and later default to checking for Apple Intelligence models when available. Apps built with earlier SDKs default to traditional models.

To explicitly specify which translation models to check for, use [`init(preferredStrategy:)`](languageavailability/init(preferredstrategy:).md).

## See Also

- [init(preferredStrategy: TranslationSession.Strategy)](languageavailability/init(preferredstrategy:).md)
  Creates an instance for checking language availability with a preferred translation strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/init())*