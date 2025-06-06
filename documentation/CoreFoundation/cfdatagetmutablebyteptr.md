# CFDataGetMutableBytePtr(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a pointer to a mutable byte buffer of a CFMutableData object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFDataGetMutableBytePtr(_ theData: CFMutableData!) -> UnsafeMutablePointer<UInt8>!
```

#### Return Value

A pointer to the bytes associated with `theData`.

#### Discussion

If the length of `theData`‘s data is not zero, this function is guaranteed to return a pointer to a CFMutableData object’s internal bytes. If the length of `theData`’s data  zero, this function may or may not return `NULL` dependent upon many factors related to how the object was created (moreover, in this case the function result might change between different releases and on different platforms).

## Parameters

- `theData`: A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatagetmutablebyteptr(_:))*