# init(array:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated array by placing in it the objects contained in a given array.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@nonobjc
convenience init(array anArray: NSArray)
```

#### Return Value

An array initialized to contain the objects in `anArray``. The returned object might be different than the original receiver.

#### Discussion

Discussion: After an immutable array has been initialized in this way, it cannot be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(array:)-9rh7)*