# CFDateGetTimeIntervalSinceDate(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number of elapsed seconds between the given `CFDate` objects.

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
func CFDateGetTimeIntervalSinceDate(_ theDate: CFDate!, _ otherDate: CFDate!) -> CFTimeInterval
```

#### Return Value

The number of elapsed seconds between `theDate` and `otherDate`. The result is positive if `theDate` is later than `otherDate`.

## Parameters

- `theDate`: The date to compare to  .
- `otherDate`: The date to compare to  .

## See Also

- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](cfdatecompare(_:_:_:).md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](cfdatecreate(_:_:).md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](cfdategetabsolutetime(_:).md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTypeID() -> CFTypeID](cfdategettypeid().md)
  Returns the type identifier for the `CFDate` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdategettimeintervalsincedate(_:_:))*