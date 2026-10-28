# siriLanguageCode()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Returns the language that Siri uses to communicate with the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func siriLanguageCode() -> String
```

```objc
+ (NSString *) siriLanguageCode;
```

## Return Value

The locale ID that identifies the language and any optional region or script information. Examples of locale IDs are “en”, “en_GB”, “zh-Hans”, and “zh-Hans_HK”. For more information about the structure of locale IDs, see [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

## Discussion

This property is for informational purposes only. Siri’s input language can be different than the language displayed on the user’s device. However, your app and Intents extension should always specify content using the user’s preferred language, as indicated by the language settings of the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpreferences/sirilanguagecode())*