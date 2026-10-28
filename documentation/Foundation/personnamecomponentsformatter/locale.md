# locale

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Specifies the locale to format names.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var locale: Locale! { get set }
```

```objc
@property (copy, null_resettable) NSLocale * locale;
```

## Discussion

Defaults to `autoupdatingCurrentLocale`. Also resets to `autoupdatingCurrentLocale` on assignment of `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/locale)*