# allFrameworks

**Framework**: Foundation  
**Kind**: property

Returns an array of all of the application’s bundles that represent frameworks.

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
class var allFrameworks: [Bundle] { get }
```

#### Return Value

An array of all of the application’s bundles that represent frameworks. Only frameworks with one or more Objective-C classes in them are included.

#### Discussion

The returned array includes frameworks that are linked into an application when the application is built and bundles for frameworks that have been dynamically created.

## See Also

- [class var main: Bundle](bundle/main.md)
  Returns the bundle object that contains the current executable.
- [class var allBundles: [Bundle]](bundle/allbundles.md)
  Returns an array of all the application’s non-framework bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/allframeworks)*