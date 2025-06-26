# ~=(_:_:)

**Framework**: Translation  
**Kind**: op

This operator allows you to check for a given value of a translation error and handle each error case.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
static func ~= (match: TranslationError, error: any Error) -> Bool
```

#### Discussion

You can use `switch` and `case` to check for a given value of `TranslationError`, if you want to handle each error case separately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/~=(_:_:))*