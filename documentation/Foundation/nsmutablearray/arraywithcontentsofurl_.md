# arrayWithContentsOfURL:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a mutable array containing the contents specified by a given URL.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSMutableArray<id> *) arrayWithContentsOfURL:(NSURL *) url;
```

## Return Value

A mutable array containing the contents specified by `aURL`. Returns `nil` if the location can’t be opened or if the contents of the location can’t be parsed into a mutable array.

## Discussion

The array representation at the location identified by `aURL` must contain only property list objects (`NSString`, `NSData`, `NSDate`, `NSNumber`, `NSArray`, or `NSDictionary` objects). The objects contained by this array are immutable even if the array is mutable.

## Parameters

- `url`: The location of the file containing a string representation of a mutable array produced by the `writeToURL:atomically:` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablearray/arraywithcontentsofurl:)*