# localizedKeyDictionary

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The localized key names that are displayed by the receiver in place of the key names.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var localizedKeyDictionary: [String : String] { get set }
```

```objc
@property (copy) NSDictionary<NSString *,NSString *> * localizedKeyDictionary;
```

#### Discussion

The dictionary contains the key names as the keys, and the localized key names as the corresponding values.

## See Also

### Localizing Key Names
- [var localizedKeyTable: String?](./localizedkeytable.md)
  the strings file used to localize key names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/localizedkeydictionary)*