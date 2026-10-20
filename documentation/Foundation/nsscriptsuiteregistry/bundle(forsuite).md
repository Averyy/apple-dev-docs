# bundle(forSuite:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func bundle(forSuite suiteName: String) -> Bundle?
```

```objc
- (NSBundle *) bundleForSuite:(NSString *) suiteName;
```

## See Also

### Getting Other Suite Information
- [func aeteResource(String) -> Data?](./aeteresource%28_%29.md)
  Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.
- [func appleEventCode(forSuite: String) -> FourCharCode](./appleeventcode%28forsuite%29.md)
  Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/bundle(forsuite:))*