# shared()

**Framework**: Foundation  
**Kind**: method

Returns the single, shared instance of `NSScriptSuiteRegistry`, creating it first if it doesn’t exist.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func shared() -> NSScriptSuiteRegistry
```

#### Discussion

If it creates an instance, and if the application provides scriptability information in the script suite format, the method loads suite definitions in all frameworks and other bundles that the application currently imports or includes; if information is provided in the sdef format, the method loads information only from the specified sdef file. If in reading scriptability information an exception is `raised` because of parsing errors, it handles the exception by printing a line of information to the console.

## See Also

- [func loadSuite(with: [AnyHashable : Any], from: Bundle)](nsscriptsuiteregistry/loadsuite(with:from:).md)
  Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.
- [class func setShared(NSScriptSuiteRegistry)](nsscriptsuiteregistry/setshared(_:).md)
  Sets the single, shared instance of `NSScriptSuiteRegistry` to `registry`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/shared())*