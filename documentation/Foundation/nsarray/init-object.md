# init(object:)

**Framework**: Foundation  
**Kind**: init

Creates and returns an array containing a given object.

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
convenience init(object anObject: Any)
```

#### Return Value

An array containing the single element `anObject`.

#### Discussion

Alternatively, you can use array literal syntax in Objective-C or Swift to create an array containing a given object:

## Parameters

- `anObject`: An object.

## See Also

- [init?(contentsOfURL: URL)](nsarray/init(contentsofurl:)-fk8x.md)
  Creates and returns an array containing the contents specified by a given URL.
- [convenience init(objects: UnsafePointer<AnyObject>, count: Int)](nsarray/init(objects:count:)-7dct1.md)
  Creates and returns an array that includes a given number of objects from a given C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/init(object:))*