# arrayWithContentsOfURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns an array containing the contents specified by a given URL.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```objc
+ (NSArray<id> *) arrayWithContentsOfURL:(NSURL *) url;
```

#### Return Value

An array containing the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into an array.

#### Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable, even if the array is mutable.

## Parameters

- `url`: The location of a file containing a string representation of an array produced by the `writeToURL:atomically:` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/arraywithcontentsofurl:)*