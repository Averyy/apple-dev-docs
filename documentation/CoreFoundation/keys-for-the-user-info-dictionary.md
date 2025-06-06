# Keys for the user info dictionary

**Framework**: Core Foundation

Keys in the `userInfo` dictionary.

#### Overview

When you create a user info dictionary, at a minimum you should provide values for one of `kCFErrorLocalizedDescriptionKey` and `kCFErrorLocalizedFailureReasonKey`; ideally you should provide values for `kCFErrorLocalizedDescriptionKey`, `kCFErrorLocalizedFailureReasonKey`, and  `kCFErrorLocalizedRecoverySuggestionKey`. Typically, you should provide a value for one of either `kCFErrorURLKey` or `kCFErrorFilePathKey`.

## Topics

### Constants
- [let kCFErrorLocalizedDescriptionKey: CFString!](kcferrorlocalizeddescriptionkey.md)
  Key to identify the user-presentable description in the `userInfo` dictionary.
- [let kCFErrorLocalizedFailureReasonKey: CFString!](kcferrorlocalizedfailurereasonkey.md)
  Key to identify the user-presentable failure reason in the `userInfo` dictionary.
- [let kCFErrorLocalizedRecoverySuggestionKey: CFString!](kcferrorlocalizedrecoverysuggestionkey.md)
  Key to identify the user-presentable recovery suggestion in the `userInfo` dictionary.
- [let kCFErrorDescriptionKey: CFString!](kcferrordescriptionkey.md)
  Key to identify the description in the `userInfo` dictionary.
- [let kCFErrorUnderlyingErrorKey: CFString!](kcferrorunderlyingerrorkey.md)
  Key to identify the underlying error in the `userInfo` dictionary.
- [let kCFErrorURLKey: CFString!](kcferrorurlkey.md)
  Key to identify associated URL in the `userInfo` dictionary.
- [let kCFErrorFilePathKey: CFString!](kcferrorfilepathkey.md)
  Key to identify associated file path in the `userInfo` dictionary.

## See Also

- [Error domains](error-domains.md)
  These constants define domains for CFError objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/keys-for-the-user-info-dictionary)*