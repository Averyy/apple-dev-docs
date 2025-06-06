# appleEventCode(forSuite:)

**Framework**: Foundation  
**Kind**: method

Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func appleEventCode(forSuite suiteName: String) -> FourCharCode
```

## See Also

- [func suite(forAppleEventCode: FourCharCode) -> String?](nsscriptsuiteregistry/suite(forappleeventcode:).md)
  Returns the name of the suite definition associated with the given four-character Apple event code, `code`.
- [func aeteResource(String) -> Data?](nsscriptsuiteregistry/aeteresource(_:).md)
  Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.
- [func bundle(forSuite: String) -> Bundle?](nsscriptsuiteregistry/bundle(forsuite:).md)
  Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/appleeventcode(forsuite:))*