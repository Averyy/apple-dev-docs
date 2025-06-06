# CFDateGetAbsoluteTime(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a `CFDate` object’s absolute time.

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
func CFDateGetAbsoluteTime(_ theDate: CFDate!) -> CFAbsoluteTime
```

#### Return Value

The absolute time of `theDate`.

#### Discussion

Absolute time is measured in seconds relative to the absolute reference date of Jan 1 2001 00:00:00 GMT. A positive value represents a date after the reference date, a negative value represents a date before it. For example, the absolute time -32940326 is equivalent to December 16th, 1999 at 17:54:34.

## Parameters

- `theDate`: The date to examine.

## See Also

- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](cfdatecompare(_:_:_:).md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](cfdatecreate(_:_:).md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](cfdategettimeintervalsincedate(_:_:).md)
  Returns the number of elapsed seconds between the given `CFDate` objects.
- [func CFDateGetTypeID() -> CFTypeID](cfdategettypeid().md)
  Returns the type identifier for the `CFDate` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdategetabsolutetime(_:))*