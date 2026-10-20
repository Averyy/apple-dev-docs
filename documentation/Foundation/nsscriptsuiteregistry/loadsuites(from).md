# loadSuites(from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Loads the suite definitions in bundle `aBundle`, invoking [`loadSuite(with:from:)`](./loadsuite%28with,from%29.md) for each suite found.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func loadSuites(from bundle: Bundle)
```

```objc
- (void) loadSuitesFromBundle:(NSBundle *) bundle;
```

#### Discussion

If errors occur while method is parsing a suite-definition file, the method logs error messages to the console.

## See Also

### Loading Suites
- [func loadSuite(with: [AnyHashable : Any], from: Bundle)](./loadsuite%28with,from%29.md)
  Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/loadsuites(from:))*