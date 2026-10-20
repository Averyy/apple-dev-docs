# allObjects

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

All the objects in the receiver.

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
var allObjects: [Any] { get }
```

```objc
@property (copy, readonly) NSArray * allObjects;
```

## See Also

### Managing the Collection
- [var count: Int](./count.md)
  The number of elements in the receiver.
- [func pointer(at: Int) -> UnsafeMutableRawPointer?](./pointer%28at%29.md)
  Returns the pointer at a given index.
- [func addPointer(UnsafeMutableRawPointer?)](./addpointer%28_%29.md)
  Adds a given pointer to the receiver.
- [func removePointer(at: Int)](./removepointer%28at%29.md)
  Removes the pointer at a given index.
- [func insertPointer(UnsafeMutableRawPointer?, at: Int)](./insertpointer%28_,at%29.md)
  Inserts a pointer at a given index.
- [func replacePointer(at: Int, withPointer: UnsafeMutableRawPointer?)](./replacepointer%28at,withpointer%29.md)
  Replaces the pointer at a given index.
- [func compact()](./compact%28%29.md)
  Removes `NULL` values from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/allobjects)*