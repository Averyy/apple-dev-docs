# appleEventCode(forSuite:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func appleEventCode(forSuite suiteName: String) -> FourCharCode
```

```objc
- (FourCharCode) appleEventCodeForSuite:(NSString *) suiteName;
```

## See Also

### Related Documentation
- [func suite(forAppleEventCode: FourCharCode) -> String?](./suite%28forappleeventcode%29.md)
  Returns the name of the suite definition associated with the given four-character Apple event code, `code`.
### Getting Other Suite Information
- [func aeteResource(String) -> Data?](./aeteresource%28_%29.md)
  Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.
- [func bundle(forSuite: String) -> Bundle?](./bundle%28forsuite%29.md)
  Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/appleeventcode(forsuite:))*