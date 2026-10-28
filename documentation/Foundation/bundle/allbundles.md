# allBundles

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy, readonly) NSArray<NSBundle *> * allBundles;
```

## Return Value

An array of all the application’s non-framework bundles.

## Discussion

The returned array includes the main bundle and all bundles that have been dynamically created but doesn’t contain any bundles that represent frameworks.

## See Also

### Getting standard bundle objects
- [class var main: Bundle](./main.md)
  Returns the bundle object that contains the current executable.
- [class var allFrameworks: [Bundle]](./allframeworks.md)
  Returns an array of all of the application’s bundles that represent frameworks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/allbundles)*