# CFDateCompare(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Compares two `CFDate` objects and returns a comparison result.

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
func CFDateCompare(_ theDate: CFDate!, _ otherDate: CFDate!, _ context: UnsafeMutableRawPointer!) -> CFComparisonResult
```

#### Return Value

A [`CFComparisonResult`](cfcomparisonresult.md) value that indicates whether `theDate` is equal to, less than, or greater than `otherDate`.

## Parameters

- `theDate`: The date to compare to  .
- `otherDate`: The date to compare to  .
- `context`: Unused. Pass  .

## See Also

- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](cfdatecreate(_:_:).md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](cfdategetabsolutetime(_:).md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](cfdategettimeintervalsincedate(_:_:).md)
  Returns the number of elapsed seconds between the given `CFDate` objects.
- [func CFDateGetTypeID() -> CFTypeID](cfdategettypeid().md)
  Returns the type identifier for the `CFDate` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatecompare(_:_:_:))*