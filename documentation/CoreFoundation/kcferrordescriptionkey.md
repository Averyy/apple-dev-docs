# kCFErrorDescriptionKey

**Framework**: Core Foundation  
**Kind**: var

Key to identify the description in the `userInfo` dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCFErrorDescriptionKey: CFString!
```

#### Discussion

When you create a CFError object, you can provide a value for this key if you do not have localizable error strings. The description should be a complete sentence if possible, and should not contain the domain name or error code.

## See Also

- [let kCFErrorLocalizedDescriptionKey: CFString!](kcferrorlocalizeddescriptionkey.md)
  Key to identify the user-presentable description in the `userInfo` dictionary.
- [let kCFErrorLocalizedFailureReasonKey: CFString!](kcferrorlocalizedfailurereasonkey.md)
  Key to identify the user-presentable failure reason in the `userInfo` dictionary.
- [let kCFErrorLocalizedRecoverySuggestionKey: CFString!](kcferrorlocalizedrecoverysuggestionkey.md)
  Key to identify the user-presentable recovery suggestion in the `userInfo` dictionary.
- [let kCFErrorUnderlyingErrorKey: CFString!](kcferrorunderlyingerrorkey.md)
  Key to identify the underlying error in the `userInfo` dictionary.
- [let kCFErrorURLKey: CFString!](kcferrorurlkey.md)
  Key to identify associated URL in the `userInfo` dictionary.
- [let kCFErrorFilePathKey: CFString!](kcferrorfilepathkey.md)
  Key to identify associated file path in the `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcferrordescriptionkey)*