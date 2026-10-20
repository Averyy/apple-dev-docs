# aeteResource(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an `NSData` object that contains data in `'aete'` resource format describing the scriptability information currently known to the application.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func aeteResource(_ languageName: String) -> Data?
```

```objc
- (NSData *) aeteResource:(NSString *) languageName;
```

#### Discussion

This method is typically invoked to implement the `get aete` Apple event for an application that provides scriptability information in the script suite format. The `languageName` argument is the name of a language for which a localized resource directory (such as `English.lproj`) exists. This language indication specifies the set of `.scriptTerminology` files to be used to generate the data. `NSScriptSuiteRegistry` does not create an `'aete'` resource unless this method is called.

## See Also

### Getting Other Suite Information
- [func appleEventCode(forSuite: String) -> FourCharCode](./appleeventcode%28forsuite%29.md)
  Returns the Apple event code associated with the suite named `suiteName`, such as `‘core’` for the Core suite.
- [func bundle(forSuite: String) -> Bundle?](./bundle%28forsuite%29.md)
  Returns the bundle containing the suite-definition property list (extension `.scriptSuite`) identified by `suiteName`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/aeteresource(_:))*