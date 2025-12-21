# main

**Framework**: Foundation  
**Kind**: property

Returns the bundle object that contains the current executable.

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
class var main: Bundle { get }
```

#### Return Value

The `NSBundle` object corresponding to the bundle directory that contains the current executable. This method may return a valid bundle object even for unbundled apps. It may also return `nil` if the bundle object could not be created, so always check the return value.

#### Discussion

The main bundle lets you access the resources in the same directory as the currently running executable. For a running app or code running in a framework, the main bundle offers access to the app’s bundle directory.

## See Also

- [Resource Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingResources/Introduction/Introduction.html#//apple_ref/doc/uid/10000051i)
- [init(for: AnyClass)](bundle/init(for:).md)
  Returns the `NSBundle` object with which the specified class is associated.
- [Bundle Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i)
- [class var allFrameworks: [Bundle]](bundle/allframeworks.md)
  Returns an array of all of the application’s bundles that represent frameworks.
- [class var allBundles: [Bundle]](bundle/allbundles.md)
  Returns an array of all the application’s non-framework bundles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/main)*