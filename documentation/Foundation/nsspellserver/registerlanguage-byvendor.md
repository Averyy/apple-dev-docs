# registerLanguage(_:byVendor:)

**Framework**: Foundation  
**Kind**: method

Notifies the receiver of a language your spelling checker can check.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func registerLanguage(_ language: String?, byVendor vendor: String?) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the language is registered, [`false`](https://developer.apple.com/documentation/swift/false) if for some reason it can’t be registered.

#### Discussion

If your spelling checker supports more than one language, it should invoke this method once for each language. Registering a language-vendor combination causes it to appear in the Spelling panel’s pop-up menu of spelling checkers.

## Parameters

- `language`: A string specifying the English name of a language on Apple’s list of languages.
- `vendor`: A string that identifies the vendor (to distinguish your spelling checker from those that others may offer for the same language).

## See Also

- [func run()](nsspellserver/run.md)
  Causes the receiver to start listening for spell-checking requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserver/registerlanguage(_:byvendor:))*