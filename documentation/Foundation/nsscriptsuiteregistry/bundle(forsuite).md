# bundle(forSuite:)

**Framework**: Foundation  
**Kind**: method

Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func bundle(forSuite suiteName: String) -> Bundle?
```

## See Also

- [func aeteResource(String) -> Data?](nsscriptsuiteregistry/aeteresource(_:).md)
  Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.
- [func appleEventCode(forSuite: String) -> FourCharCode](nsscriptsuiteregistry/appleeventcode(forsuite:).md)
  Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/bundle(forsuite:))*