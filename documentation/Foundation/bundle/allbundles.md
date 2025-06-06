# allBundles

**Framework**: Foundation  
**Kind**: property

Returns an array of all the application’s non-framework bundles.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var allBundles: [Bundle] { get }
```

#### Return Value

An array of all the application’s non-framework bundles.

#### Discussion

The returned array includes the main bundle and all bundles that have been dynamically created but doesn’t contain any bundles that represent frameworks.

## See Also

- [class var main: Bundle](bundle/main.md)
  Returns the bundle object that contains the current executable.
- [class var allFrameworks: [Bundle]](bundle/allframeworks.md)
  Returns an array of all of the application’s bundles that represent frameworks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/allbundles)*