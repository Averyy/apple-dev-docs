# loadSuites(from:)

**Framework**: Foundation  
**Kind**: method

Loads the suite definitions in bundle `aBundle`, invoking [`loadSuite(with:from:)`](nsscriptsuiteregistry/loadsuite(with:from:).md) for each suite found.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func loadSuites(from bundle: Bundle)
```

#### Discussion

If errors occur while method is parsing a suite-definition file, the method logs error messages to the console.

## See Also

- [func loadSuite(with: [AnyHashable : Any], from: Bundle)](nsscriptsuiteregistry/loadsuite(with:from:).md)
  Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/loadsuites(from:))*