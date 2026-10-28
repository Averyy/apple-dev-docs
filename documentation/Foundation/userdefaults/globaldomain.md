# globalDomain

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The identifier for the domain that contains system-specified settings for all apps.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let globalDomain: String
```

```c
extern NSString * const NSGlobalDomain;
```

## Discussion

The system populates this domain with information that’s relevant to all apps. For example, this domain contains the current language settings for the device. You can read values from this domain, but don’t write your own settings to it.

## See Also

### Getting the domain names
- [class let argumentDomain: String](./argumentdomain.md)
  The identifier for the domain that contains command-line settings.
- [class let registrationDomain: String](./registrationdomain.md)
  The identifier for the domain that contains your app’s registered default values.
- [var volatileDomainNames: [String]](./volatiledomainnames.md)
  An array of identifiers for the volatile domains associated with the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/globaldomain)*