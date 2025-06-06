# NSMapEnumerator

**Framework**: Foundation  
**Kind**: struct

Allows successive elements of a map table to be returned each time this structure is passed to [`NSNextMapEnumeratorPair(_:_:_:)`](nsnextmapenumeratorpair(_:_:_:).md).

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
struct NSMapEnumerator
```

#### Overview

The fields of `NSMapEnumerator` are private.

## Topics

### Initializers
- [init()](nsmapenumerator/init.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [NSMapTable](legacy-nsmaptable.md)
  The opaque data type used by the functions described in Managing Map Tables.
- [struct NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.
- [typealias NSMapTableOptions](nsmaptableoptions.md)
  Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
- [struct NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmapenumerator)*